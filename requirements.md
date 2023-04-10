

## Functional Requirements
1. Ryan: Login
2. Marvin: To-do list
3. Chatbox (direct message others)
4. Recycle and permanently delete emails
5. Derrick: User registration
6. Marvin: Edit User Profile
7. Derrick: Search Messages 
8. Sort Messages/emails
9. Ryan: Draft emails
10. Ryan: Attach images in e-mail
11. Send emoticons
12. Marvin: Categorize emails

## Non-functional Requirements
1. Emails should arrive after 2 seconds
2. Character count should not exceed 256 characters
3. Image size limit of 8MBs
4. Limit amount of people can receive an email to 5 people


## Use Case

1. Use Case: Search Messages
- **Summary:** search the User’s messages through specific parameters
- **Actor(s):** User
- **Pre-condition:** User has emails inside their inbox 
- User has an email account and is signed into the client 
- **Trigger:** User enters the parameters to search through their emails
- **Primary Sequence:**
1. User navigates to their inbox to view their emails
2. User selects the sort option from the search bar 
3. User enters keywords, phrases, or other information into search bar
4. User clicks “Enter” to initialize the search and client will search through inbox for those parameters
5. Email client displays all emails that fit the search criteria 
- **Alternate Sequence:**
1. User doesn’t have any emails that relate to the search criteria they entered
2. User doesn’t provide adequate information inside the search bar for the client to look for
- Post-Condition: User is able to view the specific emails/messages that they were looking for


2. Use Case: User Registration 
- **Summary:** User is able to register for the email client
- **Actor(s):** User
- **Pre-condition:** User doesn’t have an account for the client
- **Trigger:** User decides to create an account for this email client
- **Primary Sequence:**
1. User navigates to the email client’s registration page
2. User provides their personal information ex. Name, Date of Birth, etc
3. User creates a username and password for the client
4. System will verify the username and password 
5. System creates a new account for the user 
6. User is guided to the homepage interface of the email client
- **Alternate Sequence:** User enters a username that has already been taken which prompts the client to display an error message to change their username 
Information provided by the user may be incomplete which prompts the client to display an error message
- **Post-condition:** The user successfully creates an account for the email client and has access to its features 

3. Use Case: Draft Emails
- **Summary:** Users should be able to draft emails
- **Actors:** User, website
- **Pre-condition:** User is logged in
- **Trigger:** User clicks on the "New Message" button
- **Primary Sequence:**
1. The user clicks on the "New Message" button
2. The user clicks on the "Recipient" data field and types in an email address
3. The system checks whether the username / email is valid or not.
4. The user types in a message in the "Message" field 
5. The user clicks the "Draft" button.
6. The system proceeds to save the user's email in the draft.
- **Alternative Sequence:**
- The recipient is not a valid email address
- a. Proceed to alert the user with a pop-up box that the username entered is not valid.
- b. The user has to re-enter the email
**Post-conditions:** The user will be able to see their draft messages and go back to them anytime.

4. Use Cases: Login
- **Summary:** Users should be able to login
- **Actors:** Website, user
- **Pre-condition:** The user is on the website
- **Trigger:** The user clicks on the "login" on the webpage.
- **Primary Sequence:**
1. The user clicks "Login" on the homepage.
2. The system redirects the user to the login webpage.
3. The user will click the username field enter in the username in the username field.
4. The user will then click the password field and enter their password.
5. The user clicks "Login." 
6. The system validates whether the username and password is valid.
7. The system then redirects the user to the e-mail client.
**Alternative Sequence:** 
1. The username and password is invalid. 
a. Alert the user that the username or password is invalid.
b. The user re-enters their username and password.
**Post-conditions:** The user is on the main webpage with all their emails.





