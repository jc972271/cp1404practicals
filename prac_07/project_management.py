"""
CP1404 - Practical 7
Project Manager
Estimate: 40 minutes
Actual:
"""

import datetime
from project import Project

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
            filename = input("Filename:")
            load_project(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def display_projects(projects):
    """Display projects and whether they are complete or incomplete"""
    not_complete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("Incomplete projects: ")
    for project in not_complete:
        print(f"\t{project}")
    print("Complete projects: ")
    for project in complete:
        print(f"\t{project}")


def load_project(filename=DEFAULT_FILE):
    """Load .txt file and convert into list of Project objects"""
    infile = open(filename, "r")
    projects = []
    infile.readline() #remove headings
    for line in infile:
        line = line.strip().split("\t")
        #0=name, 1=start_date 2=priority 3=cost 4=completion %
        project = Project(line[0], datetime.datetime.strptime(line[1], "%d/%m/%Y").date(), int(line[2]), float(line[3]), int(line[4]))
        projects.append(project)
    infile.close()
    return projects
main()