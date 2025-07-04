# FastAPI Test

FastAPI Learning Repo.

## Docker

To build the Docker image, run the following command:

```bash
docker build -t fastapi-test .
```

To run the Docker image, run the following command:

```bash
docker run -p 8000:8000 fastapi-test
```

You can then access the application at <http://localhost:8000>.


## Alembic

- To initialize alembic:
```sh
alembic init <migrations-name>
```

- to make migrations
```sh
alembic revision --autogenerate -m "message"
```

- to apply migrations
```sh
alembic upgrade head # for the most recent file generated 
```

## Fixtures

For the initial data population there's `fixtures.py` file. After database initialization, run

```sh
uv run fixtures.py
```

## FastAPI documentation

- [Official FastAPI documentation](https://fastapi.tiangolo.com/)
FastAPI project documentation is self generated from the source code. It can be found in two endpoinds:

1. <http://localhost:8000/docs> - [Swagger UI](https://swagger.io/tools/swagger-ui/) format
2. <http://localhost:8000/redoc> - [ReDoc format](https://github.com/Redocly/redoc)
3. [FastAPI - Complete Course for Python API Development](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQghmnb865lpdmYyWU3I5F1)
4. [Typing Module](https://docs.python.org/3.13/library/typing.html#typing.Annotated)
5. [How to use MaxLen of typing.Annotation](https://stackoverflow.com/questions/68454202/how-to-use-maxlen-of-typing-annotation-of-python-3-9)
6. [Alembic Integration With FAST-API](https://medium.com/@jamshidsadiqi25/alembic-integration-with-fast-api-fc992fb0e70b)
7. [Alembic - Documentation](https://alembic.sqlalchemy.org/en/latest/)