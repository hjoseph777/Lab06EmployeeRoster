"""
Automated Test Cases for Employee Roster Manager
This script documents all the test scenarios mentioned in the lab instructions.

Run this after implementing the main program to verify all functionality works correctly.
"""

TEST_SCENARIOS = """
=== EMPLOYEE ROSTER MANAGER - TEST SCENARIOS ===

Test Case 1: Add Department "Sales" with 2 Employees
Expected: File data/employees_sales.txt created with 2 lines
Steps:
1. Run program
2. Choose option 1 (Add New Department)
3. Enter department name: Sales
4. Enter number of employees: 2
5. Employee 1: John, Doe, E001, Senior
6. Employee 2: Jane, Smith, E002, Middle
7. Verify success message
8. Check that data/employees_sales.txt exists with correct content

Test Case 2: View Non-existent Department "IT"
Expected: Error message → prompt to retry or quit
Steps:
1. Choose option 2 (View Existing Department)
2. Enter department name: IT
3. Should show "Department 'IT' not found!"
4. When asked "Try another department? (y/n)", test both y and n options

Test Case 3: Invalid Seniority Level
Expected: Re-prompt until valid input
Steps:
1. Start adding a department
2. When prompted for seniority, enter "Intern" (invalid)
3. Should re-prompt with valid options
4. Enter valid seniority like "Entry" or "1"

Test Case 4: Non-numeric Employee Count
Expected: Re-prompt until valid number
Steps:
1. Start adding a department  
2. When asked "How many employees", enter "abc"
3. Should show error and re-prompt
4. Enter valid number like "1"

Test Case 5: Add Department That Already Exists  
Expected: Reject gracefully, no overwrite
Steps:
1. Add department "Sales" (if not already done)
2. Try to add "Sales" again
3. Should show error: "Department 'Sales' already exists!"
4. Return to main menu without overwriting

Test Case 6: Exit Program Cleanly
Expected: Program terminates gracefully
Steps:
1. Choose option 3 (Exit Program)
2. Should show goodbye message
3. Program should terminate without errors

Test Case 7: Invalid Menu Choice
Expected: Error message, stay in menu
Steps:
1. From main menu, enter "4" or "abc"
2. Should show "Invalid choice! Please enter 1, 2, or 3."
3. Menu should redisplay

Test Case 8: Empty Input Handling
Expected: Appropriate error messages for all empty inputs
Steps:
1. Try empty department name
2. Try empty first name, last name, employee ID
3. Try empty seniority choice
4. All should show appropriate error messages and re-prompt

Test Case 9: View Successfully Created Department
Expected: Proper formatted display of employee roster
Steps:
1. Add a department with employees (if not done)
2. View that same department
3. Should show formatted roster with employee count

Test Case 10: Special Characters in Department Names
Expected: Safe filename generation
Steps:  
1. Try department name with spaces: "Human Resources"
2. Should create file: employees_human_resources.txt
3. Should work for viewing as well

AUTOMATION NOTES:
- Run each test case manually and document results
- Take screenshots showing successful completion
- Note any edge cases discovered during testing
- Verify all files are created in the correct data/ directory
"""

def run_interactive_test():
    """
    Interactive test helper - guides through manual testing process.
    """
    print("🧪 EMPLOYEE ROSTER MANAGER - INTERACTIVE TEST GUIDE")
    print("="*60)
    print("This will guide you through testing each scenario.")
    print("Have your Employee Roster program ready to run!")
    print()
    
    test_cases = [
        "Add Department 'Sales' with 2 Employees",
        "View Non-existent Department 'IT'", 
        "Invalid Seniority Level Input",
        "Non-numeric Employee Count Input",
        "Add Duplicate Department Name",
        "Exit Program Cleanly",
        "Invalid Menu Choice",
        "Empty Input Handling",
        "View Successfully Created Department",
        "Special Characters in Department Names"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        input(f"\nPress Enter to run Test Case {i}: {test_case}...")
        print(f"✅ Now execute: {test_case}")
        print("   (Follow the detailed steps in the TEST_SCENARIOS section above)")
        
        result = input("Did this test case pass? (y/n): ").strip().lower()
        if result == 'y':
            print(f"   ✅ Test Case {i}: PASSED")
        else:
            print(f"   ❌ Test Case {i}: FAILED")
            issue = input("   What was the issue? ").strip()
            print(f"   Issue noted: {issue}")
    
    print("\n🎉 All test cases completed!")
    print("   Remember to take screenshots for your submission.")

if __name__ == "__main__":
    print(TEST_SCENARIOS)
    print("\n" + "="*60)
    
    choice = input("Run interactive test guide? (y/n): ").strip().lower()
    if choice == 'y':
        run_interactive_test()
    else:
        print("Review the TEST_SCENARIOS above and test manually.")