import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
azure_client_id = os.getenv("AZURE_CLIENT_ID")
azure_client_secret = os.getenv("AZURE_CLIENT_SECRET")
azure_tenant_id = os.getenv("AZURE_TENANT_ID")
azure_subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

# Example usage (e.g., printing or logging, but NOT recommended in production!)
print("AZURE_CLIENT_ID:", azure_client_id)
print("AZURE_CLIENT_SECRET:", azure_client_secret)
print("AZURE_TENANT_ID:", azure_tenant_id)
print("AZURE_SUBSCRIPTION_ID:", azure_subscription_id)
print("GITHUB_ACCESS_TOKEN:", github_access_token)

