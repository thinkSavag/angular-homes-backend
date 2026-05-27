# NewEdg Backend API

FastAPI backend for the NewEdg Angular application.

This backend serves housing/location data to the Angular frontend and is designed to support local development first, with future deployment to Render or Google Cloud Run.

---

## Tech Stack

- FastAPI
- Uvicorn
- Python
- Angular frontend integration
- CORS-enabled API

---

## Project Structure

backend/ <br>
│<br>
├── app/<br>
│   ├── main.py<br>
│   └── routes/<br>
│       └── locations.py<br>
│<br>
├── requirements.txt<br>
└── README.md<br><br>

---

## Local Development Setup

### 1. Create Virtual Environment

Windows:
```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run FastAPI Server

From the backend folder:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## API Endpoints

### Root Endpoint
This project originally extended the Angular Homes tutorial and evolved into a separated frontend/backend architecture using FastAPI:
https://github.com/thinkSavag/angular-homes-tutorial


### YouTube Guides
Part 1: [Angular Homes Tutorial] https://www.youtube.com/watch?v=UZm4DsxCeog&list=PL47k7fyMzVz5JUjLihHIkOCsYJycmnQHi&index=3
Part 2: [Extend Original Tutorial]https://www.youtube.com/watch?v=YSgHA4aIXw0&list=PL47k7fyMzVz5JUjLihHIkOCsYJycmnQHi&index=4
Part 3: [Replace API to Local Environment] https://www.youtube.com/watch?v=VLvflhqNR-8&list=PL47k7fyMzVz5JUjLihHIkOCsYJycmnQHi&index=5
Part 4 [Connect to Firebase]: https://www.youtube.com/watch?v=cJ2um80x-TM&list=PL47k7fyMzVz5JUjLihHIkOCsYJycmnQHi&index=6