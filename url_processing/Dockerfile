FROM tiangolo/uwsgi-nginx-flask:python3.6

# Copy req file
COPY requirements.txt /tmp/

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
COPY ./global_config/nginx.conf /etc/nginx/nginx.conf

ENV PROCESSING_PORT "80"
