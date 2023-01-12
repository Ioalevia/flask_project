FROM python:3.11

WORKDIR /app

RUN pip3 install -U pip

# poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN ln -s /root/.local/bin/poetry /usr/bin/poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --without=dev --no-root

# ~poetry

COPY wsgi.py wsgi.py

COPY blog ./blog

EXPOSE 5000

COPY entrypoint.sh .

ENTRYPOINT [ "./entrypoint.sh" ]