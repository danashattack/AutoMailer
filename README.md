# AutoMailer

Automation framework using Microsoft Graph API to send emails. Includes chat module with Markovify-generated responses and attachment module. Built with Python, utilizing Faker, msal, and Requests. Future goals are to implement attachments for larger sends and more realistic email exchanges.

## Table of Contents

* [License](#license)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Acknowledgments](#acknowledgments)

## License

This project is licensed under the [MIT License](LICENSE).

## Prerequisites

* Python 3.8+
* Microsoft EntraID App with required permissions and app secret
* Configure "Send on Behalf of" permissions in M365 for all users
* Faker, Markovify, msal, and Requests libraries

## Installation

1. Clone the repository: `git clone https://github.com/your-username/your-repo-name.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Microsoft EntraID Application credentials: `cp .env.example .env` and fill in your credentials

## Usage

1. Create(or use existing) EntraID application with required permissions
2. Add your Microsoft EntraID application credentials to the .env file
3. Modify the chat module prompt if you want it to be more personalized.
4. Run the main module: `python main.py`

## EntraID Application Permissions

* Mail.ReadWrite
**Delegated**
Read and write access to user mail

* Mail.ReadWrite
**Application**
Read and write mail in all mailboxes

* Mail.ReadWrite.Shared
**Delegated**
Read and write user and shared mail

* Mail.Send
**Delegated**
Send mail as a user

* Mail.Send
**Application**
Send mail as any user

* Mail.Send.Shared
**Delegated**
Send mail on behalf of others

* User.Read.All
**Delegated**
Read all users' full profiles

* User.Read.All
**Application**
Read all users' full profiles

## Acknowledgments

* [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/)
* [Faker](https://faker.readthedocs.io/en/master/)
* [Markovify](https://github.com/jsvine/markovify)
* [msal](https://github.com/AzureAD/microsoft-authentication-library-for-python)
* [Requests](https://requests.readthedocs.io/en/master/)
