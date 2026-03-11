# Base model for all database tables
class BaseModel:
    pass

# Schema for application users
class User:
    id = int
    email = str
    password_hash = str