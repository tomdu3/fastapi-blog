# Use a specific and more secure version of the Python image.
FROM python:3.12.4-slim-bookworm

# Set environment variables to prevent caching and improve security.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install uv, pinning the version for reproducible builds.
COPY --from=ghcr.io/astral-sh/uv:0.2.29 /uv /uvx /bin/

# Create a non-root user and group.
RUN groupadd --system app && useradd --system --gid app app

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Change ownership of the app directory to the non-root user.
RUN chown -R app:app /app

# Switch to the non-root user.
USER app

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
