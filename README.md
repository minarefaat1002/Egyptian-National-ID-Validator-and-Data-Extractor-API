# 🛂 Egyptian National ID Validator and Data-Extractor API 🛂
This project is a backend service that validates Egyptian national IDs and extracts relevant 
information such as birth date, governorate, and gender. The API is built using FastAPI and PostgreSQL,
and it is containerized using Docker Compose. The project includes features like rate limiting, API key
authentication, and request tracking.
# 🚀 Features
✅ National ID Validation: Validates the Egyptian national ID based on its structure and checksum.
   - 📂 Data Extraction: Extracts the following information from a valid national ID:
   - 🎂 Birth date (year, month, day)
   - 🏙️ Governorate
   - 👫 Gender
⏳ Rate Limiting: Limits the number of requests a service can make to the api within a specified time frame.
🔑 API Key Authentication: Ensures that only authenticated services can access the API.
📝 Request Tracking: Logs all API requests for tracking purposes.

# 🛠️ Technologies Used
## 1. FastAPI 🚀
used to build the API endpoints for validating and extracting data from national IDs.
Why it was chosen: FastAPI is known for its speed, ease of use, and automatic generation
of OpenAPI documentation. It also supports asynchronous programming, making it highly efficient 
for handling multiple requests.

## 2. PostgreSQL 🐘
Why it was chosen: PostgreSQL is highly reliable, supports advanced data types, and has 
robust performance for handling complex queries.

## 3. Docker 🐳
What it does: Docker is a platform for developing, shipping, and running applications in
containers. It ensures that the application runs consistently across different environments.
Why it was chosen: Docker simplifies the deployment process by packaging the application and 
its dependencies into a single container, ensuring consistency and reducing "it works on my machine" issues.

## 4. Docker Compose 🐙
What it does: Docker Compose is a tool for defining and running multi-container Docker applications. 
It is used to orchestrate the FastAPI application and PostgreSQL database.
Why it was chosen: Docker Compose makes it easy to manage multiple services (e.g., the API and the database) 
with a single configuration file, simplifying development and deployment.

## 5. SQLAlchemy 🔗
What it does: SQLAlchemy is an ORM (Object-Relational Mapping) tool for Python.
It is used to interact with the PostgreSQL database in a Pythonic way.
Why it was chosen: SQLAlchemy provides a high-level abstraction for database operations,
making it easier to work with databases without writing raw SQL queries.

## 6. Pydantic 📜
What it does: Pydantic is a data validation and settings management library.
It is used to validate request and response data in the FastAPI application.

Why it was chosen: Pydantic integrates seamlessly with FastAPI, providing automatic data validation
and serialization, which reduces boilerplate code and improves reliability.

## 7. SlowAPI 🐌
What it does: SlowAPI is a rate-limiting library for FastAPI. It is used to limit the number of
requests a user can make within a specified time frame.
Why it was chosen: SlowAPI is lightweight, easy to integrate with FastAPI, and provides a simple 
way to implement rate limiting without requiring additional infrastructure like Redis.


## 🚀 Getting Started
# 📋 Prerequisites
Docker and Docker Compose installed on your machine.

# 🛠️ Installation
## 1- Clone the repository:
```bash
git clone https://github.com/minarefaat1002/Egyptian-National-ID-Validator-and-Data-Extractor-API.git
cd Egyptian-National-ID-Validator-and-Data-Extractor-API
```
## 2- Start the application using Docker Compose:
```bash
docker-compose up --build
```
This will:
1- Build the Docker images for the FastAPI app and PostgreSQL database.
2- Start the containers and link them together.

## 3- Access the API:
1- The FastAPI app will be running at http://localhost:8000.
2- You can access the interactive API documentation (Swagger UI) at http://localhost:8000/docs.
