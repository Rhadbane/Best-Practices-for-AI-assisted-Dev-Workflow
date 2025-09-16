# data_processor.py

import json

# This function is a bit messy and could be improved.
def process_user_data(file_path):
    # It reads a json file, filters for active users, and gets their names.
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

    active_users = []
    for user in data['users']:
        if user['isActive'] == True:
            active_users.append(user)

    user_names = []
    for user in active_users:
        user_names.append(user['name'])

    return user_names

# Example usage:
# users_data.json content:
# {
#   "users": [
#     {"id": 1, "name": "Alice", "isActive": true},
#     {"id": 2, "name": "Bob", "isActive": false},
#     {"id": 3, "name": "Charlie", "isActive": true}
#   ]
# }
#
# names = process_user_data('users_data.json')
# print(names) # Expected output: ['Alice', 'Charlie']
