from email.message import EmailMessage


email_sender = ""
email_password = ""

email_receiver = ""

subject = "Test"
body = "" "Test body email" ""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)