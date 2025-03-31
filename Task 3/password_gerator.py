import random

def main():
    print("============PASSWORD GENERATOR================")
    print()
    password_deisired_length = int(input("How long do you want the password to be\n"))
    print("Generated Password: ",generate_password(password_deisired_length))
    if password_deisired_length<8:
        print("PASSWORD STATUS: VERY WEAK ")
    elif password_deisired_length>=8 and password_deisired_length<12:
        print("PASSWORD STATUS: STRONG ")
    else:
        print("PASSWORD STATUS: VERY STRONG ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print()

def generate_password(password_length:int):
    characters="ABCDEFGHIJKabcdefghijklmnopqrstuvwxyzLMNOPQRSTU0987654321VWXYZ!@#$%^&*()_+/.,"
    password=""
    for i in range(password_length):
        random_char= random.choice(characters)
        password+=random_char

    return password

    

if __name__=="__main__":
    main()