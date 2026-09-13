from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to the home page!"}

@app.get("/about")
def about():
    return{"message": "This is the about page."}

@app.get("/contact")
def contact():
    return{"message": "This is the contact page."}
