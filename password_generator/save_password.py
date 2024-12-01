from datetime import datetime

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(f"{password} - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
