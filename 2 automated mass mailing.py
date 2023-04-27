from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

email_data = pd.read_excel("email_data.xlsx")

# Replace with gmail credentials
email_id = list(email_data["sender_email"])
password = list(email_data["password"])

# Replace with email recipients
to_email = list(email_data["recipient_email"])

# Count of sent email
sent_email = []
sent_email_records = []

# Launch chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Loop through each gmail account
for x in range(len(email_id)):
    email_ids = email_id[x]
    passwords = password[x]

    sent_email_records.extend(sent_email)