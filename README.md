# Python Login System

A Python-based command-line login system created as a practical project to practice user registration, authentication logic, file handling, input validation, and activity logging.

## Overview

This program allows users to:

- Register an account
- Log in
- Log out
- View activity logs
- Check the currently logged-in user
- Exit the program

User information is stored in a local text file, while login and logout activities are recorded in a separate log file.

## Features

- User registration
- Username validation
- Password confirmation
- Password requirements
- Duplicate username detection
- Login authentication
- Three login attempts
- Login/logout tracking
- Activity logging
- Current-user display
- File handling
- Error handling

## Technologies Used

- Python 3
- `datetime`
- File handling
- Functions
- Loops
- Conditional statements
- Exception handling
- String methods

## How It Works

### Registration

The user provides:

1. Username
2. Password
3. Password confirmation

The program validates the information before storing the account.

### Login

The user enters their username and password.

The program checks the stored information and allows up to three login attempts.

### Logout

The currently logged-in user can log out of the system.

### Activity Logs

The program records registration, login, and logout events with timestamps.

## How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK
