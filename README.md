

# FastAPI App with Docker
This repository contains a FastAPI app that performs feature engineering on data and provides an API endpoint for accessing the results. The app can be run using Docker, which provides an isolated environment for the application. 
The application consists of:

- Endpoints
   * (GET) /feature_engineering 
   * (POST) /feature_engineering 
   * (GET) /health
- Feature services
   * Logger
   * Unit Tests
   

## Prerequisites
Before running the app, ensure you have the following installed on your system:

- Docker - Install Docker according to your operating system.

## Getting Started
Follow the steps below to run the FastAPI app with Docker:

1. ### Clone the repository

       git clone https://github.com/Herc-Ch/ml_assignment.git\
   
   and
   
       cd ml_assignment
   
1. ### Build the Docker image

   Run the following command to build the Docker image for the FastAPI app:


       docker-compose build
    This will create a Docker image based on the Dockerfile in the repository.

1. ### Run the Docker container

    Use the following command to run the FastAPI app in a Docker container:


       docker-compose up
   
    This command will start the container and expose port 8000 on your host system, allowing you to access the app at http://localhost:8000.

1. ### Unit Tests

    To verify that the endpoints work correctly, run the following command:

       docker-compose exec app pytest .
    
    You should see the results on the console (2 passed).

1. ### Access the FastAPI app

    You can now access the FastAPI app through your browser or any API client (e.g., Postman or curl):


        http://localhost:8000/feature_engineering
   
   and
   
        http://localhost:8000/health
    The API endpoint /feature_engineering will return the feature-engineered data in JSON format and the health status respectively.

