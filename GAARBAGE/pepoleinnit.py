import csv
import pandas as pd
import random

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

for name , person in persons.items():
    for day in person.work_days:
        df.at[name, day] = "workn"

print(df)

refrencedays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#mtn = ['MD','E4','A', 'A', 'A', 'E', 'E','E', 'E', 'E','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M']
dayno =  [x for x in range(1, 32)]

# Create DataFrame with None values
df2 = pd.DataFrame( columns=dayno)#index=mtn,
df2 = df2.fillna("OFF")

level4s =[]
doghands = []

for name , person in persons.items():
    if person.level == 4:
        level4s.append(name)
    if person.dog == True:
        doghands.append(name)



def get_week_day(daynum):
    weekday = refrencedays[(daynum-1)]
    return weekday

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


def fill_day(wkday):
    # get working, get working dogs, fill dog, get lvl  4s fill egleise 4, check if person has worked andisite
    # fill andisite,  check egleise , fill egleise, fill the rest on main, check for lvel 4s on main
    #wkday = get_week_day(column)

    working = getworkingroster(wkday)
    workingdogs = getworkingdogs(working)
    dog_hand = random.choice(workingdogs)
    print(dog_hand, wkday)
    df.at[dog_hand,wkday] = "doggo"



fill_day('Saturday')

#df2 = df.fillna("OFF")

#df2.at[3,"MD"] = "dogo"
#print(df.iloc[4])
row_name = df.index[3]  # Get the index name of the fourth row
row = df.loc[row_name]
print(row_name,list(row))


df.at['Gayton', [3]] = "doggo"
