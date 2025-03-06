# Importing module user_admin.
import user_admin
# Importing module user.
import user

# Creating admin.
user_admin_lmpkessels = user_admin.Admin(first_name="luuk", last_name="kessels", 
                              user_name="admin_lmpkessels", 
                              user_email="admin@lmpkessels", 
                              password="AdminLmP123!.!")

# Creating user.
user_anja = user.User(first_name="anja", last_name="kessels", 
                      user_name="anja-kessels1967", 
                      user_email="anja.kessels@live.nl", 
                      password="JoLuKo1967!!")

# Creating list of privileges for admin.
admin_privilege_list = [
    "can add post",
    "can delete post",
    "can ban user",
]

print("\n")
# Assigning privileges list to privilige list of module user_admin.
user_admin_lmpkessels.privileges.privileges_list = admin_privilege_list

print("\n")
# Calling method show_privileges to display privileges for admin.
user_admin_lmpkessels.privileges.show_privileges()

print("\n")
# Getting user discription out of the module user.
user_anja.get_user_description()
user_anja.privileges.show_privileges()