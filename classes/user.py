class UserAlreadyExistsError(Exception):
    def __init__(self, username: str, message: str = "Пользователь с таким именем уже существует"):
        self.message = message
        self.username = username
        super().__init__(self.message)
    
    def __str__(self):
        return f" {self.message}: {self.username}"


class UserNotFoundError(Exception):
    def __init__(self, username: str, message: str = "Пользователь не найден"):
        self.message = message
        self.username = username
        super().__init__(self.message)
    
    def __str__(self):
        return f" {self.message}: {self.username}"

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Age: {self.age}"
    

class UserManager:
    users = {}
        
    def add_user(self, user: User):
        if user.username in UserManager.users:
            raise UserAlreadyExistsError(user.username)
        UserManager.users[user.username] = user
        return f'Пользователь {user.username} добавлен'
    

    def remove_user(self, username: str):
        if username not in UserManager.users:
            raise UserNotFoundError(username)
        del UserManager.users[username]
        return f'Пользователь {username} удален'
        
    def find_user(self, username: str):
        if username not in UserManager.users:
            raise UserNotFoundError(username)
        return UserManager.users[username]