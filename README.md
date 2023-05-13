# [DuckORM CLI](https://pypi.org/project/duck-orm-cli/)

DuckORM CLI is a database migration tool for usage with the [DuckORM](https://github.com/richecr/duck-orm).

**Requirements**: Python 3.10+

**Duck-ORM-CLI is still in the early stages of development, production use is not recommended**.

## Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-3107/)
- [Poetry](https://python-poetry.org/)
- [Typer](https://typer.tiangolo.com/)
- [Docker](https://www.docker.com/)

## Table of Contents

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Quickstart](#quickstart)
    - [Commands](#commands)
        - [init](#init)
        - [create-migrate](#create-migrate)
        - [create-seed](#create-seed)
        - [run-migrations](#run-migrations)
        - [undo-migrations-all](#undo-migrations-all)
        - [create-seed](#create-seed)
- [Author](#author)
- [License](#license)

## Installation

```bash
$ pip install duck-orm-cli
```

!!! note
    Don't forget to install `databases` before installing `duck-orm-cli`. 

## Quickstart

For this example we will create a connection to the SQLite database and create a model.

```bash
$ pip install databases[sqlite]
$ pip install ipython
```

Note that we want to use `ipython` here, because it supports using await expressions directly from the console.

### Commands

#### init

The command to create the initial settings for migrations.

- Example

```sh
duck-orm-cli init
```

This command will create the `duckorm_file.py` file with the structure below:

```python
configs = {
    "development": {
        "client": "postgresql", # dialect (or sqlite)
        "database_url": "url", # uri (dev-duckorm:postgres123@localhost:5432/dev-duckorm)
    },
    "production": {
        "client": "postgresql", # dialect (or sqlite)
        "database_url": "url", # uri: dev-duckorm:postgres123@localhost:5432/dev-duckorm
    },
}
```

Here is where you must correctly configure the connection to your database.

`OBS`: This command also creates the `migrations` and `seeds` folders.


#### create-migrate <name>

The command to create a database migration.

- Example

```sh
duck-orm-cli create-migrate create_users
```

The file with `<timestamp>_create_users.py` will be created with the structure:

```python
from duck_orm.sql import fields as Field
from duck_orm.model_manager import ModelManager


async def up(model_manager: ModelManager):
    await model_manager.create_table('users', {
        'id': Field.Integer(primary_key=True, auto_increment=True),
        'name': Field.String(),
        'email': Field.String(unique=True)
    })


async def down(model_manager: ModelManager):
    await model_manager.drop_table('users')
```

With the `up` and `down` methods. Where it is possible to describe what that migration will do and how the migration will be undone.


#### create-seed <name>

The command to create a seed in your database.

- Example

```sh
duck-orm-cli create-seed insert_user_admin
```

The file with `<timestamp>_insert_user_admin.py` will be created with the structure:

```python
from duck_orm.model_manager import ModelManager
from duck_orm.sql.condition import Condition


def up(model_manager: ModelManager):
    return model_manager.insert(
        "users", [{"id": 1, "name": "User 1", "email": "user1@gmail.com"}]
    )


def down(model_manager: ModelManager):
    return model_manager.remove("users", conditions=[Condition("id", "=", 1)])
```

With the `up` and `down` methods. Where it is possible to describe what that seed will do and how the seed will be undone.


#### run-migrations

The command to perform all migrations on the database.

- Example

```sh
duck-orm-cli run-migrations
```

This command will take each created migration and run the `up` method and apply it to your database.

#### undo-migrations-all

The command to undo all applied migrations on the database.

- Example

```sh
duck-orm-cli undo-migrations-all
```

This command will take each performed migration and run the `down` method and undo the change in your database.


## Author

- Rich Ramalho - [@richecr](https://github.com/richecr) - [@richzinho_ecr](https://twitter.com/richzinho_ecr)

## License

`Duck ORM CLI` is built as an open-source tool and remains completely free (MIT license).
