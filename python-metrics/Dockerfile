FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir prometheus_client

COPY ./client.py .

CMD [ "python", "./client.py" ]
# CMD [ "python", "-m", "http.server"]
# python -m http.server --directory /tmp/