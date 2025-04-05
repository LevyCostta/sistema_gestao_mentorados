# Sistema de Gestão de Mentorados

Este é um projeto desenvolvido durante a Pystack Week 13, promovido pela Pythonando. O objetivo deste sistema é facilitar a gestão de mentorados, permitindo que mentores e mentorados se conectem, gerenciem suas interações e acompanhem o progresso.

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML/CSS
- JavaScript 

## Funcionalidades

- Cadastro de mentores e mentorados
- Sistema de login e autenticação
- Criação e gerenciamento de sessões de mentoria
- Acompanhamento de progresso dos mentorados
- Sistema de feedback

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Django

## Instalação

1. Clone o repositório:
   
   git clone https://github.com/seuusuario/sistema-gestao-mentorados.git
   cd sistema-gestao-mentorados
   
2. Crie um ambiente virtual (opcional, mas recomendado):

  python -m venv venv
  source venv/bin/activate  # Para Linux/Mac
  venv\Scripts\activate  # Para Windows

3. Instale as dependências:

  pip install -r requirements.txt

4. Execute as migrações do banco de dados:

  python manage.py migrate

5. Crie um superusuário (opcional, para acessar o admin):
   
  python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento:

  python manage.py runserver

7. Acesse o sistema em:

  http://127.0.0.1:8000/

#Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga estas etapas:

Fork este repositório.
Crie uma nova branch (git checkout -b feature/nome-da-sua-feature).
Faça suas alterações e commit (git commit -m 'Adiciona nova funcionalidade').
Envie para o repositório remoto (git push origin feature/nome-da-sua-feature).
Abra um Pull Request.

#Agradecimentos

Agradeço à Pythonando e a todos os participantes da Pystack Week 13 pela inspiração e suporte durante o desenvolvimento deste projeto.
