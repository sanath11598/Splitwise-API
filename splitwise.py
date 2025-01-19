import requests

# Splitwise API URL
BASE_URL = "https://secure.splitwise.com/api/v3.0"

# Replace with your Splitwise API key
API_KEY = "6iKwj4xWyPZmSh31oSb4EorwWcobGn266Y76765n"

def get_groups():
    """
    Fetches all groups from Splitwise.

    Returns:
        list: A list of groups with their IDs and names.
    """
    url = f"{BASE_URL}/get_groups"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        groups = response.json().get("groups", [])
        return [{"id": group["id"], "name": group["name"]} for group in groups]
    else:
        print("Error fetching groups:", response.status_code, response.text)
        return None

def add_transaction_to_group(group_id, cost, description):
    """
    Adds a transaction to a Splitwise group, splitting the cost equally.

    Args:
        group_id (int): The ID of the group.
        cost (float): The total cost of the transaction.
        description (str): A description of the transaction.

    Returns:
        dict: The response from the Splitwise API.
    """
    url = f"{BASE_URL}/create_expense"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "group_id": group_id,
        "cost": cost,
        "description": description,
        "split_equally": True  # This ensures the amount is split equally among group members
    }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error adding transaction:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    # Step 1: Fetch all groups and display them
    print("Fetching your Splitwise groups...")
    # groups = get_groups()
    
    # if groups:
    #     print("\nYour groups:")
    #     for group in groups:
    #         print(f"ID: {group['id']}, Name: {group['name']}")
        
    #     # Step 2: Ask the user to select a group ID
    #     try:
    #         group_id = int(input("\nEnter the Group ID to add a transaction: "))
    #     except ValueError:
    #         print("Invalid input. Please enter a valid Group ID.")
    #         exit()

    #     # Step 3: Ask for transaction details
    #     try:
    #         cost = float(input("Enter the total cost of the transaction: "))
    #         description = input("Enter a description for the transaction: ")
    #     except ValueError:
    #         print("Invalid cost. Please enter a numeric value.")
    #         exit()

    #     # Step 4: Add the transaction
    #     print("\nAdding transaction...")
    result = add_transaction_to_group(66875995, 10, "Temp Trx")
        
    if result:
        print("Transaction added successfully!")
    else:
        print("Failed to add the transaction.")
    # else:
    #     print("No groups found or an error occurred.")
