from fastapi import FastAPI

app = FastAPI(title = "AI Document Search API")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running smoothly."}