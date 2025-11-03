# Employee Roster Manager LAB06

A professional menu-driven Python program for managing department-based employee rosters with comprehensive file I/O and robust error handling.

## Project Overview

This program demonstrates key programming concepts including:
- **File I/O Operations**: Reading from and writing to text files
- **Error Handling**: Comprehensive exception handling for user input and file operations  
- **Input Validation**: Robust validation for all user inputs
- **Modular Programming**: Clean separation of concerns with focused functions
- **User Experience**: Intuitive menu design and helpful error messages

## Folder Structure

```
lab6_employee_roster/
├── employee_roster.py          # Main program file
├── automated_test_runner.py    # Comprehensive automated testing
├── testcase_script.py          # Manual testing guide
├── data/                       # Directory for department files
│   ├── employees_engineering.txt   # Engineering department roster
│   ├── employees_marketing.txt     # Marketing department roster
│   └── employees_sales.txt         # Sales department roster
├── test_output_demo.md         # Real-time test output documentation
└── README.md                   # This documentation file
```

**Files:**
- [employee_roster.py](lab6_employee_roster/employee_roster.py) - Main program code
- [automated_test_runner.py](lab6_employee_roster/automated_test_runner.py) - Automated testing suite
- [testcase_script.py](lab6_employee_roster/testcase_script.py) - Manual testing guide
- [test_output_demo.md](lab6_employee_roster/test_output_demo.md) - Test results

**Sample Data Files:**
- [employees_sales.txt](lab6_employee_roster/data/employees_sales.txt) - Sales department
- [employees_marketing.txt](lab6_employee_roster/data/employees_marketing.txt) - Marketing department
- [employees_engineering.txt](lab6_employee_roster/data/employees_engineering.txt) - Engineering department

## How to Run

```bash
cd lab6_employee_roster
python employee_roster.py
```

Follow the on-screen menu to add departments, view rosters, or exit.

## Testing

**Automated Testing:**
```bash
python automated_test_runner.py
```

---

## 🎬 **LIVE DEMO - See The Program In Action!**

### **👉 [VIEW COMPLETE TEST OUTPUT DEMO](lab6_employee_roster/test_output_demo.md) 👈**

**See real-time program output from comprehensive testing scenarios**

---

**Manual Testing:**
```bash
python testcase_script.py
```
Interactive guide through test scenarios.

---

## 📦 **Download**

**Download the complete project:**

[![DOWNLOAD](https://img.shields.io/badge/DOWNLOAD-Lab06EmployeeRoster.zip-blue?style=for-the-badge&logo=github)](https://github.com/hjoseph777/Lab06EmployeeRoster/releases/download/v1/Lab06EmployeeRoster.zip)

**Or clone the repository:**

```bash
git clone https://github.com/hjoseph777/Lab06EMPLOYEEROSTER.git
cd Lab06EMPLOYEEROSTER
git checkout v1
```

---

## Features

### Add New Department
- Prompts for department name and validates uniqueness
- Collects employee data (first name, last name, ID, seniority)
- Validates seniority levels: Entry, Junior, Middle, Senior, Management, Executive
- Saves data to individual text files in the `data/` directory
- **Note**: Won't overwrite existing departments

### View Existing Department  
- Loads employee roster from saved files
- Displays formatted employee information
- Shows total employee count
- Handles missing departments gracefully with retry options

### Error Handling
- **File Errors**: FileNotFoundError, PermissionError handling
- **Input Validation**: Non-empty names, valid integers, valid seniority levels
- **User Experience**: Clear error messages and recovery options

## Technical Details

### File Format
Employee data is stored as comma-separated values (CSV) with this format:
```
FirstName,LastName,EmployeeID,SeniorityLevel
```

### Filename Convention  
Department files are saved as:
```
data/employees_[department_name].txt
```
Department names are converted to lowercase with spaces replaced by underscores for safe filesystem usage.

### Functions

- [`get_valid_integer()`](lab6_employee_roster/employee_roster.py#L11) - Validates numeric input with minimum value checking
- [`get_valid_seniority()`](lab6_employee_roster/employee_roster.py#L35) - Handles seniority level validation with multiple input formats
- [`build_filename()`](lab6_employee_roster/employee_roster.py#L70) - Creates safe filenames from department names
- [`add_department()`](lab6_employee_roster/employee_roster.py#L80) - Complete workflow for creating new departments
- [`view_department()`](lab6_employee_roster/employee_roster.py#L147) - File loading and formatted display with error recovery
- [`main()`](lab6_employee_roster/employee_roster.py#L186) - Menu system and program coordination

## Notes

- All employee data is stored locally in text files
- The program creates the `data/` directory automatically if it doesn't exist
- Department names are case-insensitive for file operations but preserve user input for display
- No network connectivity required - fully self-contained application

---

## Author   
- Harry Joseph
