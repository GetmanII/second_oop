from classes.user import User, UserManager

manager = UserManager()

print(manager.add_user(User("user1", "email1", 20)))
print(manager.add_user(User("user2", "email2", 30)))
print(manager.add_user(User("user1", "email3", 40)))

print(manager.find_user("user1"))

print(manager.remove_user("user1"))

print(manager.remove_user("user1"))

print(manager.find_user("user1"))