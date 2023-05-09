

## Functional Requirements
1. Ryan: Login
2. Marvin: To-do list
3. Felix: Public chatbox 
4. Felix: Recycle and permanently delete emails
5. Derrick: User registration
6. Marvin: Edit User Profile
7. Derrick: Search Messages 
8. Felix: Sort Messages/emails
9. Ryan: Draft emails
10. Ryan: Create and send messages
11. Derrick: Attach images
12. Marvin: Add custom categories

## Non-functional Requirements
1. Hash all passwords with the SHA1 algorithm
2. Character count should not exceed 256 characters
3. Image size limit of 8MBs
4. Limit amount of people can receive an email to 5 people


## Use Case

1. Use Case: Search Messages
- **Summary:** search the User’s messages through specific parameters
- **Actor(s):** User, email client
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
- a. The email client shows no e-mails.
- b. Put an alert saying that no e-mails were found. 
- c. The user re-enters another search term.
3. User doesn’t provide adequate information inside the search bar for the client to look for
- a. Alert the user that there was inadequate information and prompt the user to reenter search criteria.
- b. The user reenters information in the search bar.
- Post-Condition: User is able to view the specific emails/messages that they were looking for


2. Use Case: User Registration 
- **Summary:** User is able to register for the email client
- **Actor(s):** User, e-mail client
- **Pre-condition:** User doesn’t have an account for the client
- **Trigger:** User decides to create an account for this email client
- **Primary Sequence:**
1. User navigates to the email client’s registration page
2. User provides their personal information ex. Name, Date of Birth, etc
3. User creates a username and password for the client
4. System will verify the username and password 
5. System creates a new account for the user 
6. User is guided to the homepage interface of the email client
- **Alternate Sequence:** 1. User enters a username that has already been taken which prompts the client to display an error message to change their username 
- a. Display an error message saying the username has already been taken.
- b. The user enters in another username. 
2. Information provided by the user may be incomplete which prompts the client to display an error message
- a. Highlight the fields where the user have not entered information.
- b. The user fills in information that is missing.
- **Post-condition:** The user successfully creates an account for the email client and has access to its features 

3. Use Case: Draft Emails
- **Summary:** Users should be able to draft emails
- **Actors:** User, e-mail client
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
1. The recipient is not a valid email address
- a. Proceed to alert the user with a pop-up box that the username entered is not valid.
- b. The user has to re-enter the email
**Post-conditions:** The user will be able to see their draft messages and go back to them anytime.

4. Use Cases: Login
- **Summary:** Users should be able to login
- **Actors:** E-mail client, user
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
- **Alternative Sequence:** 
1. The username and password is invalid. 
- a. Alert the user that the username or password is invalid.
- b. The user re-enters their username and password.
- **Post-conditions:** The user is on the main webpage with all their emails.


5. Use Cases: Edit Profile
- **Summary:** Users should be able to edit their profile
- **Actors:** User, website
- **Pre-condition:** The user has to be logged in on their account.
- **Trigger:** The user clicks on their profile and click on edit profile from the drop down menu
- **Primary Sequence:**
1. The user clicks on their icon on the top right.
2. The user is moved to a their profile account
3. User presses on the edit profile button
4. User changes what they desire
5. User hits the save button at the bottom
6. The system saves the newly updated profile.
- **Alternative Sequence:** 
1. The user forgets to hit save
- a. Profile is not updated
- b. Message pops up explaining asking to save changes before going
- **Post-conditions:**  The user is prompted to the newly saved profile

6. Use Case: Categorize Emails
- **Summary:** User is able to categorize the emails they recieve and send
- **Actor(s):** User, Website
- **Pre-condition:** User has to be signed in and have some emails in inbox
- **Trigger:** User hits the categorize button
- **Primary Sequence:**
1. User navigates to the their personal email inbox
2. User presses the categorize button
3. User can sort their personal inbox however they want
4. Default option given is sorting by inbox by recipient name, date, and age
5. Users can create own categories to put email in
6. System saves categories with emails in each
- **Alternate Sequence:** 
1. User forget to input a category name for email.
- a. Tell the user to input a category name.
- b. The user reinputs the category name.
- **Post-condition:** The user is in the inbox with categories

7. Use Case: To-do list
- **Summary:** User will have a checklist on the side to help guide them through the steps needed to send a message
- **Actor(s):** User, Website
- **Pre-condition:** User has to be drafting an email for the to-do list to appear
- **Trigger:** User begins drafting an email
- **Primary Sequence:**
1. User clicks on the "New Message" button
2. To-do list appears prompting the user to complete a checklist of things needed to send a message
3. Once the website verifies that the username/email for the recipient is valid, the checklist will cross out the requirement to enter a recipient
4. Once the user types a message into the "Message" field, the checklist will cross out the requirement to enter a message and be completed.
- **Alternative Sequence:**
1. Too many recipients are specified by the user
- a. The To-do list requirement involving specifying the recipient will become unchecked again
- b. User will no longer be able to send the message
- c. User will be prompted to reduce the number of recipients in order to meet the maximum requirement for maximum recipients
2. Message has too many characters
- a. The requirement involving entering a message will become unchecked again
- b. User will no longer be able to send the message
- c. User will be prompted to reduce the characters in their message
- d. Once the user reduces the number of characters to meet the requirements, the checklist will check off the requirement to enter a message once again
- **Post-conditions:** User will once again be able to send a message

8. Use Case: Recycle and permanently delete emails
- **Summary:** User will have the option to recycle or permanently delete previous emails
- **Actor(s):** User, Website
- **Pre-condition:** User has to have received emails
- **Trigger:** User clicks the recycle button on an email that is in their inbox
- **Primary Sequence:**
1. User clicks on the "Recycle" button
2. Message moves from the messages category to a recycled category
3. If the user enters the recycled category, they can view messages that they previously recycled.
4. Users will be able to do one of two things to recycled messages
- **Alternative Sequence**
1. Move recycled messages back to the messages category
- a. User will press the "move back to messages" button
- b. Message will be removed from the recycled messages category
- c. Message will reappear in the messages category
2. Permanently delete recycled messages
- a. User will press the "permanently delete message" button
- b. Message will be removed from the recycled messages category
- **Post-condition:** Message will no longer exist in the User's messages or the recycled messages categories
