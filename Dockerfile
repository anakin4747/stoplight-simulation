FROM python:3.9

WORKDIR /stoplight

COPY Makefile /stoplight

COPY stoplight /stoplight

CMD ["make"]
