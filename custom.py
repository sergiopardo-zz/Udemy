import smtplib

host = "smtp.gmail.com"
port = 587
username = "sergio.pardo@runahr.com"
password = "Altair01"
from_email = username
to_list = ["sergio.pardo@runahr.com"]


email_conn = smtplib.SMTP(host,port)
# Help me to know if connect the service
email_conn.ehlo()
# Start the process
email_conn.starttls()
# Login email
email_conn.login(username,password)
# Send a email
email_conn.sendmail(from_email,to_list, "Hello it's a test")
# Close the service 
email_conn.quit()
