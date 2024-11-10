"""
CP1404 - Practical 7
Project Manager
Estimate: 40 minutes
Actual:
"""

import datetime
from project import Project
from operator import itemgetter

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_project()
    print(f"{len(projects)} projects loaded from {DEFAULT_FILE}")
    print(MENU)
    choice = input(">>> ").upper()
    print(choice)
    while choice != "Q":
        if choice == "L":
            print("Load Project")
            filename = input("Filename: ")
            load_project(filename)
        elif choice == "S":
            print("Save Project")
            filename = input("Filename: ")
            save_project(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def update_project(projects):
    """Allows user to update the completion and priority of a project."""
    for index, project in enumerate(projects, 1):
        print(f"{index}: {project}")
    is_done = False
    while not is_done:
        try:
            chosen_id = int(input("Enter Project ID: "))
        except ValueError:
            print("Please Enter an Integer")
        if 0 < chosen_id < len(projects) + 1:
            is_done = True
        else:
            print("Please chose a valid ID")
    chosen_id -= 1  # corrects ID to start from 0
    print(f"You are editing:\n{projects[chosen_id]}")
    print("Leave blank to keep current values")
    new_priority = input("New Priority: ")
    new_completion = input("Completion: ")
    if new_priority != "":
        projects[chosen_id].priority = int(new_priority)
    if new_completion != "":
        projects[chosen_id].completion = int(new_completion)


def add_project(projects):
    """Allows user to add new project"""
    is_done = False
    while not is_done:
        try:
            name = input("Project Name: ")
            date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            priority = int(input("Project Priority: "))
            cost = float(input("Project Cost: "))
            is_done = True
        except ValueError:
            print("Please enter the correct data type")
    new_project = Project(name, date, priority, cost, 0)  # while loop ensures value
    print(f"Added: {new_project}")
    projects.append(new_project)


def filter_by_date(projects):
    """Filters projects by a user chosen date."""
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    date_filtered_projects = [project for project in projects if project.date_filter(date)]
    for project in date_filtered_projects:
        print(project)


def display_projects(projects):
    """Display projects and whether they are complete or incomplete"""
    not_complete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("Incomplete projects: ")
    for project in sorted(not_complete):
        print(f"\t{project}")
    print("Complete projects: ")
    for project in sorted(complete):
        print(f"\t{project}")


def load_project(filename=DEFAULT_FILE):
    """Load .txt file and convert into list of Project objects"""
    infile = open(filename, "r")
    projects = []
    infile.readline()  # remove headings
    for line in infile:
        line = line.strip().split("\t")
        # 0=name, 1=start_date 2=priority 3=cost 4=completion %
        project = Project(line[0], datetime.datetime.strptime(line[1], "%d/%m/%Y").date(), int(line[2]), float(line[3]),
                          int(line[4]))
        projects.append(project)
    infile.close()
    return projects


def save_project(projects, filename=DEFAULT_FILE):
    """Load .txt file and convert into list of Project objects"""
    outfile = open(filename, "w")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
    for project in projects:
        print(repr(project))
    outfile.close()


main()
