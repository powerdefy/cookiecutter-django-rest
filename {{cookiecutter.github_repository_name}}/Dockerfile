FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Change Timezone to GMT+7
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install additional packages
RUN apt update
RUN apt install -y gettext

# Location of source code
ENV PROJECT_ROOT /opt/app
RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

# Copying requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copying manage.py file
COPY ./manage.py .

# Copying flake8/coverage config file
COPY ./.flake8 .
COPY ./.coveragerc .

# Copying static file
COPY ./static ./static

# Copying source files
COPY ./{{cookiecutter.app_name}} ./{{cookiecutter.app_name}}