class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        # instantiate storage of specified capacity
        self.storage = [None] * self.capacity 

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_num = 5381
        for char in key:
            hash_num = ((hash_num << 5) + hash_num) + ord(char)
        return hash_num

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # must hash the key to find the appropriate index in storage
        index = self.hash_index(key)
        # print('key', key, 'val', value, 'index', index)

        # must set the node, to easily iterate through linked list if collisions
        node = self.storage[index]

        # if there exists no other values at this index
        if node is None:
            # set storage at hashed index to the key,value tuple
            self.storage[index] = HashTableEntry(key, value)
            return
        # otherwise
        # if there exists nodes at this index
        # iterate through all the nodes, while next is not None and node's key does not equal input key
        prev = node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # if the node's key matches the input key
        if prev.key == key:
            # update the node's value
            prev.value = value
            return
        else:
            # otherwise, create and insert a new HashTableEntry for the last node
            prev.next = HashTableEntry(key, value)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # hash the key to find the appropriate index in storage
        index = self.hash_index(key)
        # must set the node, to easily iterate through linked list if collisions
        node = self.storage[index]

        # if there exists data at this node
        # loop through all nodes, until you get a key that matches or node is None
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # if there is nothing, return warning
        if node is None:
            return 'Warning: key not found'
        # if key matches, delete the node entirely
        # if node.key == key:
        else:
            if prev is None:
                self.storage[index] = node.next
                # node = node.next
            else:
                prev.next = node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # must hash the key to find the appropriate index in storage
        index = self.hash_index(key)
        # must set a node variable, so it's easy to iterate if there is a collision
        node = self.storage[index]
        # if there is nothing at given index, then return None
        if self.storage[index] is None:
            return None
        # otherwise
        # prev = node
        # while node is not None and key is not found
        while node is not None and key != node.key:
            # update next and prev pointers
            # prev = node
            node = node.next
        # then check if node is None:
        if node is None:
            # return none
            return None
        # otherwise, assumes key is found, so return value
        return node.value
        

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # double the capacity
        self.capacity *= 2
        # create a new temp storage variable
        new_storage = [None] * self.capacity
        # rehash / copy all key/value pairs to new storage
        # iterate through all key, value tuples in the storage
        for key_val in self.storage:
            # if there exists values at the index
            if key_val is not None:
                # rehash key with new capacitys
                new_index = self.hash_index(key_val.key)
                # store key, value tuple at new hashed index
                new_storage[new_index] = HashTableEntry(key_val.key, key_val.value)
        # return the new storage / set it to self.storage
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
