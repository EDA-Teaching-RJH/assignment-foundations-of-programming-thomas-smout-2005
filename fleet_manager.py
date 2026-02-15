
def main():
    names, ranks, divs, ids = init_database()


def init_database():
    names = ["Freeman", "Ransom", "Billups", "Shaxs", "T'Ana", "Marinar"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander", "Ensign"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences", "Command"]
    ids = ["001", "011", "101", "201", "301", "401"]

    return names, ranks, divs, ids


def display_menu():
    user_name = input("What is your full name?").strip().title()

    print("--- Menu ---")
    print("1. Add Crew")
    print("2. Remove Crew")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search for Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("--- ---- ---")

    print("Current User Logged In :", user_name)
    user_choice = input("Select Option : ")
    return user_choice


def add_member(names, ranks, divs, ids):


def remove_member(names, ranks, divs, ids):


def update_rank(names, ranks, ids):


def display_roster(names, ranks, divs, ids):
    print("{:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
    print("=== === === === === === === === === === === === ===")
    for j in range(len(names)):
        print("{:<15} {:<15} {:<15} {:<15}".format(names[j], ranks[j], divs[j], ids[j]))


def search_crew(names, ranks, divs, ids):
    term = input("Enter search term").strip().title()
    for k in range(len(names)):
        if names[k] == term:
            print(names[k])
        elif ranks[k] == term:
            print(names[k])
        elif divs[k] == term:
            print(names[k])
        elif ids[k] == term:
            print(names[k])


def filter_by_division(names, divs):
    filter = input("Which would you like to filter by; Command, Operations, or Sciences").strip().title()
    for i in range(len(divs)):
        if divs[i] == filter:
            print(names[i])


def calculate_payroll(ranks):
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


def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count = count + 1
    return count


