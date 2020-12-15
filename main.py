# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# BBicksler,12.14.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as IO
else:
    raise Exception('This file was not imported')
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lstFile = FP.read_data_from_file('EmployeeData.txt')
lstTable = []
for line in lstFile:
    lstTable.append(EMP(line[0].strip(), line[1].strip(), line[2].strip()))
# Show user a menu of options
while(True):
    try:
        IO.print_menu_items()
# Get user's menu option choice
        option = IO.input_menu_options()
    # Show user current data in the list of employee objects
        if option == '1':
            IO.print_current_list_items(lstTable)
    # Let user add data to the list of employee objects
        elif option == '2':
            lstTable.append(IO.input_employee_data())
    # let user save current data to file
        elif option == '3':
            FP.save_data_to_file('EmployeeData.txt',lstTable)
    # Let user exit program
        elif option == '4':
            print('Thanks, goodbye')
            break

        else:
            print('Please enter a valid choice.')

    except ValueError as e:
        print(e)
# Main Body of Script  ---------------------------------------------------- #
