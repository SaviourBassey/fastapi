from fastapi import APIRouter
from ..schemas import user_schema


router = APIRouter(
    tags=["users"]
)


@router.get("/users/get-all-user")
def get_user():
    return {"all": "All users"}


@router.get("/users/get-user/{ID}")
def get_user(ID):
    return {"user": f"user Details with the id: {ID}"}


@router.get("/users/filter-user")
def get_user(user_first_name):
    return {"user": f"list of users with the name: {user_first_name}"}


@router.post("/users/add-user", response_model=user_schema.User)
def get_user(user:user_schema.User):
    return  user