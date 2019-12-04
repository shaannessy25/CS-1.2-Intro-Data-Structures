#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(N) in both cases because you have to obtain all the keys"""
        # Collect all keys in each bucket
        all_keys = []               
        for bucket in self.buckets:     # loops through every bucket
            for key, value in bucket.items():   #loops through every item in bucket
                all_keys.append(key)            #add the key to list
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(N) in both average and best case because you have to obtain all the keys"""
        all_values = []
        for bucket in self.buckets:     #loops through all the buckets
            for key, value in bucket.items():   #loops through all item in buckets
                all_values.append(value)        #adds value of each item to the listd

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(b*L) = O(n) in both average and best case scenario"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:     #loops through every bucket   
            all_items.extend(bucket.items())        #appends each item in bucket into a list
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(b*L) = O(N) in both best and average case"""
        count = 0   #counter variable
        for bucket in self.buckets:     # loops through buckets   
            for item in bucket.items(): #loops through every item in bucket
                count += 1      #updates the counter variable for each item in bucket
        return count


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(N) Worst Case last item in the traversed bucket
        Best Case one item in bucket O(1)"""
        bucket = self.buckets[hash(key) % len(self.buckets)]    #sets a bucket with a specified key
        for item_key, value in bucket.items():      #loops through items in bucket
            if item_key == key:     # if the specified key matches then return true else return false
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) in best case scenario and  O(n/b) in an average case where n is number of key/value pairs and b is number of b"""

        bucket = self.buckets[self._bucket_index(key)] #sets a bucket with a specified

        for item_key, value in bucket.items():  #loops through all buckets 
            if item_key == key:
                return value                    #Once the correct bucket with the item is found return the vale

        raise KeyError(f'Key not found: {key}')     #Raises an error for the user to see

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: 0(1) in best case scenario and O(n/b) for the average case"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item [0] == key)   #sets the node with a specific key

        if node is not None:                #if the node has an item in it then delete
            bucket.delete(node)             #deletes the node in the bucket

        bucket.append((key, value))         #if the node is empty the append the new node
 

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) in the best case scenario and O(n/b) in the average case scenario"""
        
        # bucket = self.buckets[hash(key) % len(self.buckets)]
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item[0] == key) #sets variable with specific 

        if node is not None:        #if item exist then delete bucket
            bucket.delete(node)
        else:
            raise KeyError(f'Key not found: {key}') #raises an error if the item is not found



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()