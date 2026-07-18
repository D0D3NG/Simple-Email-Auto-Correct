# Simple-Email-Auto-Correct

The goal of this project was to simulate a simple account registration process by accepting a user's first name, last name, and email address. Before displaying the final account information, it automatically cleans and formats the user's input to make it more consistent and readable.

The goal of this project was to practice working with user input, string manipulation, conditional statements, and basic input validation.

# Features:
*Accepts a user's first name, last name, and email address.
*Automatically formats names into proper title case.
*Removes unnecessary leading and trailing whitespace.
*Removes accidental numeric characters from name input.
*Converts email addresses to lowercase for consistency.
*Performs basic validation for supported email domains.
*Displays a formatted account summary after successful registration.

# Concepts Practiced
User input (input())
String methods
.title()
.lower()
.strip()
.lstrip()
.rstrip()
Conditional statements (if / else)
Basic input validation
String formatting with f-strings
Purpose

This project was created as a learning exercise to better understand how programs can clean and standardize user input before processing it.

Rather than focusing on building a complete registration system, the objective was to practice writing code that improves the quality and consistency of user-entered information.

Current Limitations

# This is an introductory learning project and has several intentional limitations:

*Supports only a small set of email domains.
*Performs only basic validation.
*Does not verify whether an email address actually exists.
*Does not store registered accounts.
*Does not repeatedly prompt the user after an invalid input.

# Possible Future Improvements
*Support additional email providers.
*Improve email validation.
*Continue prompting until valid input is entered.
*Store registered users in a file or database.
*Prevent duplicate registrations.
*Add a graphical user interface or web version.
