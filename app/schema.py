from pydantic import BaseModel
from ninja import Schema

# Pydantic models that provide data validation of data received


# Ninja Schema that ensures that ensures formatting of incoming and outgoing JSON objects
class Error(Schema):
    error: str


class Auth(Schema):
    email: str
    first_name: str
    