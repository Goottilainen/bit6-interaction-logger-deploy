# BIT6.2 – Minimal AI-Powered Web Application

This project is a minimal full-stack AI-powered web application built as part of the **BIT6.2 assignment**.  
It demonstrates the interaction between a **React frontend**, a **Python backend**, a **PostgreSQL database**, and an **external AI service**.

The goal of this project is not to build a complex product, but to implement the **basic functional structure of a modern web application**.

---

## Features

- Single-page frontend where users can submit text input
- Backend service that sends the input to an AI model
- AI-generated response displayed in the frontend
- Each prompt and response is stored in a PostgreSQL database
- Fully deployed using free-tier platforms

---

## Tech Stack

### Frontend
- React (Vite)
- JavaScript
- HTML / CSS

### Backend
- Python
- Flask
- OpenAI API

### Database
- PostgreSQL (managed database on Render)

### Deployment Platforms
- Frontend: Vercel
- Backend: Render
- Database: Render PostgreSQL

---

## Live Deployment

**Frontend (Vercel):**  
https://bit6-ai-webapp-frontend.vercel.app

**Backend (Render):**  
https://ai-webapp-backend.onrender.com

**API Endpoint:**  
POST https://ai-webapp-backend.onrender.com/process

---

## Application Architecture

1. The user enters a text prompt in the frontend.
2. The frontend sends the prompt to the backend API.
3. The backend forwards the prompt to an AI model (OpenAI).
4. The AI generates a response.
5. The backend:
   - Saves the prompt and response in PostgreSQL
   - Returns the AI response to the frontend
6. The frontend displays the response to the user.

---

## Database Structure

A single PostgreSQL table is used.

**Table: `prompts`**

| Column        | Type      | Description               |
|---------------|-----------|---------------------------|
| id            | SERIAL    | Primary key               |
| user_prompt   | TEXT      | User input                |
| ai_response   | TEXT      | AI generated response     |
| created_at    | TIMESTAMP | Time of request           |

---

## Environment Variables

### Backend Environment Variables

The backend requires the following environment variables:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>:5432/<database>?sslmode=require
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=production

These variables are configured in the Render dashboard for the deployed backend.

Run Locally
Clone the Repository

git clone https://github.com/Goottilainen/bit6-interaction-logger-deploy.git

cd bit6-interaction-logger-deploy

Backend Setup

cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt


Create a .env file inside the backend folder:

DATABASE_URL=your_local_or_remote_postgres_url
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development

Run the backend:

python app.py

The backend will run on:

http://localhost:5000

Frontend Setup:

cd frontend
npm install
npm run dev

The frontend will run on:

http://localhost:5173

Deployment Process

Backend Deployment (Render)

- Create a new Web Service on Render

- Connect the GitHub repository

- Set the build and start commands:

     Build command: pip install -r requirements.txt

     Start command: python app.py

Add environment variables in Render:

     DATABASE_URL

     OPENAI_API_KEY

     FLASK_ENV=production

Deploy the service

Database Deployment (Render PostgreSQL)

1) Create a PostgreSQL database on Render

2) Copy the Internal Database URL

3) Use it as the DATABASE_URL environment variable in the backend

4) The backend automatically initializes the database table on startup

Frontend Deployment (Vercel)

Navigate to the frontend folder

Login to Vercel:

vercel login

Deploy the frontend:

vercel

Use the detected Vite settings:

   Build command: vite build

   Output directory: dist

Vercel generates a public URL for the frontend


Submission

All code and documentation are included in this repository and pushed to the GitHub Classroom repository provided for the assignment.

This project fulfills all technical and deployment requirements of the BIT6.2 – Minimal AI-Powered Web Application assignment.

Assignment Status:

✔ Frontend implemented and deployed

✔ Backend implemented and deployed

✔ PostgreSQL database integrated

✔ AI API integrated

✔ Data persistence confirmed

✔ Documentation completed