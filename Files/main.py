import json

def send_sms(phone_number):
    print(f"SMS is sent to {phone_number}")

def send_email(email):
    print(f"Email is sent to {email}")

with open('sample.json', encoding="utf-8") as json_file:
    data = json.load(json_file)

for company in data["companies"]:
    for contact in company["contacts"]:
        send_sms(contact["phone"])
        send_email(contact["email"])