FROM python:3.9-alpine

WORKDIR /code

EXPOSE 5000
ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["flask", "run"]
