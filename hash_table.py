
class Contact:
    """
    Contact class to represent a contact with a name and number.
    """

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    """
    Node class to represent a single entry in the hash table.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    HashTable class to represent a hash table for storing contacts.
    Uses separate chaining to handle collisions.
    """

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0

        for character in key:
            total += ord(character)

        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        contact = Contact(key, value)

        # If the index is empty, create a new node
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

        # Check the linked list for an existing contact
        current = self.data[index]

        while current is not None:
            # Update the number if the name already exists
            if current.key == key:
                current.value.number = value
                return

            if current.next is None:
                break

            current = current.next

        # Add the new contact to the linked list
        current.next = Node(key, contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end=" ")

            current = self.data[index]

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next

                print()


# Test your hash table implementation here.

table = HashTable(10)

# Print the empty table
print("Initial Hash Table:")
table.print_table()

# Insert contacts
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

print("\nHash Table After Inserting Contacts:")
table.print_table()

# Search for a contact
contact = table.search("John")
print("\nSearch result:", contact)

# Test collision handling
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

print("\nHash Table After Testing Collisions:")
table.print_table()

# Test duplicate contact names
table.insert("Rebecca", "999-444-9999")

print("\nHash Table After Updating Rebecca:")
table.print_table()

# Test searching for a contact that does not exist
print("\nSearching for Chris:", table.search("Chris"))

