import ast

# בדיקה 1: אורך קובץ
def check_file_length(lines, filename, max_lines=200):
    if len(lines) > max_lines:
        return [{
            "filename": filename,
            "type": "FileTooLong",
            "message": f"הקובץ מכיל {len(lines)} שורות (המקסימום הוא {max_lines})"
        }]
    return []

# בדיקה 2 + 4: פונקציות ארוכות / ללא מחרוזת תיעוד
def check_functions(tree, filename):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # בדיקת אורך
            start = node.lineno
            end = getattr(node, 'end_lineno', start)
            length = end - start + 1
            if length > 20:
                issues.append({
                    "filename": filename,
                    "type": "FunctionTooLong",
                    "function": node.name,
                    "message": f"הפונקציה '{node.name}' ארוכה מדי: {length} שורות"
                })

            # בדיקת מחרוזת תיעוד
            if not ast.get_docstring(node):
                issues.append({
                    "filename": filename,
                    "type": "MissingDocstring",
                    "function": node.name,
                    "message": f"הפונקציה '{node.name}' חסרה מחרוזת תיעוד"
                })
    return issues

# בדיקה 3: משתנים שאינם בשימוש
def check_unused_variables(tree, filename):
    assigned = set()
    used = set()

    class VariableVisitor(ast.NodeVisitor):
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):
                assigned.add(node.id)
            elif isinstance(node.ctx, ast.Load):
                used.add(node.id)

    VariableVisitor().visit(tree)

    unused = assigned - used
    issues = [{
        "filename": filename,
        "type": "UnusedVariable",
        "variable": var,
        "message": f"המשתנה '{var}' הוגדר אך לא נעשה בו שימוש"
    } for var in unused]

    return issues

# פונקציית ניתוח ראשית
def analyze_code(code: str, filename: str):
    tree = ast.parse(code)
    lines = code.splitlines()

    issues = []
    issues += check_file_length(lines, filename)
    issues += check_functions(tree, filename)
    issues += check_unused_variables(tree, filename)
    return issues
