from fastapi import FastAPI
from .api import users, items

description = """

"""

app = FastAPI(
    title= "An endpoint for kodecamp intermediate",
    description="This is a description",
    summary= "This is a summary",
    version="0.0.1",
    contact={
        "name": "Group 1",
        "email": "person1@gmail.com"
    },
    docs_url="/group1/documentation"
)

app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
def root():
    return {"message": "Well Structured Folder"}