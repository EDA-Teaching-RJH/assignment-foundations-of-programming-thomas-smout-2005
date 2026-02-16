
def main():
    names, ranks, divs, ids = init_database()
    user_name = input("What is your full name? ").strip().title()
    while True:
        user_choice = display_menu(user_name)
        if user_choice == "1":
            add_member(names, ranks, divs, ids)
        elif user_choice == "2":
            remove_member(names, ranks, divs, ids)
        elif user_choice == "3":
            update_rank(names, ranks, ids)
        elif user_choice == "4":
            display_roster(names, ranks, divs, ids)
        elif user_choice == "5":
            search_crew(names, ranks, divs, ids)
        elif user_choice == "6":
            filter_by_division(names, divs)
        elif user_choice == "7":
            print("--> The current payroll comes out to around", calculate_payroll(ranks), "latinum")
        elif user_choice == "8":
            print("--> There are currently", count_officers(ranks), "officers on deck")
        elif user_choice == "9":
            break
        else:
            print("Invalid input")


def init_database():
    names = ["Freeman", "Ransom", "Billups", "Shaxs", "T'Ana", "Marinar"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander", "Ensign"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences", "Command"]
    ids = ["001", "011", "101", "201", "301", "401"]

    return names, ranks, divs, ids


def display_menu(user_name):
    print("--- Menu ---")
    print("1. Add Crew")
    print("2. Remove Crew")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search for Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Log Out")
    print("--- ---- ---")

    print("Current User Logged In :", user_name)
    user_choice = input("Select Option : ")
    return user_choice


def add_member(names, ranks, divs, ids):
    new_name = input("Name: ").strip().title()
    names.append(new_name)
    while True:
        new_rank = input("Rank: ").strip().title()
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt. Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":
            ranks.append(new_rank)
            break
        else:
            print("Invalid rank! Please enter a valid TNG rank")

    while True:
        new_div = input("Division: ").strip().title()
        if new_div == "Command" or new_div == "Operations" or new_div == "Sciences":
            divs.append(new_div)
            break
        else:
            print("Invalid division! Please enter a valid TNG division")
    
    while True:
        new_id = input("ID : ")
        check = True
        for _ in ids:
            if _ == new_id:
                print("Duplicate ID! Enter a different ID")
                check = False
                break
        if check == True:
            ids.append(new_id)
            break

    print("Member Added")
    

def remove_member(names, ranks, divs, ids):
    removable_id = input("ID to remove: ").strip()
    remove_index = ids.index(removable_id)
    names.pop(remove_index)
    ranks.pop(remove_index)
    divs.pop(remove_index)
    ids.pop(remove_index)
    print("Removed Member")


def update_rank(names, ranks, ids):
    update_id = input("ID to update: ").strip()
    update_index = ids.index(update_id)
    print(names[update_index], "is currently a", ranks[update_index])
    while True:
        new_rank = input("New rank: ").strip().title()
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt. Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":
            ranks[update_index] = new_rank
            break
        else:
            print("Invalid rank! Please enter a valid TNG rank")
    print(names[update_index], "has been changed to a", ranks[update_index])


def display_roster(names, ranks, divs, ids):
    print("{:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
    print("=== === === === === === === === === === === === ===")
    for j in range(len(names)):
        print("{:<15} {:<15} {:<15} {:<15}".format(names[j], ranks[j], divs[j], ids[j]))


def search_crew(names, ranks, divs, ids):
    term = input("Enter search term : ").strip().title()
    for k in range(len(names)):
        if names[k] == term:
            print("--> Term found!")
            print("--> {:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
            print("--> === === === === === === === === === === === === ===")
            print("--> {:<15} {:<15} {:<15} {:<15}".format(names[k], ranks[k], divs[k], ids[k]))
        elif ranks[k] == term:
            print("--> Term found!")
            print("--> {:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
            print("--> === === === === === === === === === === === === ===")
            print("--> {:<15} {:<15} {:<15} {:<15}".format(names[k], ranks[k], divs[k], ids[k]))
        elif divs[k] == term:
            print("--> Term found!")
            print("--> {:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
            print("--> === === === === === === === === === === === === ===")
            print("--> {:<15} {:<15} {:<15} {:<15}".format(names[k], ranks[k], divs[k], ids[k]))
        elif ids[k] == term:
            print("--> Term found!")
            print("--> {:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
            print("--> === === === === === === === === === === === === ===")
            print("--> {:<15} {:<15} {:<15} {:<15}".format(names[k], ranks[k], divs[k], ids[k]))


def filter_by_division(names, divs):
    filter = input("Which would you like to filter by; Command, Operations, or Sciences").strip().title()
    print("--> List of crew in", filter)
    for i in range(len(divs)):
        if divs[i] == filter:
            print("->", names[i])


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


main()