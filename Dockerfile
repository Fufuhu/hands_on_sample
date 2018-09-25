FROM python:3.6.6-alpine3.6

COPY sampleapp /sampleapp
WORKDIR /sampleapp
RUN apk update && apk add gcc libffi-dev libc-dev openssl-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]