import smtplib

# Replace with your own email address and password
email = 'your-email@gmail.com'
password = 'your-password'

# Replace with the recipient's email address
recipients = ['recipient1@gmail.com', 'recipient2@gmail.com', ...]

# Replace with a custom subject
subject = 'Test email from Python'

# Replace with a custom message
message = 'This is a test email sent from Python'

# Set up the email server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# Send the email
for recipient in recipients:
    server.sendmail(email, recipient, subject, message)

server.quit()
