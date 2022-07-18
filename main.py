from turtle import title
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]= None

#dictionary of post objects
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id" : 1},{"title": "title of post 2", "content": "content of post 2", "id" : 2}]

# request for get method, url: "/"
@app.get("/")
def root():
    return{"message": "Welcome!!"}

#find specific post 
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#body is the json output converted into a dictionary, Post object stored into new_post var 
@app.post("/posts")
def create_posts(post: Post):
     post_dict = post.dict()
     post_dict['id'] = randrange(0, 10000000)
     my_posts.append(post_dict)
#    print(post)
#    print(post.dict()) #convert to dict 
     return {"data": post_dict }

@app.get("/posts/{id}")
def get_post(id):
    post = find_post(int(id))
    return{"post_detail": post}