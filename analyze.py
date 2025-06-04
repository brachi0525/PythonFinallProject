import os
import uuid
import ast
import matplotlib.pyplot as plt
from collections import Counter
from fastapi import UploadFile

# כתובת בסיס לשימוש בקישורים - מתאימה אם אתה מריץ את FastAPI בברירת מחדל
BASE_STATIC_URL = "http://127.0.0.1:8000/static"

def generate_histogram(lengths: list[int]) -> str:
    plt.figure()
    bins = range(0, max(lengths) + 5, 5) if lengths else [0, 5]
    plt.hist(lengths, bins=bins, color='skyblue', edgecolor='black')
    plt.title("התפלגות אורכי פונקציות")
    plt.xlabel("אורך פונקציה (שורות)")
    plt.ylabel("כמות פונקציות")

    os.makedirs("static", exist_ok=True)
    filename = f"histogram_{uuid.uuid4().hex}.png"
    path = os.path.join("static", filename)
    plt.savefig(path)
    plt.close()
    return f"{BASE_STATIC_URL}/{filename}"


def generate_pie_chart(data: dict[str, int]) -> str:
    plt.figure()
    labels = list(data.keys())
    sizes = list(data.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("סוגי בעיות בקוד")

    os.makedirs("static", exist_ok=True)
    filename = f"pie_{uuid.uuid4().hex}.png"
    path = os.path.join("static", filename)
    plt.savefig(path)
    plt.close()
    return f"{BASE_STATIC_URL}/{filename}"


def generate_bar_chart(data: dict[str, int]) -> str:
    plt.figure()
    files = list(data.keys())
    counts = list(data.values())
    plt.bar(files, counts, color='orange', edgecolor='black')
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("כמות בעיות")
    plt.title("מספר בעיות לכל קובץ")

    os.makedirs("static", exist_ok=True)
    filename = f"bar_{uuid.uuid4().hex}.png"
    path = os.path.join("static", filename)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return f"{BASE_STATIC_URL}/{filename}"


async def analyze_files(files: list[UploadFile], analyze_code_func) -> dict:
    """
    מקבלת רשימת קבצים ופונקציית ניתוח,
    מחזירה קישורים לגרפים שנוצרו (ניתנים לפתיחה בדפדפן).
    """
    function_lengths = []
    all_issues = []

    for file in files:
        content = await file.read()
        source_code = content.decode("utf-8")

        # ניתוח בעיות
        issues = analyze_code_func(source_code, file.filename)
        all_issues.extend(issues)

        # חישוב אורכי פונקציות
        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = getattr(node, "end_lineno", start)
                function_lengths.append(end - start + 1)

    # יצירת גרפים
    histogram_url = generate_histogram(function_lengths)
    pie_chart_url = generate_pie_chart(Counter(issue['type'] for issue in all_issues))
    bar_chart_url = generate_bar_chart(Counter(issue['filename'] for issue in all_issues))

    return {
        "histogram": histogram_url,
        "pie_chart": pie_chart_url,
        "bar_chart": bar_chart_url,
    }
