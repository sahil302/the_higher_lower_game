import random
import time
from game_data import data
from art import logo , vs
print(logo)
def random_picker():
    random_number=random.randint(0,51)
    length=len(data)
    #print(random_number)
    names=(data[random_number]['name'])
    Country=(data[random_number]['country'])
    Description=(data[random_number]['description'])
    global follwer1
    follwer1=(data[random_number]['follower_count'])
    print(f"{names} from {Country} is {Description}")
def random_picker2():
    random_number=random.randint(0,51)
    length=len(data)
    #print(random_number)
    names=(data[random_number]['name'])
    Country=(data[random_number]['country'])
    Description=(data[random_number]['description'])
    global follwer2
    follwer2=(data[random_number]['follower_count'])
    print(f"{names} from {Country} is {Description}")
def checker():
    game=False
    score=0
    while game!=True:
        random_picker()
        print(vs)
        random_picker2()
        b=follwer1
        a=follwer2
        print("..........................................")
        print("..........................................")
        answer=input("who has more follower? A or B ====>")
        if answer=="A":
            if a<b:
                print("you guessed it right")
                score+=1
                print(f"your score is {score}")
                print("..........................................")
                print("..........................................")
            else:
                print("game over")
                print(f"your score is {score}")
                game=True
                time.sleep(100)
        elif answer=="B":
            if a>b:
                print("you guessed it right")
                score+=1
                print(f"your score is {score}")
                print("..........................................")
                print("..........................................")
            else:
                print("game over")
                print(f"your score is {score}")
                game=True
                time.sleep(100)
checker()
