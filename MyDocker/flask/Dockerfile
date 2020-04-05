# Step 1: Import the Os
from alpine:latest

# Step 2: Install pip and Python Dependencies
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Step 3: Create a Work Directory
WORKDIR /app

# Step 4: copy all Project Files
COPY . /app

# Step 5: Install all Dependencies for WSGI
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip3 --no-cache-dir install -r requirements.txt; \
	apk del .build-deps;

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]