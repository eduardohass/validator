# Validador de Script SQL

## Descrição

___
Script responsável por realizar a validação de regras nos scripts SQL Server.

<br />
<br />
<br />

## Referências
___
<br />
<br />
<br />

## Regras vigentes
___
<br />
<br />
<br />

### Recursos utilizados
___
frontend construído com Bulma - https://bulma.io/documentation/

<br />
<br />
<br />


### Setup
___


Necessário realizar a configuração das variáveis de ambiente que estão localiadas no arquivo ```docker-compose.yml```

``` bash
export FLASK_DEBUG=true
export FLASK_ENV=development
export DB_DATABASE_URI="mongodb://root:rootpassword@mongo:27017"
export DB_DATABASE_NAME="db_validator"
export SECRET_KEY=key
export MONGO_INITDB_ROOT_USERNAME="root"
export MONGO_INITDB_ROOT_PASSWORD="rootpassword"
```

