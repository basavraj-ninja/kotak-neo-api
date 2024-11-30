import time
import logging
import json
from neo_api_client import NeoAPI
from neo_api_client.api.limits_api import LimitsAPI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Threshold for unrealized losses
LOSS_THRESHOLD = -5000.0  # Set your loss threshold here
CHECK_INTERVAL = 60  # Time interval (in seconds) between checks

# Initialize the Kotak Neo API client
client = NeoAPI(
    consumer_key="nfD9cE235rOqFHIERNbrIseUjY0a",
    consumer_secret="oEAfqGkKe_JoefyjY3fQfXPacY0a",
    environment="prod"
)

# Log in to the API
try:
    client.login(
        mobilenumber="+919900927937",
        password="Aarav@123"
    )
    print("Login successful!")
    otp = input("Enter the OTP sent to your mobile: ")
    client.session_2fa(OTP=otp)
    print("Authentication successful!")
except Exception as e:
    print("Login or authentication failed:", str(e))
    exit(1)



# Pretty print the available methods of the client object
def print_client_methods(client):
    methods = dir(client)
    print("\nAvailable Methods in Client:")
    print("=" * 40)
    for method in methods:
        print(f"- {method}")
    print("=" * 40)

# Call the function with your client object
print_client_methods(client)

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

# Fetch positions using the `positions` method
try:
    limits_data = client.limits()  # Directly call the positions method
    print("limits Data:")
    print(json.dumps(limits_data, indent=4))  # Pretty-print the positions data
except Exception as e:
    print("Failed to fetch limits:", str(e))

