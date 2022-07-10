from turtle import title
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]= None

# request for get method, url: "/"
@app.get("/")
def root():
    return{"message": "Welcome!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}

#body is the json output converted into a dictionary, Post object stored into new_post var 
@app.post("/createposts")
def create_posts(post: Post):
   print(post)
   print(post.dict()) #convert to dict 
   return {"data": post }