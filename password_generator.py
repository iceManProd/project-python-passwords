#this is my program, is a password generator
#But i forgot the way how I was writed this programm
import random

def password_generator():
    mayus = ['A','B','C','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minus = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5']
    symbols = ['!','¡','¿','?','#']

    characters = mayus + minus + numbers + symbols

    password = []

    for i in range (15):
        random_character = random.choice(characters)
        password.append(random_character)
    
    password = ''.join(password)
    return password

def run():
    

    password = password_generator()
    print("""
    >>> Your new password is: """+password)


if __name__=='__main__':
    run()
