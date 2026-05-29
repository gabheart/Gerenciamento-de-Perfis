from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Página inicial"""
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard do usuário"""
    return render_template('dashboard.html', user=current_user)

@main_bp.route('/profile')
@login_required
def profile():
    """Perfil do usuário"""
    return render_template('profile.html', user=current_user)
