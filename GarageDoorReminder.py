import time
from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
user_phone_number = 'user_phone_number_to_receive_reminder'

# State variables
door_opened_time = 0
reminder_sent = False

# Function to send SMS using Twilio
def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=user_phone_number,
        from_=twilio_phone_number,
        body=message
    )

# Main loop
while True:
    # Replace this with code to check the status of your door sensor
    door_status = check_door_status()

    if door_status == 'opened':
        door_opened_time = time.time()
        reminder_sent = False
    elif door_status == 'closed':
        # Check if the door has been closed for more than 15 minutes
        elapsed_time = time.time() - door_opened_time
        if elapsed_time > 900 and not reminder_sent:
            send_sms("Please ensure the garage door is closed securely.")
            reminder_sent = True

    # Adjust the sleep duration based on your requirements
    time.sleep(60)  # Sleep for 1 minute before checking again
