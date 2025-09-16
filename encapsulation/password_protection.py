import re

class User:
    def __init__(self, username: str):
        self.username = username
        self.__password = None

    def create_password(self, password:str):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one number.")
        
        self.__password = password
        print(f"Password set successfully")

    def verify_password(self, password: str) -> bool:
        return self.__password == password
    
user1 = User("Jay")
user1.create_password("heyasdfdf123")
print(user1.verify_password("hey123"))