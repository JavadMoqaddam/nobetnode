FROM python:3.12-slim

RUN apt update && \
    apt install -y iptables iproute2 ipset && \
    apt clean

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["python"]

CMD ["nobetnode.py"]