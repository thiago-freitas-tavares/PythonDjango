# Website com Python e o Framework Django

- framework é uma biblioteca de módulos reutilizáveis, que fornecem funcionalidades para atividades comuns.
- framework define a estrutura das aplicações (padronização da estrutura dos códigos).

- Ambiente Virtual com o Django instalado evita a sua instalação num ambiente Python global.
- o que proporciona controle sobre as bibliotecas utilizadas no app e facilita a criação de um arquivo requirements.txt para o ambiente.

# Criando Ambiente Virtual e Projeto

01. Windows Command Prompt: `cd C:\Users\Xis\OneDrive\Documentos\VSCodeProjects\PythonDjango` (referencia a pasta do projeto).
02. Windows Command Prompt: `py -3 -m venv venv` (cria um ambiente virtual chamado venv).
manage.py criado na raiz + pasta venv com Include, Lib\site-packages, Scripts, pyvenv.cfg.
03. Windows Command Prompt: `C:\Users\Xis\OneDrive\Documentos\VSCodeProjects\PythonDjango\venv\scripts\activate` (ativa o ambiente virtual criado).
04. VS Code: View -> Command Palette ou `Ctrl+Shift+P` -> seleciona o virtual environment na pasta do projeto que começa com .\venv\.
05. VS Code: ao abrir um novo terminal Command Prompt ou Bash, o ambiente virtual é automaticamente ativado (venv no temrinal).
06. VS Code Command Prompt: `python -m pip install` --upgrade pip (atualiza o pip no ambiente virtual).
07. VS Code Command Prompt: `python -m pip install django` (instala o Django no ambiente virtual).
08. VS Code Command Prompt: `django-admin startproject pyshop .` (startproject cria a pasta pyshop - nome do projeto - e o . indica na pasta atual).
pasta pyshop criada com __init__.py, asgi.py (Asynchronous Server Gateway Interface), settings.py, urls.py (Uniform Resourse Locator), wsgi.py (Web Server Gateway Interface).
09. VS Code Command Prompt: `python manage.py migrate` (cria um banco de dados SQLite vazio).
10. VS Code Command Prompt: `python manage.py runserver` (após criado o projeto, utilizamos manage.py ao invés de django-admin).
este comando retorna o link do website do projeto Django criado na porta padrão 8000 (python manage.py runserver 5000 - troca a porta).
11. VS Code Command Prompt: `python manage.py startapp products` cria o app products para gerenciar os produtos.
pasta products criada com __init__.py, admin.py, apps.py, models.py, tests.py, views.py (pacote que pode ser utilizado em outro projeto Django).

# Pastas Criadas

# venv

- ambiente virtual.

# pyshop

- `__init__.py`: indica pacote Python.
- `settings.py`: configurações do projeto.
- `urls.py`: tabela com conteúdo para o projeto.
- `wsgi.py` e `asgi.py`: são módulos reponsáveis pela conexão do app com os servidores de produção.

# products

- `__init__py`: indica pacote Python.
- `admin.py`: criar interface de administrador.
- `apps.py`: configurações do app.
- `models.py`: contém as classes que definem os objetos do app.
- `tests.py`: criar testes automatizados.
- `views.py`: contém as funções que definem as páginas do app.
  # migrations
  - utilidade administrativa para o Django gerenciar as versões do banco de dados.

# Desenvolvimento do Website Django

- dividimos o projeto Django em múltiplos apps Django. Cada App foca em uma área funcional.
- ao tentarmos acessar um URL diferente da main page, o navegador envia um HttpRequest para um Servidor Web.
- o Django analisa o URL do pedido e envia para a função view, responsável por enviar o retorno (HTML) para o navegador ou client, que exibe o HTML como página.

01. `products\views.py`: cria a primeira função view chamada index (por convenção a página principal do app).
02. para linkar a função index ao URL da página principal do app -> botão direito na pasta `products` -> `New` -> Python File chamado `urls.py`.
03. `products\urls.py`: definir variável chamada urlpatterns (convenção), que neste caso é uma lista onde linkamos as URLs e suas respectivas funções view, através do módulo path.
04. `pyshop\urls.py`: já possui a variável urlpatterns -> incluímos um objeto path para delegar qqr URL começando com products/ para o app products.
05. para visualizar o que foi feito até agora -> lembrar de ativar o ambiente virtual em caso de reinicialização:
06. Windows Command Prompt: `C:\Users\Xis\OneDrive\Documentos\VSCodeProjects\PythonDjango\venv\scripts\activate`.
07. VS Code Command Prompt: `python manage.py runserver` -> Testar: 127.0.0.1.8000/products.

- se tentarmos acessar a página inicial ocorrerá um erro, pois assim que criamos um novo urlpatterns, a págiona inicial, que foi automaticamente gerada na criação do projeto, desaparece.

# Criando uma Página 127.0.0.1.8000/products/new para Exibir 'New Products'.

01. `products\views.py`: cria a função view chamada new.
02. `products\urls.py`: mapeia o final da URL new/ com a função view new.
03. VS Code Command Prompt: `python manage.py runserver` -> Testar: 127.0.0.1.8000/products/new.

# Criando um Modelo

- um modelo é a representação de um conceito do mundo real, por exemplo, modelos da OnlineMusicShop: order, customer, shopping cart, product review.

01. `products\models.py`: cria uma classe chamada Product, herdando todas as funções da classe Model, e define os atributos dos produtos (id não é obrigatório, pois o Django gera automaticamente).

- db.sqlite3 é o arquivo de banco de dados SQLite vazio que criamos com o comando `python manage.py migrate` anteriormente.
- o SQLite atende às necessidades de pequenas aplicações, mas não às de grandes aplicações empresariais. Para aplicações mais robustas, o ideal é a utilização de SGBDRs (`Sistema de Gestão de Banco de Dados Relacional` - armazena dados em linhas e colunas), como Oracle Database, MySQL, SQL Server, PostgreSQL ou IBM DB2.
- é possível criar tabelas manualmente através do `DB Browser for SQLite` (Google -> DB Browser for SQLite -> Downloads), porém, também é possível criá-las automaticamente através do modelo Django desenvolvido.

02. VS Code Command Prompt: `python manage.py makemigrations` -> No changes Detected (Django ainda nao foi informado sobre a existência do modelo Product).
03. `pyshop\settings.py`: o projeto Django vem com apps criados automaticamente (admin, auth, contenttypes, sessions, messages, staticfiles), mas o app products que criamos não está na lista INSTALLED_APPS.
04. `products\apps.py`: a classe ProductsConfig armazena definições de configuração para este app (products) específico.
05. `pyshop\settings.py`: inserimos em INSTALLED_APPS o caminho completo de ProductsConfig -> 'products.apps.ProductsConfig'.
06. VS Code Command Prompt: `python manage.py makemigrations` -> Migrations for 'products' -> cria o módulo 0001_initial.py em products\migrations.
07. `products\migrations\0001_initial.py`: o primeiro item da lista operations é a classe migrations.CreateModel, que cria uma tabela chamada Product no DB com os campos que criamos em `products\models.py`.
08. VS Code Command Prompt: `python manage.py migrate` cria uma tabela para cada migration (admin, auth, contenttypes, products, sessions). Cada migration adiciona nova tabela ou modifica tabela existente no DB.

- se abrirmos o arquivo db.sqlite3 deste projeto no DB Browser SQLite teremos 12 tabelas (uma delas products_product -> id, name, price, stock, image_url).
- para criar um novo modelo (especificando atributos) ou atualizar um modelo existente, executamos 2 comandos:
`python manage.py makemigrations`: cria uma migração baseada nas alterações realizadas no código.
`python manage.py migrate`: roda as migrações pendentes.

# Criando Novo Modelo (tabela) Chamado Offer

01. `products\models.py`: cria uma classe chamada Offer, herdando todas as funções da classe Model, e define seus atributos (salvar).
02. VS Code Command Prompt: `python manage.py makemigrations` -> Migrations for 'products' -> cria o módulo 0002_offer.py em products\migrations.
03. VS Code Command Prompt: `python manage.py migrate` cria uma tabela offer.

- se abrirmos o arquivo db.sqlite3 deste projeto no DB Browser SQLite veremos a tabela products_offer -> id, code, description, discount.

# Painel Administrativo das Aplicações Django (gerado automaticamente)

- VS Code Command Prompt: `python manage.py runserver` -> Testar: 127.0.0.1.8000/admin.

01. VS Code Command Prompt: `python manage.py createsuperuser` cria o primeiro usuário da aplicação (super usuário). Comando solicita Username, Email address e Password (neste projeto utilizei admin - 1234).

- com isso, conseguimos logar no Site Administration do Django e administrar as tabelas de autenticação e autorização, bem como as tabelas criadas no app.

02. `products\admin.py`: importamos nosso modelo Product (from products.models.py), depois o registramos no admin site para que possamos gerenciar os produtos na área do admin (salvar e atualizar página no 127.0.0.1.8000/admin).
03. `127.0.0.1.8000/admin`: clica em Products -> Add -> inclui Name, Price, Stock e Image url (link da imagem na internet).
04. `products\admin.py`: para customizar a tabela Products no 127.0.0.1.8000/admin criamos uma classe ProductAdmin, que herda as funções da classe ModelAdmin -> incluímos esta classe como segundo argumento do admin.site.register. (salvar e atualizar página no 127.0.0.1.8000/admin). Repete 02 e 04 para a tabela Offer.
05. `127.0.0.1.8000/admin`: clica em Offer -> Add -> inclui Code e Discount.

# Exibir Lista de Produtos na Página Inicial

01. `products\views.py`: importamos a classe Product definida em products\models.py e utilizamos o método objects.all para recuperar todos os dados da tabela do DB.

- agora precisamos formatar estes dados em um template HTML para apresentar a lista de produtos para o usuário.

02. `products`: Botão Direito + New + Directory (chamado templates por convenção).
03. `products\templates`: Botão Direito + New + File (index.html).
04. `products\templates\index.html`: cria uma lista com os produtos e preços.
ctrl+shift+P -> Change Language Mode -> HTML (caso atalhos não estejam funcionando)
05. `products\views.py`: na função view index, ao invés do Hello World, retornar o index.html ao browser ou client através da função render (renderizar template).
06. `getbootstrap.com`: Docs -> Quick Start 2 -> copy code (código CSS e JavaScript pronto para produção via CDN).
CDN (Content Delivery Network) é uma maneira de enviar conteúdo massivo para usuários sem ter problemas com desempenho.
07. `products\templates`: Botão Direito + New + File (base.html) -> paste code. (template básico com formatações para todas as páginas da nossa aplicação).
08. `templates\base.html`: o conteúdo de <body> tag é o que o usuário visualiza na página. substituímos o <h1> tag Hello, world! por um template tag com um bloco chamado content.
09. `templates\index.html`: utilizamos o template tag extends para estendermos o template base.html e podermos utilizar suas formatações definidas. além disso, o block content do template base.html será preenchido com o código definido aqui.
10. `getbootstrap.com`: Docs -> Components (Card) -> Example HTML -> copy code.
11. `templates\index.html`: substituiremos <ul> e <li> por <div> para exibirmos os produtos em cards com imagens ao invés de bullet points.
- entre <h1> e <ul> inserir (div.row + TAB), que cria uma classe chamada row (linha). dentro deste <div> inserir (div.col + TAB), que cria uma classe chamada col (coluna). dentro de ambos <div> (row e col) -> paste code.
- entre <div row> e <div col> inserir o template tag for, pois para cada linha queremos renderizar um produto por coluna em um card.
- dentro do <div card> temos <img src> sem atributo -> incluimos o image.url de cada produto.
- dentro do <div card-body> temos <h5 card-title> -> substituimos Card title pelo nome de cada produto.
- dentro do <div card-body> temos <p card-text> -> substituimos o texto pelo preço de cada produto.
- dentro do <div card-body> temos <a btn btn-primary> -> substituimos o nome do botão para Add to Cart.
12. `getbootstrap.com`: Docs -> Components (Navbar) -> Brand Text HTML -> copy apenas o código (As a link), para incluir uma barra de navegação no projeto.
13. `templates\base.html`: colamos o código <nav> dentro da <head> tag do base.html, para que esta configuração seja aplicada a todas as páginas do projeto e alteramos o nome na barra de navegação <a navbar-brand> para PyShop.
14. o arquivo base.html encontra-se dentro de `products\templates`, porém, por possuir as configurações básicas para todas as páginas do projeto, devemos tirá-lo do app products e mover para um diretório template na raiz (root) do projeto.
15. `PYTHONDJANGO` (project root): Botão Direito + New + Directory (templates) -> mover base.html para este diretório através de drag and drop.
com essa modificação, o Django não consegue encontrar o template base.html, pois ele procura apenas dentro dos apps instalados. para resolver isto, temos que pedir para ele pesquisar também na pasta templates (que até o momento é somente uma pasta).
16. `pyshop\settings.py`: adicionar templates ao BASE_DIR (variável que aponta pro caminho completo em que este projeto Django está armazenado no HD).
TEMPLATES 'DIRS': referenciar o diretório templates do projeto através do método join do objeto path do módulo os. Acrescentamos 'templates' no BASE_DIR.
17. `templates\base.html`: movemos o block content para dentro de um (div.container + Tab) para espaçar os itens uniformemente.
