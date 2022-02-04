FROM python:3.7.4-stretch

WORKDIR /home/web

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

# CMD ["python", "./app/flask-server.py"]

# WORKDIR /app
# RUN chmod +x gunicorn.sh
# ENTRYPOINT ["./gunicorn.sh"]

ENV GIT_HEAD="cdefgab"
ENV MAINTAINER="XW"
ENV SUBMISSION_DATE="01/31/2022"