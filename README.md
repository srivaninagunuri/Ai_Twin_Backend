# AI Twin Backend – Basic Info Module

## Overview

This repository contains the backend implementation for the **Basic Info** module of the AI Twin platform.

The Basic Info module is responsible for collecting and managing the initial information required to create an AI Twin, including profile details and metadata required for subsequent steps such as Appearance, Voice, Lip Sync, and AI Training.

---

## Features

* Create AI Twin basic information
* Input validation using Pydantic
* REST APIs built with FastAPI
* Structured request and response models
* Interactive API documentation with Swagger UI
* Modular backend architecture

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* PostgreSQL
* VS Code

---

## Project Structure

```text
Ai_Twin_Backend/
│
├── main.py
├── routers/
├── services/
├── models/
├── schemas/
├── database/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/srivaninagunuri/Ai_Twin_Backend.git
cd Ai_Twin_Backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## API Functionality

### Basic Info Module

* Create AI Twin profile information
* Validate user inputs
* Store profile data
* Return structured responses
* Support integration with later stages:

  * Appearance
  * Voice
  * Lip Sync
  * Train AI
  * Preview

---

## Future Enhancements

* Authentication and Authorization
* Image Upload Support
* Cloud Deployment on Google Cloud Platform
* Integration with AI Training Module
* Logging and Monitoring

---

## Author

**Srivani Nagunuri**

AI/ML Engineer Intern

Working on AI Twin Product Development
# Ai_Twin_Backend
