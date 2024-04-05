FROM python:3.11-slim-buster
ENV PIP_TIMEOUT=1000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8888
CMD ["python", "finalscript.py"]