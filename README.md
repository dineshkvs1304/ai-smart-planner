# AI Smart Daily Planner (Full Stack AI Task Scheduler)

## Overview
AI Smart Daily Planner is a full-stack productivity application that generates an optimized daily schedule from user tasks.  
The system demonstrates clean architecture, structured backend APIs, database persistence, and AI-style decision logic.

This project was built as a software engineering assessment focusing on clarity, correctness, and extensibility rather than feature count.

---

## Tech Stack

### Backend
- Python
- Flask (REST API)
- SQLite (relational database)

### Frontend
- React (UI)

### Tools & Concepts
- REST API design
- Modular backend structure
- Database persistence
- AI-style scheduling logic
- Clean and readable code
- Separation of concerns

---

## Features

- Add tasks for the day
- AI-style priority scheduling
- Automatic time allocation
- Stores generated schedules in database
- View history of schedules
- Full frontend + backend integration

---

## How AI Logic Works

Instead of random scheduling, the system uses rule-based intelligent prioritization:

Priority order example:
- Study / Exams → Highest priority
- Project / Meetings → High
- Gym / Personal → Medium
- Entertainment → Low

Tasks are sorted using priority detection and then assigned optimized time slots.

This simulates real AI decision-making logic in a controlled, testable way.

---

## API Endpoints

### Generate Schedule
POST `/generate`

Input:

{
"tasks": ["DSA study", "Gym", "Project"]
}


Output:

{
"schedule": [
{"task": "DSA study", "time": "9:00 AM"},
{"task": "Project", "time": "10:00 AM"},
{"task": "Gym", "time": "11:00 AM"}
]
}


### Get History
GET `/history`

Returns all saved schedules from database.

---

## Project Structure
ai-smart-planner
┣ backend
┃ ┣ app.py
┃ ┗ planner.db
┣ frontend
┃ ┗ react application
┗ README.md


---

## Key Engineering Decisions

1. **Simple > Complex**
   Clean readable code over over-engineering.

2. **Separation of Concerns**
   Backend handles logic & storage.
   Frontend handles UI.

3. **Database Persistence**
   Ensures system correctness and history tracking.

4. **AI-style Logic**
   Deterministic priority-based scheduling for reliability.

5. **Extensible Design**
   Can easily integrate real LLM APIs later.

---

## Future Improvements

- Real LLM integration (OpenAI)
- User authentication
- Calendar integration
- Drag-drop scheduling UI
- Deployment (AWS / Vercel)

---

## Run Locally

### Backend

cd backend

pip install flask flask-cors

python app.py


### Frontend

cd frontend

npm install

npm start


---

## Author
Kandyana Venkata Sai Dinesh  
