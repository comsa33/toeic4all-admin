FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUTF8=1 \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -y

COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /bin/

RUN uv --version

WORKDIR /app

COPY pyproject.toml uv.lock /app/

COPY . .

RUN uv sync --frozen --no-cache

EXPOSE 8000

CMD ["uv", "run", "run_server.py"]
