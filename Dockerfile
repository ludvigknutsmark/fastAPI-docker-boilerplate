FROM python:3.8-alpine

RUN apk update
RUN apk --update add ucspi-tcp
RUN apk --update add alpine-sdk && apk add libffi-dev openssl-dev

WORKDIR /usr/src/app

COPY src/requirements.txt .
RUN pip install -qr requirements.txt
COPY src/ .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]