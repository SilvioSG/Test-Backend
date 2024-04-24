# Test Backend Project

### Este é um projeto Django que implementa uma API RESTful para gerenciar usuários.
### A API permite operações CRUD (Criar, Ler, Atualizar, Deletar) em usuários.

## Instalação

### Para instalar e executar este projeto, você precisa ter Python e Django instalados em seu ambiente. Siga os passos abaixo:

``` bash
1. Clone o repositório:
    $ git clone https://github.com/SilvioSG/Test-Backend

2. Instale as dependências:
    $ pip install -r requirements.txt

3. Execute as migrações:
    $ python manage.py migrate

4. Inicie o servidor: 
    $ python manage.py runserver
```


## Uso
A API fornece os seguintes endpoints:

- `get_all_users` : Retorna uma lista de todos os usuários.

- `get_user_by_name` : Retorna um usuário específico pelo nome.

- `create_user` : Cria um novo usuário.

- `update_user` : Atualiza um usuário existente.

- `delete_user` : Deleta um usuário existente.

## Testes
Este projeto inclui testes unitários que verificam a funcionalidade dos endpoints da API. Para executar os testes, use o seguinte comando:

```
python manage.py test
```

## Contribuição
Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
