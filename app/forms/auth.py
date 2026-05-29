from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models.user import User

class RegisterForm(FlaskForm):
    """Formulário de cadastro de usuário"""
    username = StringField(
        'Usuário',
        validators=[
            DataRequired(message='O nome de usuário é obrigatório.'),
            Length(min=3, max=80, message='O nome de usuário deve ter entre 3 e 80 caracteres.')
        ],
        render_kw={"placeholder": "Digite seu nome de usuário", "class": "form-control"}
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='O email é obrigatório.'),
            Email(message='Email inválido.')
        ],
        render_kw={"placeholder": "seu.email@example.com", "class": "form-control"}
    )
    
    full_name = StringField(
        'Nome Completo',
        validators=[Length(max=120, message='O nome completo deve ter no máximo 120 caracteres.')],
        render_kw={"placeholder": "Seu nome completo (opcional)", "class": "form-control"}
    )
    
    password = PasswordField(
        'Senha',
        validators=[
            DataRequired(message='A senha é obrigatória.'),
            Length(min=6, message='A senha deve ter no mínimo 6 caracteres.')
        ],
        render_kw={"placeholder": "Digite uma senha segura", "class": "form-control"}
    )
    
    password_confirm = PasswordField(
        'Confirmar Senha',
        validators=[
            DataRequired(message='A confirmação de senha é obrigatória.'),
            EqualTo('password', message='As senhas não correspondem.')
        ],
        render_kw={"placeholder": "Confirme sua senha", "class": "form-control"}
    )
    
    submit = SubmitField('Cadastrar', render_kw={"class": "btn btn-primary w-100"})
    
    def validate_username(self, field):
        """Valida se o nome de usuário já existe"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Este nome de usuário já está em uso.')
    
    def validate_email(self, field):
        """Valida se o email já existe"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Este email já está registrado.')

class LoginForm(FlaskForm):
    """Formulário de login"""
    username = StringField(
        'Usuário',
        validators=[DataRequired(message='O nome de usuário é obrigatório.')],
        render_kw={"placeholder": "Digite seu nome de usuário", "class": "form-control"}
    )
    
    password = PasswordField(
        'Senha',
        validators=[DataRequired(message='A senha é obrigat��ria.')],
        render_kw={"placeholder": "Digite sua senha", "class": "form-control"}
    )
    
    remember = BooleanField(
        'Lembrar-me',
        render_kw={"class": "form-check-input"}
    )
    
    submit = SubmitField('Login', render_kw={"class": "btn btn-primary w-100"})
