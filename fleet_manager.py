names = ["Freeman", "Ransom", "Billups", "Shaxs", "T'ana", "Marinar"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander", "Ensign"]
divs = ["Command", "Command", "Operations", "Operations", "Sciences", "Command"]
ids = ["001", "011", "101", "201", "301", "401"]

"""

def main():


def init_database():


def display_menu():


def add_member(names, ranks, divs, ids):


def remove_member(names, ranks, divs, ids):


def update_rank(names, ranks, ids):

"""


def display_roster():
    print("{:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
    print("=== === === === === === === === === === === === ===")
    for j in range(len(names)):
        print("{:<15} {:<15} {:<15} {:<15}".format(names[j], ranks[j], divs[j], ids[j]))


def search_crew(names, ranks, divs, ids):


"""

def filter_by_division():
    filter = input("Which would you like to filter by; Command, Operations, or Sciences").lower().title()
    for i in range(len(divs)):
        if divs[i] == filter:
            print(names[i])


def calculate_payroll():
    total_payroll = 0
    for _ in ranks:
        if _ == "Captain":
            total_payroll = total_payroll + 1000
        elif _ == "Commander":
            total_payroll = total_payroll + 800
        elif _ == "Lt. Commander":
            total_payroll = total_payroll + 600
        elif _ == "Lieutenant" or _ == "Doctor":
            total_payroll = total_payroll + 500
        elif _ == "Ensign":
            total_payroll = total_payroll + 200
    return total_payroll


def count_officers():
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count = count + 1
    return count

"""

