# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Basically does same thing, but not best practices
        # index = hash(key) % self.capacity
        # index = _hash_mod(key)

        # index = self._hash_mod(key)

        # if self.storage[index] is not None:
        #     print(f'WARNING: collision has occured at {index}')

        # else:
        #     self.storage[index] = (key, value)

        # return

        pair = LinkedPair(key, value)
        hash_key = self._hash_mod(key)
        head = self.storage[hash_key]

        # if hash is empty
        if not head:
            self.storage[hash_key] = pair

        else:
            if head.key == key:
                pair.next = head.next
                self.storage[hash_key] = pair

            else:
                while head:

                    if not head.next:
                        head.next = pair
                        break

                    elif head.next.key == key:
                        pair.next = head.next.next
                        head.next = pair
                        break

                    else:
                        head = head.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)

        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         self.storage[index] = None
        #     else:
        #         print(f'WARNING: collision has occured at {index}')

        # else:
        #     print(f'Warning key ({key}) not found.')

        # return

        index = self._hash_mod(key)

        if self.storage[index] is not None:
            node = self.storage[index]
            count = 0
            while node:

                if count == 0:
                    count += 1

                    if node.key == key:
                        self.storage[index] = node.next
                        break

                else:
                    if node.next:
                        if node.next.key == key:
                            node.next = node.next.next
                            break

                        else:
                            node = node.next

                    else:
                        return 'No key'

            return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         return self.storage[index][1]
        #     else:
        #         print(f'WARNING: collision has occured at {index}')

        # else:
        #     return None

        # return

        if self.storage[index]:
            node = self.storage[index]
            while node:
                if node.key == key:
                    return node.value
                else:
                    node = node.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        # self.storage = [None] * self.capacity

        # for item in old_storage:
        #     self.insert(item[0], item[1])
        bigger_table = HashTable(self.capacity)
        for node in self.storage:
            while node:
                index = self._hash_mod(node.key)
                bigger_table.insert(node.key, node.value)
                node = node.next

        self.storage = bigger_table.storage


if __name__ == "__main__":
    # ht1 = HashTable(2)

    # ht1.insert('key1', 'hello')
    # ht1.insert('key2', 'goodbye')
    # ht1.remove('key1')

    # print(ht1.storage)
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
