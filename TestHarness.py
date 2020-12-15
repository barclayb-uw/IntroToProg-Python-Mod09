# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBicksler, 12.14.2020 ,Added testing code from listings
# ---------------------------------------------------------- #

# ---------------------------------------------------------- #
# Title: Test of the person class
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBicksler, 12-14-2020, added to TestHarness File
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes

else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
#End Test
# ---------------------------------------------------------- #
# Title: Test the Employee Class
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBicksler, 12-14-2020, added to TestHarness File
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!

else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
#End of Test
# ---------------------------------------------------------- #
# Title: Test the File Processing Class
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBicksler, 12-14-2020, added to TestHarness File
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import ProcessingClasses as P  # processing classes
else:
    raise Exception("This file was not created to be imported")
# End Test #
# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))
#End Test#
# ---------------------------------------------------------- #
# Title: Listing 12
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
#End Test#

