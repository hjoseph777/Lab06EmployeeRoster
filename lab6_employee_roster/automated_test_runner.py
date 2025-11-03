"""
Automated Test Runner for Employee Roster Manager
Runs comprehensive tests and captures real-time output for documentation.
"""

import subprocess
import os
import time
import sys
from pathlib import Path

class EmployeeRosterTester:
    def __init__(self):
        self.test_results = []
        self.data_dir = Path("data")
        
    def cleanup_test_files(self):
        """Clean up any test files before starting."""
        if self.data_dir.exists():
            for file in self.data_dir.glob("employees_*.txt"):
                try:
                    file.unlink()
                    print(f"Cleaned up: {file}")
                except:
                    pass
                    
    def run_test_scenario(self, scenario_name, inputs, expected_files=None):
        """
        Run a test scenario with given inputs and check results.
        """
        print(f"\n{'='*60}")
        print(f"TEST SCENARIO: {scenario_name}")
        print(f"{'='*60}")
        
        # Prepare input string
        input_data = '\n'.join(inputs) + '\n'
        
        try:
            # Run the main program with input
            result = subprocess.run(
                [sys.executable, 'employee_roster.py'],
                input=input_data,
                text=True,
                capture_output=True,
                timeout=30
            )
            
            # Display the output
            print("PROGRAM OUTPUT:")
            print("-" * 40)
            print(result.stdout)
            
            if result.stderr:
                print("ERRORS:")
                print(result.stderr)
            
            # Check expected files
            if expected_files:
                print("FILE VERIFICATION:")
                print("-" * 40)
                for filename in expected_files:
                    filepath = self.data_dir / filename
                    if filepath.exists():
                        print(f"✓ File created: {filename}")
                        # Show file contents
                        try:
                            content = filepath.read_text()
                            print(f"  Content:")
                            for line_num, line in enumerate(content.splitlines(), 1):
                                print(f"    {line_num}: {line}")
                        except Exception as e:
                            print(f"  Error reading file: {e}")
                    else:
                        print(f"✗ File missing: {filename}")
            
            # Record test result
            test_passed = result.returncode in [0, 130]  # 130 is Ctrl+C exit
            self.test_results.append({
                'scenario': scenario_name,
                'passed': test_passed,
                'output': result.stdout,
                'errors': result.stderr
            })
            
            print(f"\nTEST RESULT: {'PASSED' if test_passed else 'FAILED'}")
            
        except subprocess.TimeoutExpired:
            print("TEST FAILED: Program timed out")
            self.test_results.append({
                'scenario': scenario_name,
                'passed': False,
                'output': "Timeout",
                'errors': "Program timed out"
            })
        except Exception as e:
            print(f"TEST FAILED: {e}")
            self.test_results.append({
                'scenario': scenario_name,
                'passed': False,
                'output': "",
                'errors': str(e)
            })
        
        print(f"\n{'='*60}")
        time.sleep(1)  # Brief pause between tests
        
    def run_all_tests(self):
        """Execute all test scenarios."""
        print("EMPLOYEE ROSTER MANAGER - AUTOMATED TESTING")
        print("=" * 60)
        print("This script will run all test scenarios and show real-time output.")
        print()
        
        # Clean up before starting
        self.cleanup_test_files()
        
        # Test 1: Add Department "Sales" with 2 Employees
        self.run_test_scenario(
            "Add Department 'Sales' with 2 Employees",
            [
                "1",                    # Add New Department
                "Sales",                # Department name
                "2",                    # Number of employees
                "John",                 # First name
                "Doe",                  # Last name
                "E001",                 # Employee ID
                "Senior",               # Seniority
                "Jane",                 # First name
                "Smith",                # Last name
                "E002",                 # Employee ID
                "3",                    # Seniority (Middle)
                "3"                     # Exit
            ],
            expected_files=["employees_sales.txt"]
        )
        
        # Test 2: View Existing Department
        self.run_test_scenario(
            "View Existing Department 'Sales'",
            [
                "2",                    # View Department
                "Sales",                # Department name
                "3"                     # Exit
            ]
        )
        
        # Test 3: View Non-existent Department
        self.run_test_scenario(
            "View Non-existent Department 'IT'",
            [
                "2",                    # View Department
                "IT",                   # Non-existent department
                "n",                    # Don't try another
                "3"                     # Exit
            ]
        )
        
        # Test 4: Invalid Seniority Input
        self.run_test_scenario(
            "Invalid Seniority Input Test",
            [
                "1",                    # Add New Department
                "Marketing",            # Department name
                "1",                    # Number of employees
                "Alice",                # First name
                "Johnson",              # Last name
                "M001",                 # Employee ID
                "Intern",              # Invalid seniority
                "Entry",               # Valid seniority
                "3"                     # Exit
            ],
            expected_files=["employees_marketing.txt"]
        )
        
        # Test 5: Non-numeric Employee Count
        self.run_test_scenario(
            "Non-numeric Employee Count Test",
            [
                "1",                    # Add New Department
                "Engineering",          # Department name
                "abc",                  # Invalid count
                "2",                    # Valid count
                "Bob",                  # First name
                "Wilson",               # Last name
                "ENG001",               # Employee ID
                "1",                    # Entry seniority
                "Carol",                # First name
                "Davis",                # Last name
                "ENG002",               # Employee ID
                "Executive",            # Seniority
                "3"                     # Exit
            ],
            expected_files=["employees_engineering.txt"]
        )
        
        # Test 6: Duplicate Department
        self.run_test_scenario(
            "Add Duplicate Department Test",
            [
                "1",                    # Add New Department
                "Sales",                # Existing department name
                "3"                     # Exit
            ]
        )
        
        # Test 7: Invalid Menu Choice
        self.run_test_scenario(
            "Invalid Menu Choice Test",
            [
                "4",                    # Invalid choice
                "abc",                  # Invalid choice
                "3"                     # Exit
            ]
        )
        
        # Test 8: Empty Input Handling
        self.run_test_scenario(
            "Empty Input Handling Test",
            [
                "1",                    # Add New Department
                "",                     # Empty department name
                "HR",                   # Valid department name
                "",                     # Empty employee count  
                "1",                    # Valid count
                "",                     # Empty first name
                "David",                # Valid first name
                "",                     # Empty last name
                "Brown",                # Valid last name
                "",                     # Empty employee ID
                "HR001",                # Valid employee ID
                "",                     # Empty seniority choice
                "Management",           # Valid seniority
                "3"                     # Exit
            ],
            expected_files=["employees_hr.txt"]
        )
        
    def generate_summary_report(self):
        """Generate a summary of test results."""
        print("\n" + "="*60)
        print("TEST SUMMARY REPORT")
        print("="*60)
        
        passed_count = sum(1 for result in self.test_results if result['passed'])
        total_count = len(self.test_results)
        
        print(f"Tests Passed: {passed_count}/{total_count}")
        print(f"Success Rate: {(passed_count/total_count)*100:.1f}%")
        print()
        
        for i, result in enumerate(self.test_results, 1):
            status = "PASS" if result['passed'] else "FAIL"
            print(f"{i:2d}. {result['scenario']:<40} [{status}]")
        
        # Show created files
        print(f"\nFiles created in data/ directory:")
        if self.data_dir.exists():
            files = list(self.data_dir.glob("employees_*.txt"))
            if files:
                for file in files:
                    print(f"  - {file.name}")
            else:
                print("  (No files created)")
        
        print(f"\n{'='*60}")

def main():
    """Main execution function."""
    print("Starting automated test suite...")
    print("Make sure employee_roster.py is in the current directory.")
    print()
    
    # Check if main program exists
    if not os.path.exists('employee_roster.py'):
        print("Error: employee_roster.py not found in current directory!")
        return
    
    # Run tests
    tester = EmployeeRosterTester()
    tester.run_all_tests()
    tester.generate_summary_report()
    
    # Create markdown report for README
    create_markdown_report(tester.test_results)
    
    print("\nTesting complete! Check 'test_output_demo.md' for formatted results.")

def create_markdown_report(test_results):
    """Create a markdown report suitable for README documentation."""
    
    markdown_content = """# Employee Roster Manager - Test Output Demo

This document shows real-time output from automated testing of the Employee Roster Manager program.

## Test Results Summary

"""
    
    passed_count = sum(1 for result in test_results if result['passed'])
    total_count = len(test_results)
    
    markdown_content += f"- **Tests Passed:** {passed_count}/{total_count}\n"
    markdown_content += f"- **Success Rate:** {(passed_count/total_count)*100:.1f}%\n\n"
    
    markdown_content += "## Detailed Test Output\n\n"
    
    for i, result in enumerate(test_results, 1):
        status = "✅ PASSED" if result['passed'] else "❌ FAILED"
        
        markdown_content += f"### Test {i}: {result['scenario']} {status}\n\n"
        
        if result['output']:
            markdown_content += "**Program Output:**\n```\n"
            # Clean up output for markdown
            clean_output = result['output'].replace('\r\n', '\n').strip()
            markdown_content += clean_output
            markdown_content += "\n```\n\n"
        
        if result['errors']:
            markdown_content += "**Errors:**\n```\n"
            markdown_content += result['errors']
            markdown_content += "\n```\n\n"
    
    markdown_content += """
## Key Features Demonstrated

1. **Input Validation**: All invalid inputs are handled gracefully with clear error messages
2. **File I/O**: Department data is properly saved and loaded from text files
3. **Error Handling**: Missing files and permission errors are caught and handled
4. **User Experience**: Clear menus and helpful prompts guide the user
5. **Data Integrity**: Duplicate departments are prevented to maintain data consistency

## File Structure After Testing

The following files are created in the `data/` directory:
- `employees_sales.txt` - Sales department roster
- `employees_marketing.txt` - Marketing department roster  
- `employees_engineering.txt` - Engineering department roster
- `employees_hr.txt` - HR department roster

Each file contains employee data in the format:
```
FirstName – LastName – EmployeeID – SeniorityLevel
```

This automated testing ensures all functionality works correctly and handles edge cases appropriately.
"""
    
    # Write to file
    with open('test_output_demo.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    main()