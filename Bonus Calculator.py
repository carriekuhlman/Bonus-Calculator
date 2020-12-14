"""Bonus calculator to calculate appropriate bonuses for techs and dispatchers at the end of the year based on weekly client hours."""

current_techs = ("Anthony", "Chad", "Christian", "Erika", "Haik", "Karl", "Luke", "Morgan")
current_dispatch = ("Bill", "Shane") 
tech_team = {}
dispatch_team = {}
tech_hours = {}
payout = {}

def populate_dictionaries(techs, dispatch):
    """Populates the tech, dispatch, and payout dictionaries"""
    for tech in techs: 
        tech_team[tech] = 0
        payout[tech] = 0
    for employee in dispatch: 
        dispatch_team[employee] = 0
        payout[employee] = 0

def weekly_tech_hours(techs):
    """Takes an input of hours for each tech and populates a weekly resetting dictionary. Used for calculating weekly payouts for techs and dispatch"""

    target_hr_counter = 0 #counter used to determine if more than half of techs reached target of 33 hours per week
    for tech in techs:
        tech_hours[tech] = 0 #reset weekly tech hours to 0
    print("How many client hours did each tech have during this period?")
    for tech in techs: 
        print(f"{tech}:")
        hours = int(input("> "))
        tech_hours[tech] += hours #add tech hours to dict

    #print the tech hours for review. adjust as needed. 
    while True: 
        print()
        print("Review the amounts:")
        print()
        for tech in techs: 
            print(f"{tech}: {tech_hours[tech]} hours")
        print()
        print("Are the amounts correct? Y or N")
        answer = input("> ").upper()

        if answer == "Y":
            print()
            print("Perfect! Thanks for confirming.")
            break
    
        elif answer == "N":
            while True: 
                print()
                print("Enter the name of the tech which needs to be corrected.\nEnter exit if done.")
                name_to_correct = input("> ").title()
                if name_to_correct in techs:
                    print(f"How many client hours did {name_to_correct} have this week?")
                    corrected_hours = int(input("> "))
                    tech_hours[name_to_correct] = corrected_hours
                elif name_to_correct == "Exit":
                    break
                else:
                    print("That is not a valid option.")
                    print()

        else:
            print("That is not a valid option.")
    
    #review tech's hours and increment tech's weekly running count by 1 if they have 33 hours or more. employee payout is increased by $25 for getting at least 33 hours in the week
    for tech in techs: 
        if tech_hours[tech] >= 33: 
            tech_team[tech] += 1
            target_hr_counter += 1
            payout[tech] += 25

    return target_hr_counter

def dispatch_payout(): 
    """Uses collected weekly employee hours to determine if dispatch scheduled out work evenly amongst techs. If half the techs or more acheived 33 hours or more in the week, dispatch employees' weekly running counts are increased by 1 and employee payout is increased by $25"""

    hour_count = weekly_tech_hours(current_techs)
    for employee in dispatch_team: 
        if hour_count >= len(current_techs) / 2: 
            dispatch_team[employee] += 1
            payout[employee] += 25
    another_week()

def streak_check(): 
    """Reviews counts in tech and dispatch dictionaries. These are the counts to determine how many 33+ hour weeks there have been for each tech, and how many weeks dispatch scheduled at least half of the techs out at 33+ hour weeks. Payout for each employee is increased depending on values in the tech and dispatch dictionaries."""

    for tech in tech_team: 
        if tech_team[tech] >= 40:
            payout[tech] += 2000
        elif tech_team[tech] >= 30:
            payout[tech] += 1250
        elif tech_team[tech] >= 20:
            payout[tech] += 750
        elif tech_team[tech] >= 10: 
            payout[tech] += 250

    for employee in dispatch_team: 
        if dispatch_team[employee] >= 40:
            payout[employee] += 2000
        elif dispatch_team[employee] >= 30:
            payout[employee] += 1250
        elif dispatch_team[employee] >= 20:
            payout[employee] += 750
        elif dispatch_team[employee] >= 10: 
            payout[employee] += 250

def another_week():
    """Asks user whether or not they have more data (weeks) to enter. If done, prints final payout amounts alphabetically."""

    while True: 
        print("Do you have another week of data to enter?\nY or N")
        answer = input("> ").upper()
        print()

        if answer == "Y":
            dispatch_payout()
            break

        #populate employees to a list to sort alphabetically   
        elif answer == "N":
            streak_check()
            final_payout = []
            for employee in payout: 
                final_payout.append(employee)
            sorted_payout = sorted(final_payout)
            print("Here are the payout amounts.")
            print()
            for employee in sorted_payout: 
                print(f"{employee}: ${payout[employee]}")
            print()
            break
        
        else: 
            print("That is not a valid option.")

def bonus_calculator():
    """Starts the bonus calculator. Populates dictionaries and runs through calculator functions."""
    print()
    print("Welcome to the Sirinc end-of-year bonus calculator!")
    print()
    populate_dictionaries(current_techs, current_dispatch)
    dispatch_payout()

bonus_calculator()

#create tech tuple 
#create dispatch tuple
#create weekly target hr couter
#create tech dict
#create dispatch dict
#create payout dict

#create function to populate tech dict with names from tech tuple and dispatch ditc from dispatch tuple

#create function to ask for weekly hours
#ask for weekly hours for each tech
#if hours greater than or equal to 33:
#increment dict value of tech by 1
#increment weekly 33hr counter by 1
#add employee to payout dict and increment value by $25
#ask to review and confirm, adjust as needed

#create function for dispatch team payout
#if counter is greater than or equal to length of tech list divided by 2
#incremenent dict value of dispatch employee by 1
#add dispatch employee to weekly payout dict and increment value by $25

#create function for streak checks
    #check dict for values greater than or equal to 40
    #increment employee weekly payout by $1000

    #check dict for values greater than or equal to 30
    #increment employee weekly payout by $750

    #check dict for values greater than or equal to 20
    #increment employee weekly payout by $500

    #check dict for values greater than or equal to 10
    #increment employee weekly payout by $250

#create a function to print out names and payout amounts

#create a function to ask if more weeks need to be added
#if yes, go back through weekly input
#if not, print out payout amounts alphabetized 