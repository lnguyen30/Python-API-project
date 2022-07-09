from turtle import title
from fastapi import Body, FastAPI

app = FastAPI()

# request for get method, url: "/"
@app.get("/")
def root():
    return{"message": "Welcome!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}

#body is the json output converted into a dictionary, stored into Payload var
@app.post("/create")
def create_posts(payLoad: dict = Body(...)):
   print(payLoad)
   return {"new_post": f"title {payLoad['title']}, content {payLoad['content']}" }