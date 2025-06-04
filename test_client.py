import requests
from bidi.algorithm import get_display

# נתיב לקובץ שאת רוצה לבדוק
file_path = "test.py"

# כתובת השרת שלך
url = "http://127.0.0.1:8000/alerts"

def print_alerts(alerts_response):
    alerts = alerts_response.get('alerts', [])
    if not alerts:
        print(get_display("אין אזהרות."))
        return

    for alert in alerts:
        filename = alert.get('filename', 'לא ידוע')
        alert_type = alert.get('type', 'לא ידוע')
        message = alert.get('message', '')
        func = alert.get('function', '')
        var = alert.get('variable', '')

        print(get_display(f"קובץ: {filename}"))

        if alert_type == "MissingDocstring":
            print(get_display(f" - סוג אזהרה: חסר Docstring בפונקציה"))
            print(get_display(f" - פונקציה: {func}"))
            print(get_display(f" - הודעה: {message}"))

        elif alert_type == "UnusedVariable":
            print(get_display(f" - סוג אזהרה: משתנה לא בשימוש"))
            print(get_display(f" - משתנה: {var}"))
            print(get_display(f" - הודעה: {message}"))

        else:
            print(get_display(f" - סוג אזהרה: {alert_type}"))
            print(get_display(f" - הודעה: {message}"))

        print(get_display("-" * 40))


def print_dict(d, indent=0):
    space = "  " * indent
    if isinstance(d, dict):
        for key, value in d.items():
            print(get_display(f"{space}{key}:"))
            print_dict(value, indent + 1)
    elif isinstance(d, list):
        for i, item in enumerate(d):
            print(get_display(f"{space}- פריט {i+1}:"))
            print_dict(item, indent + 1)
    else:
        print(get_display(f"{space}{d}"))


# שליחת בקשת POST עם הקובץ
with open(file_path, "rb") as f:
    files = {"files": (file_path, f, "text/x-python")}
    response = requests.post(url, files=files)

print(get_display("Status code: ") + str(response.status_code))

# הדפסת תגובת JSON בצורה מסודרת עם טיפול בכיוון טקסט
response_json = response.json()
print_alerts(response_json)
print_dict(response_json)
