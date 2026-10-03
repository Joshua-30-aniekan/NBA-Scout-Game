import random
print("=================================================")
print("WELCOME TO THE USA-NIGERIA BASKETBALL SCOUT")
print("=================================================")
scout_name = input("Enter your scout name:")
print("Welcome, Scout " + scout_name + "! "+ "Let's explore the USA-Nigeria pipeline")

print("-- STAGE 1: THE TRIVIA CHALLENGE--")
scout_rating = 0
ans1 = input("Which Nigerian basketballer was drafted number 1 overall in 1984 by the Houston Rockets? ").lower()
if ans1 == "hakeem olajuwon":
    print("Correct!")
    scout_rating += 30
else:
    print("Wrong Answer!!!")

ans2 = input("Giannis Antetokounmpo plays for Greece, but his parents immigrated from which country?").lower()
if ans2 == "nigeria":
    print("VERY GOOD.His family name is Adetokunbo.")
    scout_rating += 30
elif ans2 == "south africa":
    print("Incorrect.Common mixup...His family name is Adetokunbo")
else:
    print("Incorrect!!")

if ans1 == "hakeem olajuwon" and ans2 == "nigeria":
    print("                                            ")
    print("                                            ")

    print("--STAGE 2: PHYSICAL PROSPECTS' RATING--")
    print("Enter the physical metrics of your prospective player  ")
    height = int(input("Height in cm: "))
    weight = int(input("Weight in kilograms: "))
    player_ratio = height / weight
    if 1.80 <= player_ratio <= 1.95:
        print("Perfect NBA Build\n You seem to be looking for a strong center?")
        scout_rating += 40
    elif 1.96 <= player_ratio <= 2.15:
        print("Versatile Forward Build! Your prospect has the build to be a Modern wing forward")
        scout_rating += 40
    elif 2.16 <= player_ratio <= 2.35:
        print("Elite Playmaker Build!\nYour prospect has the perfect agility for an NBA Point Guard")
        scout_rating += 40
    elif 2.36 <= player_ratio <= 2.60:
        print("Unicorn Playmaker build. Seem to br looking for a Tall Guard")
    else:
        print(
            "Out of Shape Build!\nYour prospect's physical metrics are highly unbalanced,making them an immediate conditioning project for the NBA G-League")
        scout_rating += 0

    unicorn = ["Chidi Adetokunbo", "Olumide Balogun", "Toci Adeleke", "Femi Oladipo", "Seyi Alabi"]
    wing_forwards = ["Olamide Ade", "Tochukwu Ogennetega", "Ugochukwu Praise", "Aniekan Joshua"]
    six_footers = ["Tunde Okafor", "Emeka Okoye", "Jide Awosika", "Kunle Babatunde", "Chuka Ese"]
    center_builds = ["Chinedu Olajuwon", "Babajide Agbaje", "Ucheci Nwosu", "Damilola Okonkwo", "Ifeanyi Eke"]
    out_of_shape_peeps = ["Obinna Yusuf", "Gboyega Diallo", "Kelechi Amadi", "Taiwo Bello", "Mustapha Udoh"]

    if 1.80 <= player_ratio <= 1.96:
        print("Your player is " + center_builds[random.randint(0, len(center_builds) - 1)])
    elif 2.16 <= player_ratio <= 2.35:
        print("Your player is " + six_footers[random.randint(0, len(six_footers) - 1)])
    elif 2.36 <= player_ratio <= 2.60:
        print("Your player is " + unicorn[random.randint(0, len(unicorn) - 1)])
    elif 1.96 <= player_ratio <= 2.15:
        print("Your player is " + wing_forwards[random.randint(0, len(wing_forwards) - 1)])
    else:
        print("Your prospect lacks the physical structure to play in the NBA. He should spend some time in the G league")

    print(f"Your Scout score is  {scout_rating} out of 100\n 0 to 60 - Average \n 61 to 100 - very good")
    print("Now go and dominate the NBA with your new signing...or play in the G league \U0001F602")

else:
    print("You failed the Trivia Challenge! Try Again \U0001F614")


