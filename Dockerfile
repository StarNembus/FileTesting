FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /./

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
