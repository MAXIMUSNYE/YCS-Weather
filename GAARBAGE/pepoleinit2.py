import csv
import pandas as pd
import random
from colorama import Fore, Style


class Person:
    def __init__(self, name, level=None):
        self.name = name
        self.level = level
        self.work_days = []
        self.dog = False

    def add_work_day(self, day):
        if day not in self.work_days:
            self.work_days.append(day)

def initialize_persons_from_csv(file_path, persons, level=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=days_of_week)
        next(reader)  # Skip the header row
        for row in reader:
            for day, name in row.items():
                if name:  # If there's a name for the day
                    if name not in persons:
                        persons[name] = Person(name, level)
                    persons[name].add_work_day(day)

# Initialize persons dictionary
persons = {}

# First CSV
first_csv_path = 'GAARBAGE/Normies.csv'
initialize_persons_from_csv(first_csv_path, persons, level= None)

# Second CSV with level 4
second_csv_path = 'GAARBAGE/lvl4s.csv'
initialize_persons_from_csv(second_csv_path, persons, level=4)

for level_name in ["Boyd", "Stratton", "Gayton", "Fleming", "Eisele"]:
    if level_name in persons:
        persons[level_name].dog = True

# for name, person in persons.items():
#     print(f"{name} (Level {person.level if person.level is not None else 'N/A'}) works on: {', '.join(person.work_days)}-----{person.dog}")







headers = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

names = []
for name, person in persons.items():
    names.append(name)


df = pd.DataFrame(index=names, columns=headers)
df = df.fillna("n")  # Filling all cells with None
multi_columns = pd.MultiIndex.from_tuples([(day, i // 7 + 1) for i, day in enumerate(headers)], names=['Day', 'Week'])

# Set the MultiIndex as the columns of the DataFrame
df.columns = multi_columns

# Fill the DataFrame with 'n' values
df = df.fillna("n")  # Filling all cells with 'n'

#df.loc["Nye", ("Monday", 1)] = "Your Value"

level4s =[]
doghands = []

for name , person in persons.items():
    if person.level == 4:
        level4s.append(name)
    if person.dog == True:
        doghands.append(name)

def isworking(day,person):
    print(persons[person].work_days)
    if day in persons[person].work_days:
        
        return True
    return False


def getworkingroster(day):
    working_roster = []
    for name , person in persons.items():
        if day in persons[name].work_days:
            working_roster.append(name)
    return working_roster

def getworkingdogs(workingpepole):
    werkndogs = []
    for hand in doghands:
        if hand in workingpepole:
            werkndogs.append(hand)
    return werkndogs


def fill_day(wkday,week):
    # get working, get working dogs, fill dog, get lvl  4s fill egleise 4, check if person has worked andisite
    # fill andisite,  check egleise , fill egleise, fill the rest on main, check for lvel 4s on main
    #wkday = get_week_day(column)
    working = getworkingroster(wkday)
    print(working)

    #Dogs
    workingdogs = getworkingdogs(working)
    dog_hand = random.choice(workingdogs)
    working.remove(dog_hand)
    df.at[dog_hand,(wkday,week)] = "doggo"
    print(working)
    #egleise lvl4s
    l4on = []
    for person in working:
        if persons[person].level == 4:
            l4on.append(person)
    E4 = random.choice(l4on)
    working.remove(E4)
    df.at[E4,(wkday,week)] = "EL4"
    print(working)

    #fill egelise
    for i in range(0,5):
        peep = random.choice(working)
        working.remove(peep)
        df.at[peep,(wkday,week)] = "EGL"
    print(working)
    
    #fill andy
    for i in range(0,3):
        peep = random.choice(working)
        working.remove(peep)
        df.at[peep,(wkday,week)] = "AND"
    print(working)
    
    for i in working:
        df.at[i,(wkday,week)] = "PHQ"
    print("\n",working)


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(1,4):
    for day in weekdays:
        fill_day(day,week)

#fill_day(weekdays[5],1)
print(df)

#df.to_csv('GAARBAGE/SchedghTest.csv', index=True)

def dframe():
    return df


# # Create a sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Status': ['Working', 'Not Working', 'Working']}
# df = pd.DataFrame(data)

# Define colors for specific values
# color_mapping = {
#     'PHQ': Fore.GREEN,
#     'EGL': Fore.RED,
# }

# # Apply color to the DataFrame values
# def color_text(value):
#     return f"{color_mapping.get(value, Fore.RESET)}{value}{Style.RESET_ALL}"

# colored_df = df.applymap(color_text)

# # Print the colored DataFrame
# print(colored_df)
