

## Functional Requirements
1. Login
2. To-do list
3. Chatbox (direct message others)
4. If the recipient does not exist?
5. Derrick: User registration
6. Edit User Profile
7. Derrick: Search Messages 
8. Sort Messages/emails
9. Ryan: Draft emails
10. Ryan: Attach images in e-mail
11. Send emoticons
12. Categorize emails

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




