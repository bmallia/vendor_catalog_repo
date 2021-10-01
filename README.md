# guia de instalação e utilização

Esse arquivo de leia-me descreve o passo a passo de como instalar a aplicação.

## Feramentas para testes do serviço disponibilizado ##
Não é obrigatório mas os testes foram feitos com o programa chamado Postman

## Como subir o projeto? ##

As informações para subir o projeto será baseado em containers, esta documentação 
não cubrirá por enquanto sem a utilização do containers, ou seja, para começar o 
teste supomos que você já tenha o docker instalado.

* Configuração da base de dados
* Subindo containers
* Executando as migrations
* Verificando se container está no ar

### Adicionando novos usuário na base de dados ###
Para adicionar um novo usuário na basa de dados ou se for necessária a execução de qualquer comando DML ou DLL escreva elas no arquivo /scripts_container/init.sql

exemplo:
CREATE USER user;
CREATE DATABASE VENDOR_CATALOG;
GRANT ALL PRIVILEGES on DATABASE VENDOR_CATALOG TO user;

### Subindo containers ###
Para subir a composição de containers necessário apenas execute o seguinte comando na pasta raiz do seu projeto:

docker-compose up -d

### Executando migrações ###
Toda vez que o container do serviço subir irá fazer o migrate dos dados para serem 
aplicados no banco contudo se por algum motivo se fizer necessário executá-lo execute
o comando abaixo

docker-compose exec service python manage.py migrate --noinput


### Verificando se container está no ar ###
Para verificar se o serviço está no ar acesso a url: http://localhost:8000/


## FEATURES ##

### lista de features ###
* CRUD de produtos 
* CRUD de vendor
* Busca de vendedor por um ou múltiplos campos
* Busca de produtos por um ou múltiplos campos


## CRUD de produtos ##

### Criar produto ###
Para criar um produto utiliza-se o método POST seguindo a request JSON com o seguinte:
 
 {
    "name": "Product 2",
    "code": 14.45,
    "price": 17.42
}

utilize a seguinte url: http://localhost:8000/product/ 

## Pesquisando todos os produtos ###
Para trazer todos os produtos ou trazer um produto de um id específico acesse a url:
http://localhost:8000/product/<id>/ (exemplo: http://localhost:8000/product/1/ ou http://localhost:8000/product/ para trazer todos os produtos)

## Para atualizar um produto ###
Para atualizar um produto utilize o método PUT e o seguinte padrão de url:
http://localhost:8000/product/<id>/ (exemplo: http://localhost:8000/product/1/)


## Para deletar um produto ##
Para deletar um produto, utilize o método DELETE e o seguinte padrão de url:
http://localhost:8000/product/<id>/

## Para atualizar um produto ##
Para atualizar um produto, utilize o método PATCH e o seguinte padrão de url:
http://localhost:8000/product/<id>/

## Para criar um vendedor ###
Para criar um vendedor utilize o método POST com a seguinte padrão de url e de mensagem JSON de request

{
    
    "name": "vendedor 2",
    "cnpj": "49040268000146",
    "city": "São Paulo",
    "products": [
        {
            "name": "Produto 5",
            "code": "321",
            "price": "52.51"
        }
        
    ]
}

É importante salitentar que conforme a especificação para cada post de vendedor sempre será uma lista de produtos novos

## pesquisar vendodor por multiplos campos ##




