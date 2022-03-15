FROM python:3.9.2
COPY . /./

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
