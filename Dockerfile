# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

#add ping utility
RUN apt-get update && apt-get install -y iputils-ping

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#copy run.py and requirements.txt
COPY run.py /app
COPY requirements.txt /app

# Upgrade pip
RUN pip install --upgrade pip

# 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "run.py"]
