# In-Memory Database for Transactions

This repository contains an implementation of an in-memory key-value database with transaction support, built in Python. 

## Features

- In-memory storage of key-value pairs (string key, integer values)
- Transaction support with commit and rollback functions
- Error handling for transaction violactions

## How to Run

Prerequisites
- Python 3.6 or higher

Running the Code:
- Clone this repository:
  
  `git clone https://github.com/yourusername/in-memory-database.git`
  
   `cd in-memory-database`

- Run the main script to test the database implementation:
  `python database.py`

- To use the database in your own Python code:
  ```python
  from database import database
  # Create a new database instance
  db = database()

  # Start a transaction
  db.begin_transaction()

  # Add or update keys
  db.put("key1", 100)
  db.put("key2", 200)

  # Commit changes
  db.commit()

  # Retrieve values
  value = db.get("key1")  # Returns 100
  ```
## Testing:
The code includes a basic test flow that demonstrates all functionality. You can modify the test cases in the 
database.py file or create your own test script that imports the database class.

## Assignment Improvement Suggestions:
To improve this assignment for future use, I recommend adding requirements for specific test cases in the instructions
rather than just examples to make grading easier. I would also recommend adding a requirement for basic performance metrics in the form of big-O to help students
understand the efficient implications of their implementation choices. These choices would also show real-world impact for run-time performance, an important aspect to think about when creating actual databases.
