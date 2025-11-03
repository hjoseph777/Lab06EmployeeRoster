# Employee Roster Manager - Test Output Demo

This document shows real-time output from automated testing of the Employee Roster Manager program.

## Test Results Summary

- **Tests Passed:** 8/8
- **Success Rate:** 100.0%

## Detailed Test Output

### Test 1: Add Department 'Sales' with 2 Employees

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: How many employees would you like to add? 
Adding 2 employee(s) to Sales:

--- Employee 1 ---
First name: Last name: Employee ID: 
Available Seniority Levels:
   1. Entry
   2. Junior
   3. Middle
   4. Senior
   5. Management
   6. Executive

Enter seniority level (name or number): 
--- Employee 2 ---
First name: Last name: Employee ID: 
Available Seniority Levels:
   1. Entry
   2. Junior
   3. Middle
   4. Senior
   5. Management
   6. Executive

Enter seniority level (name or number): 
Success! Created 'Sales' department with 2 employee(s).
Data saved to: data/employees_sales.txt

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 2: View Existing Department 'Sales'

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== View Department Roster ===
Enter department name to view: 
Employee Roster for 'Sales':
============================================================
    1. John – Doe – E001 – Senior
    2. Jane – Smith – E002 – Middle
============================================================
   Total employees: 2

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 3: View Non-existent Department 'IT'

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== View Department Roster ===
Enter department name to view: Error: Department 'IT' not found!
   Try another department? (y/n):    Returning to main menu...

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 4: Invalid Seniority Input Test

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: How many employees would you like to add? 
Adding 1 employee(s) to Marketing:

--- Employee 1 ---
First name: Last name: Employee ID: 
Available Seniority Levels:
   1. Entry
   2. Junior
   3. Middle
   4. Senior
   5. Management
   6. Executive

Enter seniority level (name or number): 'Intern' isn't a valid seniority level. Please try again.

Enter seniority level (name or number): 
Success! Created 'Marketing' department with 1 employee(s).
Data saved to: data/employees_marketing.txt

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 5: Non-numeric Employee Count Test

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: How many employees would you like to add? That's not a valid number. Try again!
How many employees would you like to add? 
Adding 2 employee(s) to Engineering:

--- Employee 1 ---
First name: Last name: Employee ID: 
Available Seniority Levels:
   1. Entry
   2. Junior
   3. Middle
   4. Senior
   5. Management
   6. Executive

Enter seniority level (name or number): 
--- Employee 2 ---
First name: Last name: Employee ID: 
Available Seniority Levels:
   1. Entry
   2. Junior
   3. Middle
   4. Senior
   5. Management
   6. Executive

Enter seniority level (name or number): 
Success! Created 'Engineering' department with 2 employee(s).
Data saved to: data/employees_engineering.txt

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 6: Add Duplicate Department Test

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: Error: Department 'Sales' already exists!
   Choose a different name or use 'View Department' to see existing data.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 7: Invalid Menu Choice Test

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```

### Test 8: Empty Input Handling Test

**Program Output:**
```
Welcome to the Employee Roster Manager!
Your one-stop shop for department employee tracking

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: Department name can't be empty!

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
=== Add New Department ===
Enter department name: Department name can't be empty!

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): Invalid choice! Please enter 1, 2, or 3.

==================================================
EMPLOYEE ROSTER MANAGER
==================================================
1. Add New Department
2. View Existing Department
3. Exit Program
--------------------------------------------------
Choose an option (1-3): 
Thanks for using Employee Roster Manager!
Have a great day!
```


## Key Features Demonstrated

1. **Input Validation**: All invalid inputs are handled gracefully with clear error messages
2. **File I/O**: Department data is properly saved and loaded from text files
3. **Error Handling**: Missing files and permission errors are caught and handled
4. **User Experience**: Clear menus and helpful prompts guide the user
5. **Data Integrity**: Duplicate departments are prevented to maintain data consistency

## File Structure After Testing

The following files are created in the `data/` directory:
- [`employees_sales.txt`](data/employees_sales.txt) - Sales department roster
- [`employees_marketing.txt`](data/employees_marketing.txt) - Marketing department roster  
- [`employees_engineering.txt`](data/employees_engineering.txt) - Engineering department roster

Each file contains employee data in the format:
```
FirstName – LastName – EmployeeID – SeniorityLevel
```

This automated testing ensures all functionality works correctly and handles edge cases appropriately.
