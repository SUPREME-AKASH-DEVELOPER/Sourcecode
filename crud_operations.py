# crud_operations.py
# This script provides a basic CRUD (Create, Read, Update, Delete) functionality using Python.
# It simulates a simple in-memory database where each record is a dictionary inside a list.

# Sample in-memory "database" list
database = []

# Function to create a new record and add it to the database
def create_record(record):
    database.append(record)  # Adds the new record (a dictionary) to the database list
    print(f"Record created: {record}")

# Function to read all records from the database
def read_records():
    if database:
        print("Current database records:")
        for i, record in enumerate(database):
            print(f"{i+1}. {record}")
    else:
        print("The database is currently empty.")

# Function to update a specific record by index
def update_record(index, updated_record):
    if 0 <= index < len(database):
        print(f"Updating record at index {index}: {database[index]} -> {updated_record}")
        database[index] = updated_record  # Updates the record at the specified index
    else:
        print(f"Record at index {index} does not exist.")

# Function to delete a specific record by index
def delete_record(index):
    if 0 <= index < len(database):
        deleted_record = database.pop(index)  # Removes the record at the specified index
        print(f"Deleted record: {deleted_record}")
    else:
        print(f"Record at index {index} does not exist.")

# Sample Usage
if __name__ == "__main__":
    # Creating some records
    create_record({"name": "Alice", "age": 30, "occupation": "Engineer"})
    create_record({"name": "Bob", "age": 25, "occupation": "Designer"})
    create_record({"name": "Charlie", "age": 35, "occupation": "Manager"})
    
    # Reading the records
    read_records()

    # Updating Bob's occupation
    update_record(1, {"name": "Bob", "age": 25, "occupation": "Senior Designer"})

    # Reading the updated records
    read_records()

    # Deleting Alice's record
    delete_record(0)

    # Reading the final records
    read_records()

'''
Explanation of Functions:
-------------------------
1. **create_record(record)**: Adds a new record (a dictionary) to the `database` list.
   - Example: create_record({"name": "Alice", "age": 30, "occupation": "Engineer"})

2. **read_records()**: Prints all the records currently in the `database` list.
   - Example: read_records()

3. **update_record(index, updated_record)**: Updates a record at a specific index.
   - Example: update_record(1, {"name": "Bob", "age": 25, "occupation": "Senior Designer"})

4. **delete_record(index)**: Deletes a record at a specific index.
   - Example: delete_record(0)

Sample Output:
--------------
Record created: {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
Record created: {'name': 'Bob', 'age': 25, 'occupation': 'Designer'}
Record created: {'name': 'Charlie', 'age': 35, 'occupation': 'Manager'}
Current database records:
1. {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
2. {'name': 'Bob', 'age': 25, 'occupation': 'Designer'}
3. {'name': 'Charlie', 'age': 35, 'occupation': 'Manager'}
Updating record at index 1: {'name': 'Bob', 'age': 25, 'occupation': 'Designer'} -> {'name': 'Bob', 'age': 25, 'occupation': 'Senior Designer'}
Current database records:
1. {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
2. {'name': 'Bob', 'age': 25, 'occupation': 'Senior Designer'}
3. {'name': 'Charlie', 'age': 35, 'occupation': 'Manager'}
Deleted record: {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
Current database records:
1. {'name': 'Bob', 'age': 25, 'occupation': 'Senior Designer'}
2. {'name': 'Charlie', 'age': 35, 'occupation': 'Manager'}

Summary:
--------
This Python script simulates CRUD operations on a simple in-memory "database" represented as a list of dictionaries. 
It provides functions for creating, reading, updating, and deleting records.
'''
