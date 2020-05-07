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
        self.storage = [None] * self.capacity 
        self.size = 0
        self.resizing = False

    def get_load_factor(self):
        return self.size / self.capacity

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
        if self.get_load_factor() > 0.7:
            self.resize('p')

        # must hash the key to find the appropriate index in storage
        index = self.hash_index(key)
        # print('key', key, 'val', value, 'index', index)

        # must set the node, to easily iterate through linked list if collisions
        node = self.storage[index]

        # if there exists no other values at this index
        if node is None:
            # set storage at hashed index to the key,value tuple
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1
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
            self.size += 1



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
            self.size -= 1
            if prev is None:
                self.storage[index] = node.next
            else:
                prev.next = node.next
        if self.get_load_factor() < 0.2:
            self.resize('d')


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
        # while node is not None and key is not found
        while node is not None and key != node.key:
            # update node pointers
            node = node.next
        # then check if node is None:
        if node is None:
            # return none
            return None
        # otherwise, assumes key is found, so return value
        return node.value
        

    def resize(self, dir):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # double the capacity
        if dir == 'p':
            self.capacity *= 2
        else:
            self.capacity = self.capacity // 2
        self.size = 0
        # variable for old storage
        old_storage = self.storage
        # self.storage equal to a new empty array of size self.capacity
        self.storage = [None] * self.capacity

        # iterate through each index of array
        for arr_idx in old_storage:
            # instantiate the node to be the first element in specified array index
            node = arr_idx
            # iterate through each node in specified index, while it is not none
            while node is not None:
                # put the key, value of item into *new* storage
                self.put(node.key, node.value)
                node = node.next


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
