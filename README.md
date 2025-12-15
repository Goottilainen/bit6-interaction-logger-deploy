# BIT6 – AI Web Application (Flask API)

This project is a simple REST API built with **Flask** as part of the BIT6 module.

# Features
- Health check endpoint
- POST endpoint to process JSON data
- REST architecture

# Endpoints

# GET /
Returns a simple message to confirm the API is running.

# GET /health
Returns the status of the API.

# POST /process
Accepts JSON data and returns it back as a response.

Example request body:
```json
{
  "text": "hello world"
}

Technologies

Python 3

Flask

How to run locally
python app.py

The API will be available at:
http://127.0.0.1:5000