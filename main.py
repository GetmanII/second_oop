from classes.user import User, Customer, Admin, AuthenticationService


auth_service = AuthenticationService()
print(auth_service.register(Customer, "Антон", "anton@example.com", "password123", "Улица Пушкина, дом Колотушкина"))
print(auth_service.register(Admin, "admin", "admin@example.com", "adminpass", 1))
print(auth_service.login("Антон", "password1234"))
print(auth_service.login("Антон", "password123"))
print(auth_service.get_current_user())
print(auth_service.logout())
print(Admin.list_users())
print(Admin.delete_user("Антон"))
print(Admin.list_users())
