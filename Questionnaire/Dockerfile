from python:latest

#  RUN apk add py3-pip

# RUN apk add --no-cache python3-dev \
# RUN  pip3 install --upgrade pip

WORKDIR /

COPY ./requirements.txt /requirements.txt


RUN pip3 install -r requirements.txt

COPY . /


Expose 5000

ENTRYPOINT ["python3"]
CMD ["app.py"] 