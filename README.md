# Bear_Robotics_ATM
Bear Robotics assignment - Implement a simple ATM controller


Write code for a simple ATM. It doesn't need any UI (either graphical or console), but a controller should be implemented and tested.



# Requirements
At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw



For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.



Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.



A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.



Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.



You can simplify some complex real world problems if you think it's not worth illustrating in the project.



# How to submit
Please upload the code for this project to GitHub or anywhere, and post a link to your repository below. Please attach the instruction to clone your project, build and run tests in README.md file in the root directory of the repository.


# Information about implementation
Overall, the code provides a basic implementation of an ATM and account system that allows users to perform transactions and view their account balance.
The provided code includes three classes: ATM, Account, and the main function.

The ATM class represents an automated teller machine and has methods to insert and remove cards, view the balance of the ATM, deposit cash into the ATM, and withdraw cash from the ATM. The initial balance of the ATM is set in the constructor.

The Account class represents a user account and has methods to check if the PIN number is correct, check the account balance, deposit cash into the account, or withdraw cash from the account. The account details including the account holder's name, PIN number, account number, and current balance are set in the constructor.

The main function creates an Account object with initial account details, and an ATM object with an initial balance. It then runs a loop to simulate a user transaction by taking input from the user to insert the card, enter the PIN number, select an account, and perform transactions such as checking the balance, depositing cash, and withdrawing cash. The loop continues until the user ends the transaction by selecting the option to end the transaction by removing the card.
