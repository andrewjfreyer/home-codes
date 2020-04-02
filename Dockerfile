FROM python:3.6
LABEL maintainer="andrew.freyer@gmail.com"
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 8089
ENTRYPOINT ["python"]
CMD ["app.py"]
