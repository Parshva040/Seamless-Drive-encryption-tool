from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_strength(password):
    result=zxcvbn(password)
    score = result["score"]
    if score == 3:
        response = "Strong enough password"
    elif score == 4:
        response = "Strong password"
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = "weak password : score of " + str(score)
        response += "\nwarning: " + warning
        response += "\nsuggestions: "
        for suggestion in suggestions:
            response += " " + suggestion
    return response

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(pw_attempt, hashed):
    if bcrypt.checkpw(pw_attempt.encode(), hashed):
        return "Password is correct"
    else:
        return "password is incorrect"
    
def password():
    
    while True:
        password1 = getpass("enter a password: ")
        print(check_strength(password1))
        if check_strength(password1).startswith("weak"):
            print("Please choose stronger password")
        else: 
            break
    hashed_password = hash_pw(password1)
    print("hashed password: ", hashed_password)
    attempt = getpass("re-enter password to verify: ")
    print(verify_password(attempt, hashed_password))
        
if __name__ == "__main__":
    password()