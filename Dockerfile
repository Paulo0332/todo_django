# 1 - Choosing a base image
FROM python:3.12-slim

# 2 - Defining the directory which we'll use
WORKDIR /app

# 3 - Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#4 - Copy the rest of the project
COPY . /app/

# 5 - Default command
CMD [ "python","manage.py", "runserver", "0.0.0.0:8000"]