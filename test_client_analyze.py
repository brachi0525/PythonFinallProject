import requests

# רשימת קבצים לשליחה
file_paths = ["test.py", "test2.py"]

# כתובת השרת
url = "http://127.0.0.1:8000/analyze"

# בניית הרשימה של הקבצים (שימו לב ל-[] סביב כל קובץ)
files = [("files", (fp, open(fp, "rb"), "text/x-python")) for fp in file_paths]

# שליחת הבקשה
response = requests.post(url, files=files)

# סגירת כל הקבצים (אופציונלי, רק אם רוצים לנקות כמו שצריך)
for _, (fp, file_obj, _) in files:
    file_obj.close()

# תגובת JSON
response_json = response.json()

# הדפסת הנתיב לכל גרף
print(response_json)
