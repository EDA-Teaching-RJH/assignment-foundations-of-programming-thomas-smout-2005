
def main():
    # Sets parallel lists
    names, ranks, divs, ids = init_database()
    # Asks for name once here, instead of multiple times inside the display_menu function
    user_name = input("What is your full name? ").strip().title()
    # Loop so after each function, user is brought back to the menu
    while True:
        # displays menu for user, so they know they're options
        user_choice = display_menu(user_name)
        # various options for 1 to 9 that link to their respective functions
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
        # if anything other than 1-9 is entered, this is outputted and we loop back round to the menu again
        else:
            print("Invalid input")


def init_database():
    # Our four parallel lists, name, rank, division and id of each member
    names = ["Freeman", "Ransom", "Billups", "Shaxs", "T'Ana", "Marinar"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander", "Ensign"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences", "Command"]
    ids = ["001", "011", "101", "201", "301", "401"]
    
    # returns lists so they can be used globally instead of locally
    return names, ranks, divs, ids


def display_menu(user_name):
    # Menu of options for 1-9
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

    # Says who's currently logged in to interface
    print("Current User Logged In :", user_name)
    # User chooses function they want to run
    user_choice = input("Select Option : ")
    # return answer so response can be linked to function via main function
    return user_choice


def add_member(names, ranks, divs, ids):
    # Takes name and adds it to the list
    new_name = input("Name: ").strip().title()
    names.append(new_name)
    # While true loop to ensure a proper rank is entered
    while True:
        # User enters new members rank
        new_rank = input("Rank: ").strip().title()
        # Check that rank exists and if so, adds it to the list and breaks the loop
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt. Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":
            ranks.append(new_rank)
            break
        # If rank does not exist, this is printed and we loop round to the input rank again
        else:
            print("Invalid rank! Please enter a valid TNG rank")

    # While true loop to ensure a proper division is entered
    while True:
        # User enters new members division
        new_div = input("Division: ").strip().title()
        # Check that division exists and if so, add it to the list and breaks the loop
        if new_div == "Command" or new_div == "Operations" or new_div == "Sciences":
            divs.append(new_div)
            break
        # If division does not exist, this is printed and we loop round to the input division again
        else:
            print("Invalid division! Please enter a valid TNG division")
    
    # While true loop to ensure a unique id is entered
    while True:
        # User enters new members id
        new_id = input("ID : ")
        # check variable is being used to make sure new_id is unique
        check = True
        # for loop checks new_id against every existing id
        for _ in ids:
            # If new_id is not unique, check is changed to false and user is asked to input a different id. break for loop
            if _ == new_id:
                print("Duplicate ID! Enter a different ID")
                check = False
                break
        # if statement checks if 'check' variable is still true. If so, this means the new_id is unique and can be added to the list. break while true loop
        if check == True:
            ids.append(new_id)
            break

    # Print to tell user that the process was successful
    print("Member Added")
    

def remove_member(names, ranks, divs, ids):
    # User inputs id of who they want to remove
    removable_id = input("ID to remove: ").strip()
    # members id is then turned into an index that represents their position in each list
    remove_index = ids.index(removable_id)
    # remove member for each list using their index
    names.pop(remove_index)
    ranks.pop(remove_index)
    divs.pop(remove_index)
    ids.pop(remove_index)
    # Print confirms for the user that removal was successful
    print("Removed Member")


def update_rank(names, ranks, ids):
    # User inputs the id of the member they want ranks changed
    update_id = input("ID to update: ").strip()
    # member's index is worked out so we know their position in each list
    update_index = ids.index(update_id)
    # Letting user know what the member's current rank is
    print(names[update_index], "is currently a", ranks[update_index])
    # While true loop to cycle back to user input, if rank given isn't proper the first time
    while True:
        # user inputs new rank
        new_rank = input("New rank: ").strip().title()
        # checking rank is a proper rank, if so, rank is changed for the existing rank of that member. break while true loop
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt. Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":
            ranks[update_index] = new_rank
            break
        # If new_rank wasn't a proper rank, print this and loop back round to user input
        else:
            print("Invalid rank! Please enter a valid TNG rank")
    # Let user know of the member's new rank
    print(names[update_index], "has been changed to a", ranks[update_index])


def display_roster(names, ranks, divs, ids):
    # print the titles of the lists + formatting
    print("{:<15} {:<15} {:<15} {:<15}".format("Name", "Rank", "Division", "ID"))
    # Just some decorations to help make it easier to read
    print("=== === === === === === === === === === === === ===")
    # for loop to print all members info underneath their respective titles and in line with their other info
    for j in range(len(names)):
        print("{:<15} {:<15} {:<15} {:<15}".format(names[j], ranks[j], divs[j], ids[j]))


def search_crew(names, ranks, divs, ids):
    # User inputs term they want me to find in parallel lists
    term = input("Enter search term : ").strip().title()
    # for loop to check term against all items in all lists
    for k in range(len(names)):
        # if term is found, output the info of the member associated with that term
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
    # User input of which division they want to filter by
    filter = input("Which would you like to filter by; Command, Operations, or Sciences").strip().title()
    # prints info explaining what is about to be output
    print("--> List of crew in", filter)
    # checks division list for all members that match filter and output them
    for i in range(len(divs)):
        if divs[i] == filter:
            print("->", names[i])


def calculate_payroll(ranks):
    # Creates a variable to track current payroll total
    total_payroll = 0
    # Scrolls through ranks list and turns each rank into a value that is added to the total
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
    # returns total
    return total_payroll


def count_officers(ranks):
    # creates total of officers found
    count = 0
    # checks the ranks list for any members than count as officers and if so, increases the count by 1
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count = count + 1
    # return total count
    return count


# runs main code
main()