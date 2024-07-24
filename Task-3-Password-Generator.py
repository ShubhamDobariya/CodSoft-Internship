import random
import string

def genpassword(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be 1, 2, or 3.")

    password = ''.join(random.choice(characters) for k in range(length))
    return password

def password():
    print("------------------------------------------")
    print("                                          ")
    print("-x-x-x-x-x- Password Generator -x-x-x-x-x-")
    print("                                          ")
    print("------------------------------------------")


    length = int(input("Enter length of the password: "))

    print("                                            ")
    print("---x---x---x- Complexity Levels: -x---x---x---")
    print("                                            ")

    print("1 for Only letters(a-z,A-Z)")
    print("2 for Letters(a-z,A-Z) and digits(0-9)")
    print("3 for Letters, digits, and special characters(!,@,#,$,&,%,*,etc.)")
    complexity = int(input("select complexity level (1, 2, or 3): "))

    if length <= 0:
        print("Please enter valid Input!!")
        return
    
    if complexity not in [1, 2, 3]:
        print("Invalid complexity level!!. Please choose between 1, 2, or 3.")
        return

    password = genpassword(length, complexity)
    print(f"Your Generated Password is : {password}")

if __name__ == "__main__":
    password()
