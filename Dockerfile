# Use a Python base image
FROM python:3.12 as build
 
# Set the working directory in the container
WORKDIR /app

# Copy the poetry files into the container
COPY pyproject.toml poetry.lock /app/

# Copy the source code into the container
COPY src /app/src

# Install Poetry to manage the dependencies
RUN pip install poetry

# Export the dependencies from Poetry to a requirements.txt file
RUN poetry export -f requirements.txt > requirements.txt

# Install the dependencies using the requirements.txt file
RUN pip install -r requirements.txt

# Expose the port that your API is listening on (adjust if necessary)
EXPOSE 5000

# Command to run your application
CMD ["python", "-m", "src.api.server", "--host", "0.0.0.0", "--port", "5000"]
