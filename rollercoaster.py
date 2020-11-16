import random
import time


def coaster3():
    waiting_time = random.choice(range(1, 101))
    print("The waiting time is", waiting_time, "minutes long.")
    question4 = input("Do you want to wait or go back to another rollercoaster?\n (wait/go back)")
    if question4 == "go back":
        coaster = input("To which coaster to you want to go back?\n (coaster1/coaster2)")
        if coaster == "coaster1":
            coaster1()
        elif coaster == "coaster2":
            coaster2()
        else:
            print("I guess you still cannot read...")
    elif question4 == "wait":
        time.sleep(waiting_time)
        print("Now you can ride it. Hang on tight in the last right corner. It gets bumpy.")


def coaster2():
    print("""This is the second rollercoaster.
    If you have a necklace or anything similiar pls tuck it away so you cannot lose it.""")
    question2 = input("Did you tuck away your jewelry?\n (y/n)\n")

    if question2 == "y":
        print("Allright you are ready to go on the ride!")
        coaster3()
    elif question2 == "n":

        question3 = input("pls tuck away your jewelry! \n(y/n)\n")
        if question3 == "y":
            print("Now that it is gone you can ride the rollercoaster. Have fun!")
            coaster3()
        elif question3 == "n":
            print("You really do not want to ride it, do you?")
        else:
            print("You still need to learn how to read properly!")
    else:
        print("I guess you really need to learn how to read!")


def coaster1():
    height = int(input("""Hello and welcome at the first ride.
    Since it is a dangerous one, may I know how tall you are?\n in cm:"""))
    if height < 160:
        print("You cannot ride this one! go to the next ride")
        coaster2()
    else:
        print("Time to buckle up and pls do not puke on the ride!!")
        coaster2()


def age_price():
    age = int(input("How old are you?\n"))
    if age < 5:
        ticket_price = 0
    elif age < 18:
        ticket_price = 10
    else:
        ticket_price = 15
    currency = '€'
    print("The ticket will cost you", ticket_price, currency)

    question = input("Is that allright for you?\n (y/n) \n")
    if question == "n":
        print("Well then fuck off!")
    elif question == "y":
        print("Well then have fun and enjoy the rides!")
        coaster1()
    else:
        print("Well I guess you cannot read!")



print("Welcome to the rollercoaster!")

age_price()





