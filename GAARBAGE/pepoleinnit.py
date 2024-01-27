import csv

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


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

