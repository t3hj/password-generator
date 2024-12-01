from datetime import datetime, timedelta

def set_expiration_reminder():
    expiration_date = datetime.now() + timedelta(days=30)
    with open("passwords.txt", "a") as file:
        file.write(f"Password expires on {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
