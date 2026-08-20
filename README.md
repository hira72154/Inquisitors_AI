Inquisitors Society AI Assistant

Project Overview

The Inquisitors Society AI Assistant is an AI-powered assistant for the Inquisitors Society project. It provides two main features:

AI Chatbot — answers questions about Inquisitors Society.

AI Interview Practice — generates interview questions and evaluates interview answers.

The frontend is provided as a single index.html file, while the backend is built with FastAPI and exposes API endpoints for the AI features.

Features

AI Chatbot

Users can ask questions about Inquisitors Society. The frontend sends the user's message to the live FastAPI backend and displays the AI response.

AI Interview Practice

The system supports:

Generating interview questions

Submitting interview answers

Evaluating interview answers

Frontend

The frontend is contained in:

index.html

No separate JavaScript file is required because the HTML file contains the required frontend JavaScript.

Project Structure

inquisitors-ai/
├── index.html
└── README.md

The backend is hosted separately on FastAPI Cloud.

Live Backend

Current FastAPI backend:

https://inquisitors-ai-9d64f4c7.fastapicloud.dev

The frontend is already configured to communicate with this backend.

API Endpoints

Chatbot

POST

/chat

Full endpoint:

https://inquisitors-ai-9d64f4c7.fastapicloud.dev/chat

Example request:

{
"message": "What is Inquisitors Society?"
}

Example response:

{
"message": "What is Inquisitors Society?",
"response": "AI-generated answer..."
}

Interview Question

POST

/interview/question

Full endpoint:

https://inquisitors-ai-9d64f4c7.fastapicloud.dev/interview/question

This endpoint is used to generate interview questions.

Interview Evaluation

POST

/interview/evaluate

Full endpoint:

https://inquisitors-ai-9d64f4c7.fastapicloud.dev/interview/evaluate

This endpoint is used to evaluate an interview answer.

How the Frontend Works

User
│
▼
index.html
│
├── Chatbot ──────────────► POST /chat
│
└── Interview Practice ──► /interview/question
/interview/evaluate
│
▼
FastAPI Backend
│
▼
AI Response
│
▼
Frontend UI

Team Integration

The frontend can be integrated into the main Inquisitors Society website/project.

Chatbot Integration

Use:

https://inquisitors-ai-9d64f4c7.fastapicloud.dev/chat

Send a POST request with:

{
"message": "user message here"
}

Then display the response field returned by the API.

Interview Integration

Use:

/interview/question

to generate questions and:

/interview/evaluate

to evaluate answers.

The team can either reuse the existing UI from index.html or rebuild the UI inside the main project while continuing to use the same backend APIs.

Local Frontend Testing

Because the frontend is a single HTML file, it can be tested locally by opening:

index.html

in a browser.

The frontend communicates with the deployed FastAPI backend, so a local backend is not required for basic API testing.

Backend Status

The live backend has been tested successfully.

Example:

POST /chat
200 OK

Technologies Used

HTML

CSS

JavaScript

FastAPI

Python

AI/LLM backend

FastAPI Cloud

GitHub

Important Notes

Do not put API keys or other secrets inside index.html.

The frontend should communicate with the backend API.

The live backend URL can be changed later if the backend is moved.

The team can integrate this chatbot into the main project without deploying this standalone frontend separately.

Integration Checklist

Copy/reuse the chatbot UI

Connect the chat input to POST /chat

Test a sample chatbot question

Connect interview question generation

Connect interview answer evaluation

Verify CORS if the main website uses a different domain

Test the final integrated website

Repository

This repository contains the frontend implementation and integration information required by the Inquisitors Society project team.

The backend is available through the live FastAPI deployment mentioned above.
