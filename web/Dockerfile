FROM python:3.7-slim

RUN useradd --create-home myappuser
WORKDIR /home/myappuser
USER myappuser

ENV VIRTUAL_ENV=/home/myappuser/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY myapp myapp
COPY myapp/static /usr/src/app/static
COPY requirements.txt manage.py ./

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
