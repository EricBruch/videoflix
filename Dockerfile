FROM python:3

WORKDIR /usr/src/api_videoflix

ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# WORKDIR /usr/src/api_videoflix/api_videoflix

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]