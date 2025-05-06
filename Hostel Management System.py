Overview of the project:-------

In this project, you will create a simple Hostel management system using Python. This application will allow users to add, search for, delete, and list of Student entries. The project focuses on reinforcing your understanding of Python's basic concepts, particularly conditional statements and dictionaries.

Objectives-----

Understand and apply Python dictionaries to store student  entries.
Use conditional statements to handle different student actions like (entry time and exit time from hostel)actions.
Implement CRUD (Create, Read, Update, Delete) operations on the student  entries.

Project Structure:------

Your application should be able to:
Add a New Student Contact: Prompt the user for the name and phone number of a new contact and add it to the list.
Search for a  Student Contact: Allow the user to search for a contact by name and display the contact's phone number.
Delete a Student Contact: Enable the user to delete a contact by name.
List All Contacts: Display all contacts in the list.
Exit: Terminate the application.

Implementation Steps:-------

Step 1: Setup Your Project
a)Create a new Python file named Hostel management.py.
b)Open this file in your chosen text editor.

Step 2: Initialize the Student list
a)At the beginning of your program, create an empty dictionary to store your Student contacts. Each Student contact name will be a key, and the associated phone number will be the value.

Step 3: User Interface
a)Implement a loop that continuously displays a menu of options to the user until they choose to exit. Use input() to read the user's choice and if-else statements to handle different actions based on the choice.

Step 4: Implementing CRUD Operations
a)Add a New Contact: Check if the name already exists in the dictionary. If it does, display a message; otherwise, add the new entry.
b)Search for a Contact: Check if the contact exists in the dictionary. If so, display the contact's phone number; otherwise, inform the user that the contact was not found.
c)Delete a Contact: Similar to search, but remove the contact from the dictionary if it exists.
d)List All Contacts: Use a loop to iterate through the dictionary and display each contact's name and phone number.

Step 5: Testing
a)Thoroughly test your application to ensure it handles different scenarios gracefully, such as searching for a non-existent contact or adding a contact that already exists.
b)Evaluation Criteria
c)Functionality: The application meets all the specified requirements.
d)Code Quality: The code is clean, well-commented, and follows standard Python conventions.
e)Error Handling: The application can handle incorrect user inputs without crashing.


Let's Wrap UP:

This project is an excellent opportunity to practice the fundamental concepts of Python. By completing it, you will gain a deeper understanding of dictionaries and conditional statements, which are essential components of Python programming. Good luck!
