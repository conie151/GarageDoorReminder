# GarageDoorReminder
An automatic Notification system that reminds family members to ensure the garage door is closed

# Important Notes
This is a simple Python script using the Twilio API for sending text messages, notifying me when the door has been open and closed and then 15 minutes of inactivity has passed by, in order to ensure that the door has been lock.
Note that you'll need to sign up for a Twilio account and obtain the necessary credentials (account SID, auth token, and a Twilio phone number) to use their API.

Instructions for the user:
Make sure to replace the placeholder values for your_account_sid, your_auth_token, your_twilio_phone_number, and user_phone_number_to_receive_reminder with your actual Twilio credentials and the phone number you want to receive reminders.

Also, replace the check_door_status() function with the actual code to retrieve the status of your door sensor. The script assumes that the function returns 'opened' or 'closed' based on the door status.