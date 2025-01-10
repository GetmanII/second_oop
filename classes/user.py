import bcrypt


class User:
    users = [] 
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = self.hash_password(password)
        User.users.append(self)
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash)
    
class Customer(User):
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address
    
    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"
    
class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email,  password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
    
    @staticmethod
    def list_users():
        return [user.get_details() for user in User.users]
    
    @staticmethod
    def delete_user(username):
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
                return f"Пользователь {username} удален."
        return f"Пользователь {username} не найден."
            
class AuthenticationService:
    def __init__(self):
        self.current_user = None
        
    def register(self, user_class, username, email, password, *args):
        if any(user.username == username for user in User.users):
            return f"Пользователь {username} с таким именем уже зарегистрирован."
        user_class(username, email, password, *args)
        return f"Пользователь {username} зарегистрирован."
    
    def login(self, username, password):
        for user in User.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                return f"Пользователь {username} успешно авторизован."
        return f"Неверное имя пользователя или пароль."
    
    def logout(self):
        if self.current_user:
            logged_out_user = self.current_user.username
            self.current_user = None
            return f"Пользователь {logged_out_user} успешно вышел из системы."
        return "Никто не авторизован."
    def get_current_user(self):
        if self.current_user:
            return f"Пользователь в сети: {self.current_user.get_details()}"
        return "Никто не авторизован."