# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container's working directory
COPY ./app /app
COPY ./cvas_data.json /app
COPY ./requirements.txt /app
# COPY ./app/test_main.py /app

# Install the required packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the API port
EXPOSE 8000

# Start the FastAPI app with Uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["ls", "/"]