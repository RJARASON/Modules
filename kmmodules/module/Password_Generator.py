"""Generates Strong or weak passwords"""
def Password_Generator():
    while True:
        try:
            import string
            import random
            Choicer=string.ascii_letters+string.digits+string.punctuation
            print("Password Generator\n")
            num=int(input("Enter Password length: "))
            for length in range(0,num):
                print(random.choice(Choicer),end="")
        except ValueError:
            print("\nInvalid. enter password length")
        break

