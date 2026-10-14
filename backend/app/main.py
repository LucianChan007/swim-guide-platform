from fastapi import FastAPI

app = FastAPI(title="Swim Guide Platform API")

@app.get("/")
def root():
    return {"message": "Swim Guide Platform API"}
