"""WSGI entry point para a aplicação Flask"""
import os
from app import create_app, db
from app.models import User

config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

@app.shell_context_processor
def make_shell_context():
    """Contexto para o shell do Flask"""
    return {'db': db, 'User': User}

@app.cli.command()
def init_db():
    """Inicializa o banco de dados"""
    db.create_all()
    print('✓ Banco de dados inicializado com sucesso!')

@app.cli.command()
def create_admin():
    """Cria um usuário administrador"""
    username = input('Digite o nome de usuário: ')
    email = input('Digite o email: ')
    password = input('Digite a senha: ')
    
    if User.query.filter_by(username=username).first():
        print('✗ Este usuário já existe!')
        return
    
    admin = User(
        username=username,
        email=email,
        password_hash=User.set_password(password),
        role='admin',
        is_active=True
    )
    db.session.add(admin)
    db.session.commit()
    print(f'✓ Usuário administrador "{username}" criado com sucesso!')

@app.cli.command()
def seed_db():
    """Popula o banco com dados de teste"""
    if User.query.count() > 0:
        print('✗ Banco de dados já contém usuários!')
        return
    
    users = [
        User(
            username='admin',
            email='admin@example.com',
            full_name='Administrador',
            password_hash=User.set_password('admin123'),
            role='admin',
            is_active=True
        ),
        User(
            username='usuario1',
            email='usuario1@example.com',
            full_name='Usuário Um',
            password_hash=User.set_password('senha123'),
            role='user',
            is_active=True
        ),
        User(
            username='usuario2',
            email='usuario2@example.com',
            full_name='Usuário Dois',
            password_hash=User.set_password('senha123'),
            role='user',
            is_active=True
        ),
    ]
    
    for user in users:
        db.session.add(user)
    
    db.session.commit()
    print('✓ Banco de dados populado com dados de teste!')
    print('  - Admin: admin / admin123')
    print('  - Usuário 1: usuario1 / senha123')
    print('  - Usuário 2: usuario2 / senha123')

if __name__ == '__main__':
    app.run()
