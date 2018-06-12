FROM python:2.7
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY main.py /app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
