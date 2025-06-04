from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from alerts import analyze_code
from analyze import analyze_files

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/analyze")
async def analyze(files: list[UploadFile] = File(...)):

    result = await analyze_files(files, analyze_code)
    return JSONResponse(content=result)

@app.post("/alerts")
async def alerts(files: list[UploadFile] = File(...)):
    results = []

    for file in files:
        content = await file.read()
        source_code = content.decode("utf-8")

        file_issues = analyze_code(source_code, file.filename)
        results.extend(file_issues)

    return JSONResponse(content={"alerts": results})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
