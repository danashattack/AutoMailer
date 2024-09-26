from concurrent.futures import ProcessPoolExecutor
from dotenv import load_dotenv
from src.chat_module import chatbot_response
from faker import Faker
import multiprocessing
import msal
import os
import random
import requests;

# Clear the console
def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

clear_console()

# Define the function to acquire an access token
def acquire_token():
    app = msal.ConfidentialClientApplication(
        authority=authority,
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
    )
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return token

# Define the function to send an email
def send_email(i, num_emails, users, result):
    # Create a copy of the users list to avoid modifying the original list
    users_copy = users.copy()
    # Select a random sender from the users list
    sender = random.choice(users_copy)
    # Remove the sender from the list so that the recipient is not the same as the sender
    users_copy.remove(sender)
    # Select a random receiver from the remaining users
    recipient = random.choice(users_copy)

    print(f"Sending email {i+1} of {num_emails} from {sender['displayName']} to {recipient['displayName']}...")

    # Set the endpoint and recipient
    endpoint = f'https://graph.microsoft.com/v1.0/users/{sender["id"]}/sendMail'
    toUserEmail = recipient['mail']

    # Initialize Faker
    fake = Faker()

    # Generate subject and body using faker and markovify
    subject = fake.sentence()
    body = chatbot_response()

    # Create the email message in JSON format
    email_msg = {'Message': {'Subject': subject,
                            'Body': {'ContentType': 'Text', 'Content': body},
                            'ToRecipients': [{'EmailAddress': {'Address': toUserEmail}}]
                            },
                'SaveToSentItems': 'true'}

    # Send the email
    r = requests.post(endpoint, headers={'Authorization': 'Bearer ' + result['access_token']}, json=email_msg)
    if r.ok:
        return f"Sent email {i+1} of {num_emails} successfully"
    else:
        return f"Failed to send email {i+1} of {num_emails}"

# Define the main function with multiprocessing freeze support
if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    # Create a queue to store the output
    output_queue = multiprocessing.Queue()

    # Get the number of emails to send
    print("***Welcome to the Microsoft Graph Email Bot!***\n")
    num_emails = int(input("\nHow many emails would you like to send? "))  

    # Load environment variables from .env file
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    TENANT_ID = os.getenv("TENANT_ID")

    # Set the authority URL
    authority = f"https://login.microsoftonline.com/{TENANT_ID}"

    # Create a queue to store the users
    users_queue = multiprocessing.Manager().Queue()
    
    # Call the function to acquire an access token and begin process
    result = acquire_token()
    
    if "access_token" in result:

        # Add users to the queue
        print("Retrieving a list of users from the organization...")
        users_endpoint = 'https://graph.microsoft.com/v1.0/users'
        users_response = requests.get(users_endpoint, headers={'Authorization': 'Bearer ' + result['access_token']})
        users = users_response.json()['value']
        
        # Start ProcessPoolExecutor and send emails in parallel        
        with ProcessPoolExecutor() as executor:
            futures = []
            for i in range(num_emails):
                future = executor.submit(send_email, i, num_emails, users, result)
                futures.append(future)

            # Get the output from the futures and print it
            for future in futures:
                output = future.result()
                print(output)  
                  
        print("\nAll processing is complete, for better or worse.... !Jobs Done!")
        print("\nThanks for using the AutoMailer script!")
        
    # Print an error message if an error occurred getting token
    else:
        print("Token acquisition failed.")
        print("\nError: " + result.get("error"))
        print("Error code: " + result.get("error_codes"))
        print("Description: " + result.get("error_description"))
        print("Correlation ID: " + result.get("correlation_id"))

        

