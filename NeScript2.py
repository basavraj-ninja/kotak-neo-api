import time
import logging
from neo_api_client import NeoAPI
from neo_api_client.api.positions_api import PositionsAPI
#from neo_api_client.api.orders_api import OrdersAPIclear
import json

# Step 1: Initialize the Kotak Neo API client
client = NeoAPI(
    consumer_key="nfD9cE235rOqFHIERNbrIseUjY0a",  # Replace with your Consumer Key from Kotak
    consumer_secret="oEAfqGkKe_JoefyjY3fQfXPacY0a",  # Replace with your Consumer Secret from Kotak
    environment="prod"  # Use "prod" for live trading
)

# Step 2: Log in with your registered mobile number and password
try:
    client.login(
        mobilenumber="+919900927937",  # Replace with your registered mobile number
        password="Aarav@123"  # Replace with your Kotak login password
    )
    print("Login successful!")
except Exception as e:
    print("Login failed. Exception details:")
    print(type(e))  # Check the type of the exception
    print(str(e) if e else "Unknown error occurred")  # Handle NoneType gracefully

# Step 3: Authenticate using the OTP sent to your registered mobile number
try:
    otp = input("Enter the OTP sent to your mobile: ")  # User enters OTP
    client.session_2fa(OTP=otp)
    print("Authentication successful!")
    print("Attributes of client:", dir(client))
    
except Exception as e:
    print("Authentication failed. Exception details:")
    print(type(e))  # Check the type of the exception
    print(str(e) if e else "Unknown error occurred")  # Handle NoneType gracefully
    print("Attributes of client:", dir(client))
    # Print the attributes of the client object in a neat format
    

from neo_api_client.api.positions_api import PositionsAPI

# Initialize the PositionsAPI with the authenticated client
#positions_api = PositionsAPI(client)

# Fetch holdins using the `Hondings` method
try:
    holdings_data = client.holdings()  # Directly call the holdings method
    print("Holndings Data:", holdings_data)
except Exception as e:
    print("Failed to fetch positions:", str(e))

# Fetch Positions using the `Positions` method
try:
    positions_data = client.positions()  # Directly call the positions method
    print("Positions Data:", positions_data)
except Exception as e:
    print("Failed to fetch positions:", str(e))

    # Fetch holdings using the `holdings` method
try:
    holdings_data = client.holdings()  # Directly call the holdings method
    print("Holdings Data:")
    print(json.dumps(holdings_data, indent=4))  # Pretty-print the holdings data
except Exception as e:
    print("Failed to fetch holdings:", str(e))
        # Pretty-print the entire holdings data
    print("Holdings Data:")
    print(json.dumps(holdings_data, indent=4))  # Pretty-print the holdings data



except Exception as e:
    print(f"Failed to fetch holdings: {str(e)}")

# Fetch positions using the `positions` method
try:
    positions_data = client.positions()  # Directly call the positions method
    print("Positions Data:")
    print(json.dumps(positions_data, indent=4))  # Pretty-print the positions data
except Exception as e:
    print("Failed to fetch positions:", str(e))


# Extract all `displaySymbol` values
try:
    display_symbols = [
        holding.get("displaySymbol") for holding in holdings_data.get("data", [])
        if holding.get("")
    ]

    # Print the extracted `displaySymbol` values
    print("Extracted Display Symbols:")
    print(display_symbols)
except Exception as e:
    print("Failed to fetch positions:", str(display_symbols))




