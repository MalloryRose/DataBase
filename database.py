class database:

    def __init__(self):
        self.main_database = dict() # main dictionary
        self.changes = dict() # dictionary to store the current changes in the current transaction
        self.size = 0
        self.transaction = False # track if a transaction is going on
        
        

    def begin_transaction(self):
        # starts a new transaction
        # at a time, only one transaction can happen
        
        if self.transaction:
            raise Exception("Transaction already in progress")
        
        self.transaction = True
        self.changes.clear()
        print("Transaction started")

    def put(self, key, value):
        # keys are string, values are integers
        # if a key doesn't exist, create a new key with the provided value 
        # otherwise update the value of an existing key
        
        if self.transaction:
            self.changes[key] = value 
        else:
            raise Exception("No transaction in progress")
            
        
        

    def get(self, key):
        # return the value associated with the key 
        # or null if doesn't exist

        #only return the committed stuff, in the main database
        if key in self.main_database:
            return self.main_database[key]
        else:
            print("Error: No key exists in the database")
            return None
            
        

    def commit(self):
        # applies changes made within the transaction too the main state
        # allowing any future gets() to "see" the changes made within the transaction
        
        # merge the changes dictionary to the main_database dictionary
        
        if self.transaction:
            # check that there are changes
            if self.changes:
                for key, value in self.changes.items():
                  
                        self.main_database[key] = value
                
            
        
            #end the transaction
            self.transaction = False
            self.changes.clear()
            
            print("Changes have been committed to the main database")
        else:
            raise Exception("No transaction in progress")
            
        

    def rollback(self):
        # should aborts all changes made within the transaction and everything
        # should go back to the way it was before
        if self.transaction:
            self.changes.clear() 
            self.transaction = False
        else:
              raise Exception("No transaction in progress")



newDatabase = database()




