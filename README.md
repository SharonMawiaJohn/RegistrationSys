# Banking CLI Application

## Overview

This project involves creating a Command Line Interface (CLI) application for managing banking operations. Utilizing Python and SQLAlchemy ORM, the application will handle various banking tasks and provide a user-friendly CLI to interact with the banking system.

## Features

- **CLI Functionality**: Navigates a menu-driven interface to manage bank accounts, transactions, and customer information.
- **Database Integration**: Uses SQLAlchemy ORM to manage a relational database with interconnected tables.
- **Object-Oriented Programming (OOP)**: Applies OOP principles to ensure a well-structured and maintainable codebase.
- **Input Validation**: Validates user inputs and handle errors gracefully.

## Requirements

### ORM Requirements

- **Database Creation**: Use SQLAlchemy ORM for database management.
- **Model Classes**:
  - Defines at least 2 model classes, such as `Account`, `Transaction`, and `Customer`.
  - Implements at least one one-to-many relationship, e.g., one customer can have multiple accounts.
  - Includes property methods to add constraints to each model class.
  - Implements ORM methods for each model class:
    - Create
    - Delete
    - Retrieve all
    - Find by ID

### CLI Requirements

- **Menu Display**: Presents a menu system for user navigation.
- **User Interaction**:
  - Options to create, delete, display, view related objects, and find records by attributes for each model class.
  - Uses loops to maintain user interaction until they choose to exit.
- **Input Validation**: Ensuress user inputs are validated and handle errors with informative messages.
- **OOP Best Practices**: Follow best practices for OOP to maintain a clean and modular codebase.
- **Dependency Management**: Manages dependencies using Pipenv. 
- **Code Organization**: Maintain a well-structured project with organized folders and clear naming conventions.

## Code Structure

- **`Pipfile`**: Contains project dependencies.
- **`Pipfile.lock`**: Lock file for exact dependency versions.
- **`README.md`**: Project documentation.
- **`lib/`**: Contains the core application code.
  - **`models/`**: Contains SQLAlchemy model definitions.
    - **`__init__.py`**: Initializes the `models` package.
    - **`models.py`**: Defines the ORM model classes and methods.
  - **`cli.py`**: Main CLI application logic and menu handling.
  - **`debug.py`**: Debugging utilities and functions.
  - **`helpers.py`**: Utility functions and helper methods.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:ImeldaHope/banking.git
   cd banking
   ```

2. **Setup Virtual Environment**:

   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**:

   ```bash
   pipenv shell
   ```

4. **Run the Application**:

   ```bash
   python lib/cli.py
   ```

## Usage
Main Menu:

The main menu presents five options:
Customer Options: This leads to customer-related commands like create, update, delete, etc.
Account Options: This allows managing accounts with options like create, update, and delete.
Transaction Options: Manage transactions here.
Loan Options: Loan-related operations such as create, update, and delete.
List All Options: View a list of customer accounts, loans, or account transactions.
Exit: Ends the program.
Customer Menu:

Contains options 1 through 6 and provides functionality for customer operations.
Account Menu:

Contains options 7 through 12 and provides functionality for account operations.
Transaction Menu:

Contains options 13 through 16 and handles transaction operations.
Loan Menu:

Contains options 17 through 20 and handles loan-related operations.
List All Menu:

Contains options 21 through 23 and allows listing customer accounts, loans, and account transactions.
Exit and Back to Main Menu:

Option 0 is used to go back to the main menu from any of the nested menus.
The main menu has a 0 option to exit the program.

1. **Start the Application**:
   Launch the CLI application from the terminal.

2. **Navigate the Menu**:
   Use the menu options to:
   - Create new accounts, transactions, or customers.
   - Delete existing records.
   - Display all records or specific records by ID.
   - View related objects (e.g., transactions for an account).
   - Find records by attributes (e.g., find an account by account number).

3. **Input Validation**:
   The application will validate inputs and provide error messages for invalid data entries.

---

Thank you for interacting with my banking CLI

4. **Migrations**

Then run root@:~/Development/code/phase-3/RegistrtionSys# alembic init migrations
Next run root@:~/Development/code/phase-3/RegistrtionSys# alembic revision --autogenerate -m "Adding tables"
Next run root@:~/Development/code/phase-3/RegistrtionSys/lib# alembic upgrade head

Author 
***Sharon John***
***sharon.mawia@goldstepcapital.com***