password = "password2024"

prompt = input("Enter the user password? :")

while str(prompt) != password:
    prompt = input("Enter the user password? :")

    if str(prompt) == password:
        print ("Access granted!")
    else:
        print(f"Incorrect password")
