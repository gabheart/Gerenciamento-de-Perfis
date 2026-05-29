from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from app.forms.auth import LoginForm, RegisterForm
from datetime import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Rota para cadastro de usuário"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            full_name=form.full_name.data,
            password_hash=User.set_password(form.password.data),
            role='user'
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Você pode fazer login agora.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Rota para login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Nome de usuário ou senha inválidos.', 'danger')
            return redirect(url_for('auth.login'))
        
        if not user.is_active:
            flash('Sua conta foi desativada. Entre em contato com o suporte.', 'warning')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember.data)
        user.update_last_login()
        
        flash(f'Bem-vindo, {user.username}!', 'success')
        
        next_page = request.args.get('next')
        if not next_page or url_has_allowed_host_and_scheme(next_page):
            next_page = url_for('main.dashboard')
        
        return redirect(next_page)
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    """Rota para logout"""
    logout_user()
    flash('Você foi desconectado com sucesso.', 'info')
    return redirect(url_for('auth.login'))

def url_has_allowed_host_and_scheme(url, allowed_hosts=None, require_https=False):
    """Valida se a URL é segura para redirecionamento"""
    from urllib.parse import urlparse
    
    if allowed_hosts is None:
        allowed_hosts = []
    
    parsed = urlparse(url)
    
    if parsed.scheme and parsed.scheme not in ('http', 'https'):
        return False
    
    if parsed.netloc and parsed.netloc not in allowed_hosts:
        return False
    
    return True
