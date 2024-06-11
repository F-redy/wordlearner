FROM python:3-alpine AS builder
 
WORKDIR /code

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/code/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install

COPY . .
 
# Stage 2
FROM python:3-alpine AS runner
 
WORKDIR /code
 
COPY --from=builder /code/venv venv
COPY apps apps
 
ENV VIRTUAL_ENV=/code/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000
 
EXPOSE ${PORT}
 
CMD gunicorn --bind :${PORT} --workers 2 apps.wsgi