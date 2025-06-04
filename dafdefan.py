import requests
import webbrowser
import tempfile

files = {"files": open("test.py", "rb")}  # תחליף לשם קובץ אמיתי או לולאה עם כמה קבצים

response = requests.post("http://127.0.0.1:8000/analyze", files=files)

if response.status_code == 200:
    html = response.text
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as tmp_file:
        tmp_file.write(html)
        tmp_path = tmp_file.name

    webbrowser.open(f"file://{tmp_path}")
else:
    print("Error:", response.status_code)
