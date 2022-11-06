# a. calculating the average salary of Managers.

import csv   # importing csv.

file = open(r"employees.csv")   # opening the given csv file to read.

try:                                   # using try statement for further processing the file.
    csv_reader = csv.reader(file)      # using csv_reader to read the csv file.
    total = 0                          # setting variable to calculate the total.
    i = 0                              # setting variable to iterate.
    for column in csv_reader:          # using for-loop to iterate columns in csv file.
        if column[3] == "Manager":     # using if statement to choose Manager in employee type column[column3].
            total += int(column[2])    # adding the salary of Managers in column2.
            i += 1                     # iterating the number of Manager.

    print("The average salary of managers is", int(total / i), "dollars", ".")
            # calculating the average salary by dividing total salary of managers by number of managers.
            # using int to get the given output value.
            # printing the average salary.

finally:
    file.close()    # using finally statement to close file.



# b. finding the staff member with lowest salary.

import csv   # importing csv.

file = open(r"employees.csv")   # opening the given csv file to read.

try:                                                        # using try statement for further processing the file.
    csv_reader = csv.reader(file)                           # using csv_reader to read csv file.
    row = 0                                                 # setting variable for lower bound.
    lowest_value = int(column[2]) + 1                       # setting variable to find the lowest value.
    for column in csv_reader:                               # using for-loop to iterate columns in csv file.
        if row > 0 and int(column[2]) <= lowest_value:      # using if statement to choose salary column[column2].
            lowest_value = int(column[2])                   # using lowest value to find lowest salary in column2.
            staff_member_name = column[0] + " " + column[1]  # adding first_name and last_name columns to get the full name of the staff member
        row += 1                                            # iterating rows to find lowest salary.
    print(staff_member_name, " has the lowest salary $", float(lowest_value), ".")
             # using float to get the given output value.
             # printing the name and the lowest salary of the staff member.


finally:
    file.close()   # using finally statement to close file.
