# PythonFinallProject
🎯 Overview
CodeGuard הוא מערכת ניתוח קוד המשולבת עם פקודת wit push כדי להבטיח שמירה על איכות קוד גבוהה בכל הקומיטים. המערכת מבצעת בדיקות איכות קוד ומחזירה גרפים עם תובנות ונתונים על בעיות בקוד.

המערכת מדמה תהליך CI בסיסי, בדגש על איכות קוד.

🛠️ Technologies Used
Language: Python

Backend Framework: FastAPI

Code Analysis: ast (Abstract Syntax Tree)

Visualization: matplotlib

📂 Folder Structure
bash
CopyEdit
CodeGuard/
├── main.py          # FastAPI application
├── analysis.py      # Code analysis logic (using ast)
├── visualization.py # Graph generation logic (matplotlib)
├── alerts.py        # Issue detection logic
├── requirements.txt # Python dependencies
├── README.md        # Project documentation (this file)
└── tests/           # Unit tests for API and logic
🚀 Installation Instructions
1️⃣ Clone the repository

bash
CopyEdit
git clone https://github.com/HadassaAvimorNew/codeguard.git
cd codeguard
2️⃣ Create virtual environment & install dependencies

bash
CopyEdit
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
3️⃣ Run the server

bash
CopyEdit
uvicorn main:app --reload
The server will run at: http://127.0.0.1:8000

🌐 API Endpoints
Endpoint	Method	Description
/analyze	POST	מקבל קבצי Python ומחזיר גרפים (PNG)
/alerts	POST	מקבל קבצי Python ומחזיר התראות על בעיות קוד

Example Request (Using curl)
bash
CopyEdit
curl -X POST -F "file=@example.py" http://127.0.0.1:8000/analyze
curl -X POST -F "file=@example.py" http://127.0.0.1:8000/alerts
🔍 Code Quality Checks
Function Length: התראה אם פונקציה ארוכה מ־20 שורות

File Length: התראה אם הקובץ כולו ארוך מ־200 שורות

Unused Variables: התראה על משתנים שלא בשימוש

Missing Docstrings: התראה על פונקציות ללא תיעוד

🏆 Bonus
✔️ זיהוי משתנים בשמות שאינם באנגלית (כגון בעברית) – והצגת התראה על כך

📊 Visualizations
📉 Histogram – התפלגות אורכי הפונקציות

🥧 Pie Chart – כמות הבעיות לפי סוג

📊 Bar Chart – כמות הבעיות לפי קובץ

📈 (Bonus) Line Graph – מעקב אחר מספר הבעיות לאורך זמן

📅 Submission
קוד מלא הועלה לרפוזיטורי GitHub:
https://github.com/HadassaAvimorNew/codeguard
פרויקט זה מופץ תחת רישוי MIT.

קישורים שימושיים
FastAPI Documentation
Matplotlib Documentation
