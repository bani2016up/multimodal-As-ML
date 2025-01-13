# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN apt-get upgrade
# Install poetry
RUN pip install poetry
RUN poetry lock
# Install project dependencies
RUN poetry install


EXPOSE 8000

# Run the application when the container launches
CMD ["poetry", "run", "python", "-m", "lumina"]
