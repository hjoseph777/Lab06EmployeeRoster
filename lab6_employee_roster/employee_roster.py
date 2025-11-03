"""
Employee Roster Management System
A menu-driven program for managing department-based employee rosters.

This program demonstrates file I/O, error handling, and modular programming 
concepts through a practical employee management system.
"""

import os

def get_valid_integer(prompt, min_val=1):
    """
    Prompts user for a valid integer input >= min_val.
    Keeps asking until they give us someting that actually works!
    
    Args:
        prompt (str): The message to show the user
        min_val (int): Minimum acceptable value (default: 1)
    
    Returns:
        int: Valid integer >= min_val
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:  # Handle empty input gracefully
                print("Please enter a number, don't leave it blank.")
                continue
                
            value = int(user_input)
            if value < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            return value
        except ValueError:
            print("That's not a valid number. Try again!")

def get_valid_seniority():
    """
    Gets a valid seniority level from the user.
    Shows all options and accepts case-insensitive input - pretty forgiving!
    
    Returns:
        str: Properly capitalized seniority level
    """
    valid_levels = ["Entry", "Junior", "Middle", "Senior", "Management", "Executive"]
    
    print("\nAvailable Seniority Levels:")
    for i, level in enumerate(valid_levels, 1):
        print(f"   {i}. {level}")
    
    while True:
        choice = input("\nEnter seniority level (name or number): ").strip()
        
        if not choice:
            print("Please enter something! Can't leave this blank.")
            continue
            
        # Try to match by number first
        try:
            num_choice = int(choice)
            if 1 <= num_choice <= len(valid_levels):
                return valid_levels[num_choice - 1]
            else:
                print(f"Number must be between 1 and {len(valid_levels)}.")
                continue
        except ValueError:
            # Not a number, try text matching
            choice_lower = choice.lower()
            for level in valid_levels:
                if level.lower() == choice_lower:
                    return level
            
            print(f"'{choice}' isn't a valid seniority level. Please try again.")

def build_filename(dept_name):
    """
    Builds a safe filename from a department name.
    Handles spaces and special characters so we don't break the filesystem.
    
    Args:
        dept_name (str): The department name (e.g., "Human Resources")
    
    Returns:
        str: Safe filename (e.g., "data/employees_human_resources.txt")
    """
    # Make it lowercase and replace spaces with underscores for safety
    safe_name = dept_name.lower().replace(" ", "_")
    # Remove any other potentially problematic characters
    safe_name = "".join(c for c in safe_name if c.isalnum() or c == "_")
    return f"data/employees_{safe_name}.txt"

def add_department():
    """
    Creates a new department with employee data.
    Won't overwrite existing departments - gotta keep that data safe!
    """
    print("\n=== Add New Department ===")
    
    # Get department name and check if it already exists
    dept_name = input("Enter department name: ").strip()
    if not dept_name:
        print("Department name can't be empty!")
        return
    
    filename = build_filename(dept_name)
    if os.path.exists(filename):
        print(f"Error: Department '{dept_name}' already exists!")
        print("   Choose a different name or use 'View Department' to see existing data.")
        return
    
    # Get number of employees to add
    num_employees = get_valid_integer("How many employees would you like to add? ")
    
    employees = []
    print(f"\nAdding {num_employees} employee(s) to {dept_name}:")
    
    # Collect employee data
    for i in range(1, num_employees + 1):
        print(f"\n--- Employee {i} ---")
        
        # Get first name (required)
        while True:
            first_name = input("First name: ").strip()
            if first_name:
                break
            print("First name can't be empty!")
        
        # Get last name (required) 
        while True:
            last_name = input("Last name: ").strip()
            if last_name:
                break
            print("Last name can't be empty!")
        
        # Get employee ID (required)
        while True:
            emp_id = input("Employee ID: ").strip()
            if emp_id:
                break
            print("Employee ID can't be empty!")
        
        # Get seniority level
        seniority = get_valid_seniority()
        
        # Store employee data
        # Format: FirstName,LastName,EmployeeID,SeniorityLevel
        employee_line = f"{first_name},{last_name},{emp_id},{seniority}"
        employees.append(employee_line)
    
    # Save to file
    try:
        with open(filename, 'w') as f:
            for employee in employees:
                f.write(employee + "\n")
        
        print(f"\nSuccess! Created '{dept_name}' department with {num_employees} employee(s).")
        print(f"Data saved to: {filename}")
        
    except PermissionError:
        print(f"Error: Permission denied! Can't write to {filename}")
    except Exception as e:
        print(f"Error: Unexpected error saving file: {e}")

def view_department():
    """
    Displays the employee roster for an existing department.
    Handles missing files gracfully and offers retry options.
    """
    print("\n=== View Department Roster ===")
    
    while True:  # Allow retries if department not found
        dept_name = input("Enter department name to view: ").strip()
        if not dept_name:
            print("Please enter a department name!")
            continue
        
        filename = build_filename(dept_name)
        
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            # Display the roster with nice formatting
            print(f"\nEmployee Roster for '{dept_name.title()}':")
            print("=" * 60)
            
            if not lines:
                print("   (No employees found in this department)")
            else:
                for i, line in enumerate(lines, 1):
                    employee_info = line.strip()
                    if employee_info:  # Skip empty lines
                        print(f"   {i:2d}. {employee_info}")
            
            print("=" * 60)
            print(f"   Total employees: {len([l for l in lines if l.strip()])}")
            break  # Successfully displayed, exit the retry loop
            
        except FileNotFoundError:
            print(f"Error: Department '{dept_name}' not found!")
            retry = input("   Try another department? (y/n): ").strip().lower()
            if retry not in ['y', 'yes']:
                print("   Returning to main menu...")
                break
        except PermissionError:
            print(f"Error: Permission denied reading {filename}")
            break
        except Exception as e:
            print(f"Error: Unexpected error reading file: {e}")
            break

def main():
    """
    Main program loop with menu system.
    Keeps running until the user decides to quit - nice and simple!
    """
    # Make sure our data directory exists before we start
    os.makedirs("data", exist_ok=True)
    
    print("Welcome to the Employee Roster Manager!")
    print("Your one-stop shop for department employee tracking")
    
    while True:
        # Display the main menu with a bit of style
        print("\n" + "="*50)
        print("EMPLOYEE ROSTER MANAGER")
        print("="*50)
        print("1. Add New Department")
        print("2. View Existing Department") 
        print("3. Exit Program")
        print("-"*50)
        
        try:
            choice = input("Choose an option (1-3): ").strip()
            
            if choice == '1':
                add_department()
            elif choice == '2':
                view_department()
            elif choice == '3':
                print("\nThanks for using Employee Roster Manager!")
                print("Have a great day!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("The program will continue, but you might want to restart.")

if __name__ == "__main__":
    main()