# Amazon Account Phone Verification Bot

## Overview
This Python bot automates the process of verifying Amazon accounts using phone numbers. It uses Selenium for web automation and CapMonster for solving captchas.
## CapMonster Solve
All Thank For Capmonster for support and this is best solver
## Features
- **Multi-threaded**: Supports running multiple instances simultaneously.
- **Proxy Support**: Can be configured to use proxies for anonymity.
- **Headless Mode**: Can run in headless mode for silent operation.
- **Automated Captcha Solving**: Uses CapMonster API to solve captchas.

## Requirements
- Python 3.x
- Required Python packages can be installed using:

## Setup
1. Clone the repository:

2. Install dependencies:

3. Obtain CapMonster API Key and replace `your_capmonster_api_key` in `bot.py` with your actual API key.

## Usage
1. Prepare your accounts and phone numbers:
- Add Amazon accounts in `accounts.txt` in the format `email:password`.
- Add phone numbers in `numbers.txt`.

2. Run the bot:
- Enter the number of browsers to use.
- Choose headless or non-headless mode.
- Choose proxy or non-proxy mode.
- Enter the number of times to call per account.

3. Monitor the output and results.

## Contact
For any issues or inquiries, feel free to contact me at [your_email@example.com](mailto:your_email@example.com).

## Acknowledgments
- Thanks to CapMonster for providing a robust captcha solving service.
