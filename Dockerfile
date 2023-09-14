FROM python:3.9-slim

RUN apt-get update && apt-get install -y libncurses5

WORKDIR /stoplight

COPY stoplight /stoplight

CMD ["python3", "/stoplight/stoplight.py"]
