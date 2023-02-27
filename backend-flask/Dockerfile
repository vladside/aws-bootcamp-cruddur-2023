FROM python:3.10-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
RUN chmod +x start.sh

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD ["sh", "./start.sh"]
