FROM python:3.6
LABEL maintainer="andrew.freyer@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8089
ENTRYPOINT ["python"]
CMD ["app/app.py"]
