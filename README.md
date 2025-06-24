# FastAPI Blog

A simple blog application built with FastAPI.

## Docker

To build the Docker image, run the following command:

```bash
docker build -t fastapi-blog .
```

To run the Docker image, run the following command:

```bash
docker run -p 8000:8000 fastapi-blog
```

You can then access the application at <http://localhost:8000>.

## FastAPI documentation

- [Official FastAPI documentation](https://fastapi.tiangolo.com/)
FastAPI project documentation is self generated from the source code. It can be found in two endpoinds:

1. <http://localhost:8000/docs> - [Swagger UI](https://swagger.io/tools/swagger-ui/) format
2. <http://localhost:8000/redoc> - [ReDoc format](https://github.com/Redocly/redoc)
