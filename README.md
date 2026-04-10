# LLM Query API 

## Overview

This project is a simple and structured API that accepts a user query and generates a response using a Large Language Model (LLM).
The API is built using FastAPI and integrates with Groq for fast and efficient inference.

---

## Features

* Accepts user input via REST API
* Sends query to an LLM (Groq)
* Returns a clear and structured response
* Lightweight and easy to use
* Interactive API testing via Swagger UI

---

## Tech Stack

* Python
* FastAPI
* Groq API
* Uvicorn

---

## Project Structure

```
llm-query-app/
│── main.py
│── requirements.txt
│── .env (not included in repo)
│── .gitignore
│── README.md
│── screenshots/
```

---

## Setup Instructions

### 1) Clone the Repository

```
git clone https://github.com/mansityagi0606-lab/llm-query-app.git
cd llm-query-app
```

---

### 2) Install Dependencies

```
pip install -r requirements.txt
```

---

### 3) Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4) Run the Application

```
uvicorn main:app --reload
```

---

### 5) Access API Docs

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoint

### POST `/ask`

#### Request Body:

```json
{
  "query": "What is Artificial Intelligence?"
}
```

#### Response:

```json
{
  "query": "What is Artificial Intelligence?",
  "response": "Artificial Intelligence (AI) refers to..."
}
```

---

## How It Works

1. User sends a query via API
2. FastAPI processes the request
3. Query is sent to Groq LLM
4. Model generates a response
5. API returns the result in JSON format

---

## Security Note

* API keys are stored securely using environment variables
* `.env` file is excluded using `.gitignore`
* Sensitive data is not pushed to the repository

---

## Screenshots
<img width="1352" height="640" alt="Capture" src="https://github.com/user-attachments/assets/f0248c35-68b7-4ba0-99d9-ea17625622d7" />
<img width="1308" height="632" alt="Capture2" src="https://github.com/user-attachments/assets/54d3251e-81e8-4c19-9992-fbb07fb066c3" />



