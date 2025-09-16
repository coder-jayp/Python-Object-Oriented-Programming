import re
import os
from dotenv import load_dotenv

load_dotenv()

class User:
    def __init__(self, username: str):
        self.username = username
        self.__password = None

    def create_password(self, password: str):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one number.")
        
        self.__password = password
        print("Password set successfully")

    def verify_password(self, password: str) -> bool:
        return self.__password == password


password_from_env = os.getenv("USER_PASSWORD", "demo_password")

user1 = User("demo_user")
user1.create_password(password_from_env)

print(user1.verify_password("hey123"))
