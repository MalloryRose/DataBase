class database:

    def __init__(self):
        pass

    def begin_transaction():
        # starts a new transaction
        pass

    def put(key, value):
        # keys are string, values are integers
        # if a key doesn't exist, create a new key with the provided value 
        # otherwise update the value of an existing key
        pass

    def get(key):
        # return the value associated with the key 
        # or null if doesn't exist
        
        pass

    def commit():
        # applies changes made within the transaction too the main state
        # allowing any future gets() to "see" the changes made within the transaction
        pass

    def rollback():
        # should aborts all changes made within the transaction and everything
        # should go back to the way it was before
        pass 


# if put is called when a transaction is not in progress, throw exception

# get(key) can be called anytime even when a transaction is not in progress

# only a single transaction may exist at a time

# Within a transaction you can make as many changes to as many keys as you like.
#However, they should not be “visible” to get(), until the transaction is committed

newDatabase = database()


