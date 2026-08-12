#Q8 : Decorator-based Access Control 
# Scenario: 
# Restrict access to certain functions. 
# Task: 
# ● Create a decorator to check user role 
# ● Use condition inside decorator 
# ● Apply decorator to multiple functions 
# ● Store roles in a dictionary 
# Store user roles in a dictionary
roles = {"admin": "Admin","user": "User","guest": "Guest"}
def check_role(required_role):
    def decorator(function):
        def wrapper(username):
            if roles.get(username) == required_role:
                function(username)
            else:
                print("Access Denied")
        return wrapper
    return decorator
@check_role("Admin")
def delete_user(username):
    print("User deleted successfully")
@check_role("Admin")
def add_user(username):
    print("User added successfully")
@check_role("User")
def view_profile(username):
    print("Profile viewed successfully")
delete_user("admin")
add_user("user")
view_profile("user")
view_profile("guest")