# AI Web App – BIT6 Project

This project is a simple full-stack AI web application developed for the BIT6 module.

The application allows users to enter a text prompt through a web interface.  
The prompt is sent to a Flask backend API, processed, stored in a PostgreSQL database, and returned as a response.

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript (Vite)
- Backend: Python (Flask)
- Database: PostgreSQL
- API Communication: REST (JSON)

---

## Features

- Text input from frontend
- Backend API endpoint (`/process`)
- Database persistence of prompts and responses
- Timestamped records stored in PostgreSQL

---

## Project Structure

bit6-ai-webapp/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── .env (not included)
│
├── frontend/
│ ├── src/
│ ├── index.html
│ ├── package.json
│
├── README.md


---

## How to Run the Project Locally

### Backend


```bash
cd backend
python app.py

Backend runs on:

http://127.0.0.1:5000

Frontend
cd frontend
npm install
npm run dev


Frontend runs on:

http://localhost:5173

Database

The application uses PostgreSQL to store user prompts and AI responses.
Database credentials are managed using environment variables.

Notes

This project focuses on demonstrating frontend-backend communication, API handling, and database integration.