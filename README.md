# Gerenciamento de Perfis

Sistema Flask com autenticação de usuários e gerenciamento de perfis com controle de acesso por roles (admin, usuário comum, visitante).

## Funcionalidades

✅ **Autenticação de Usuários**
- Cadastro de novos usuários
- Login seguro com hash de senha (bcrypt)
- Logout
- Lembrar autenticação

✅ **Gerenciamento de Perfis**
- Visualizar perfil do usuário
- Dashboard personalizado
- Controle de acesso baseado em roles

✅ **Sistema de Administração**
- Dashboard do administrador
- Gerenciamento de usuários
- Estatísticas do sistema

✅ **Segurança**
- Proteção CSRF
- Senhas criptografadas com bcrypt
- Validação de formulários
- Controle de sessão

## Requisitos

- Python 3.8+
- MySQL 5.7+
- pip

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/gabheart/Gerenciamento-de-Perfis.git
cd Gerenciamento-de-Perfis
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

**Criar o banco de dados MySQL:**

```sql
CREATE DATABASE ger_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'ger_user'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL PRIVILEGES ON ger_db.* TO 'ger_user'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Inicializar o banco de dados

```bash
# Criar as tabelas
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Ou usar o comando customizado
python wsgi.py init-db
```

### 6. Popular o banco com dados de teste (opcional)

```bash
python wsgi.py seed-db
```

Credenciais de teste:
- **Admin:** admin / admin123
- **Usuário 1:** usuario1 / senha123
- **Usuário 2:** usuario2 / senha123

## Execução

### Modo desenvolvimento

```bash
flask run
```

Ou

```bash
python wsgi.py
```

A aplicação estará disponível em `http://localhost:5000`

### Modo produção

```bash
FLASK_ENV=production python wsgi.py
```

## Estrutura do Projeto

```
Gerenciamento-de-Perfis/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py              # Modelo de usuário
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py              # Rotas de autenticação
│   │   ├── main.py              # Rotas principais
│   │   └── admin.py             # Rotas de administração
│   ├── forms/
│   │   ├── __init__.py
│   │   └── auth.py              # Formulários de autenticação
│   ├── templates/
│   │   ├── base.html            # Template base
│   │   ├── index.html           # Página inicial
│   │   ├── dashboard.html       # Dashboard do usuário
│   │   ├── profile.html         # Perfil do usuário
│   │   ├── auth/
│   │   │   ├── login.html       # Página de login
│   │   │   └── register.html    # Página de cadastro
│   │   └── admin/
│   │       ├── dashboard.html   # Dashboard do admin
│   │       └── manage_users.html # Gerenciar usuários
│   └── __init__.py              # Inicialização da app
├── migrations/                   # Migrações do banco
├── wsgi.py                       # Entry point da aplicação
├── config.py                     # Configurações
├── requirements.txt              # Dependências do projeto
├── .gitignore                    # Arquivos ignorados pelo git
└── README.md                     # Este arquivo
```

## Rotas da Aplicação

### Públicas
- `GET /` - Página inicial
- `GET /auth/login` - Página de login
- `POST /auth/login` - Processar login
- `GET /auth/register` - Página de cadastro
- `POST /auth/register` - Processar cadastro

### Autenticadas (Usuário)
- `GET /dashboard` - Dashboard do usuário
- `GET /profile` - Perfil do usuário
- `GET /auth/logout` - Logout

### Administrador
- `GET /admin/` - Dashboard do administrador
- `GET /admin/users` - Gerenciar usuários

## Modelos de Dados

### User
- `id` - ID único
- `username` - Nome de usuário único
- `email` - Email único
- `password_hash` - Senha criptografada
- `full_name` - Nome completo
- `role` - Papel do usuário (admin, user)
- `is_active` - Status da conta
- `created_at` - Data de criação
- `updated_at` - Data de atualização
- `last_login` - Último acesso

## Comandos Úteis

```bash
# Criar usuário administrador
python wsgi.py create-admin

# Inicializar banco de dados
python wsgi.py init-db

# Popular banco com dados de teste
python wsgi.py seed-db

# Shell do Flask
flask shell

# Migrações do banco
flask db init
flask db migrate -m "Descrição da mudança"
flask db upgrade
```

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
FLASK_ENV=development
FLASK_APP=wsgi.py
DATABASE_URL=mysql://ger_user:pass123@localhost/ger_db
```

## Problemas Comuns

### Erro: "No module named 'MySQLdb'"

Instale o conector MySQL:

```bash
pip install mysqlclient
```

Ou use:

```bash
pip install PyMySQL
```

E altere a string de conexão em `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ger_user:pass123@localhost/ger_db'
```

### Erro: "Access denied for user 'ger_user'@'localhost'"

Verifique se o banco de dados e usuário foram criados corretamente e se a senha está correta em `config.py`.

## Próximas Melhorias

- [ ] Editar perfil do usuário
- [ ] Alterar senha
- [ ] Recuperação de senha
- [ ] Confirmação de email
- [ ] Autenticação de dois fatores (2FA)
- [ ] API REST
- [ ] Testes unitários
- [ ] Documentação Swagger

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Criado por [gabheart](https://github.com/gabheart)
