FROM python:3-slim-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:./src"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host=0.0.0.0", "--port=8000"]
