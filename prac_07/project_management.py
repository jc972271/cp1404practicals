"""
CP1404 - Practical 7
Project Manager
Estimate: 40 minutes
Actual:
"""
from unittest.mock import DEFAULT

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
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

def load_project(filename=DEFAULT_FILE):
    infile = open(filename, "r")
    projects = []
    infile.readline() #remove headings
    for line in infile:
        line = line.strip().split("\t")
        projects.append(line)
    infile.close()
    return projects
main()