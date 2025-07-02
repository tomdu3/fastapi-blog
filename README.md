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

## FastAPI documentation

- [Official FastAPI documentation](https://fastapi.tiangolo.com/)
FastAPI project documentation is self generated from the source code. It can be found in two endpoinds:

1. <http://localhost:8000/docs> - [Swagger UI](https://swagger.io/tools/swagger-ui/) format
2. <http://localhost:8000/redoc> - [ReDoc format](https://github.com/Redocly/redoc)
3. [FastAPI - Complete Course for Python API Development](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQghmnb865lpdmYyWU3I5F1)
4. [Typing Module](https://docs.python.org/3.13/library/typing.html#typing.Annotated)

