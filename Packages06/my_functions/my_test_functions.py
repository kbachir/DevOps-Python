import os

work_dir = os.getcwd()

def return_user_id():
    return os.getuid()

def return_os_info():
    return os.uname()

