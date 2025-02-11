FROM python:3.10-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade -r /requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]