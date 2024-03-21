import csv

# To Register
def register():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")
    email = input("Enter email: ")
    password = input('Enter password: ')
    row = [first_name, second_name, email, password]
    with open("userRegistration.csv", 'a') as users:
        # creating a csv writer object
        csvwriter = csv.writer(users)

        # writing new row 
        csvwriter.writerow(row)

# To Login
def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    logged_in=False
    with open("userRegistration.csv") as users:
        # read the csv file
        csvFile =  csv.reader(users)

        # Get file content
        for lines in csvFile:
            if email == lines[2] and password == lines[3]:
                logged_in = True
        if logged_in:
            print("Yaay! You are logged in!")
        else: 
            print("Please register to continue!")            


# Main
def intro():
    print("------------------------------------")
    print("Welcome To The Store Manangement App")
    print("------------------------------------")
    print("Enter: ")
    print("1 to Register")
    print("2 to Login")
    print("0 to Exit")

    choice = int(input())
    new_loop = True

    while new_loop:
        if choice == 1:
            print('Register')
            register()
            break
        elif choice == 2:
            print("Login")  
            login()
            break  
        else:
            new_loop=False


intro()