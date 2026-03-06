# Here is the module travel.py
def welcome(name):
    return "Welcome to your travel planner, " + name + "!"
    
def recommend_destination(climate, budget):
    if climate == "cold":
        if budget == "low":
            return "We recommend visiting Iceland!"
        elif budget == "medium":
            return "We recommend visiting Hungary!"
        elif budget == "high":
            return "We recommend visiting Norway!"
        else:
            return "Sorry, we don't have a destination for that budget."
    elif climate == "hot":
        if budget == "low":
            return "We recommend visiting Morocco!"
        elif budget == "medium":
            return "We recommend visiting Bali!"
        elif budget == "high":
            return "We recommend visiting the Maldives!"
        else:
            return "Sorry, we don't have a destination for that budget."
    else:
        return "Sorry, we don't have a destination for that climate."
            
def recommend_activities(days):
    if days < 4:
        return "Your " + str(days) + " day trip should include: sightseeing and local food tours."
    elif days < 7:
        return "Your " + str(days) + " day trip should include: hiking, touring historical sites, and reading in local cafes."
    else:
        return "Your " + str(days) + " day trip should include: taking local cooking classes, attending festivals, and taking up photography."
    
def sign_off():
    return "Have a great trip!"


import travel

def travel_planner(name):
    climate = input("What climate would you like? (hot/cold) ").lower()
    while climate == "" or (climate != "hot" and climate != "cold"):
        climate = input("Please enter a valid climate (hot/cold): ").lower()
    
    budget = input("What is your budget? (low/medium/high) ").lower()
    while budget == "" or (budget != "low" and budget != "medium" and budget != "high"):
        budget = input("Please enter a valid budget (low/medium/high): ").lower()
    
    days = input("How long will you stay? ")
    while days == "" or int(days) < 1:
        days = input("Please enter a valid number of days: ")
    days = int(days)

    print()
    print(travel.welcome(name))
    print(travel.recommend_destination(climate, budget))
    print(travel.recommend_activities(days))
    print(travel.sign_off())

name = str(input("What is your name? "))
while name == "":
    name = str(input("Please enter a name: "))

travel_planner(name)
