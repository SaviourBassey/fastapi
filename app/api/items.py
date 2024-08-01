from fastapi import APIRouter

router = APIRouter(
    tags=["items"]
)


@router.get("/items/get-all-item")
def get_item():
    return {"all": "All Items"}


@router.get("/items/get-item")
def get_item():
    return {"item": "Item Details"}