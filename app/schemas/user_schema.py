from pydantic import BaseModel, Field

class User(BaseModel):
    fisrt_name:str = Field(..., example="Foo")
    last_name:str = Field(..., example="Bar")
    email:str = Field(..., example="FooBar@gmail.com")