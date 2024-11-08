from fastapi import FastAPI
from readme_service import update_readme

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_event():
    update_readme()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)