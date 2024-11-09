ARG PYTHON_IMAGE_TAG=3.11-slim

FROM python:${PYTHON_IMAGE_TAG}

# Set up Poetry to use an in-project virtual environment
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_PATH=/app/.venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy dependency files and install dependencies
COPY ["./pyproject.toml", "poetry.lock", "./"]
RUN poetry install

# Check installed packages for debugging
RUN ls /app/.venv/lib/python3.11/site-packages

# Copy application code
COPY ["./", "./"]
