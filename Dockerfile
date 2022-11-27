FROM python:3.10 as builder

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./app/req.txt .
RUN pip3 install -r req.txt

EXPOSE 8000
WORKDIR ./app
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]