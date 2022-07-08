from fastapi import FastAPI

app = FastAPI()

# request for get method, url: "/"
@app.get("/")
def root():
    return{"message": "Welcome!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}