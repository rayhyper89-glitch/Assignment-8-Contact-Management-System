# Step 1: Contact Class

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

# Step 2: Node Class

class Node:
    def __init__(self, key, value):
        self.key = key              # contact name
        self.value = value          # Contact object
        self.next = None            # next Node (for chaining)

    def __str__(self):
        return str(self.value)

# Step 3: HashTable Class

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        """Simple hash function that sums character codes and mods by size"""
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        """Insert or update a contact"""
        index = self.hash_function(key)
        contact = Contact(key, number)

        # If no node exists at this index, place new node
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

       
        current = self.data[index]
        while current:
            if current.key == key:
               
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next

        current.next = Node(key, contact)

    def search(self, key):
        """Search for a contact by name"""
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        """Print the structure of the hash table"""
        for i in range(self.size):
            print(f"Index {i}:", end=" ")

            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n--- Adding contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Searching for John ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Testing collisions ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # May collide with Amy
    table.print_table()

    print("\n--- Updating existing contact (duplicate key) ---")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n--- Searching for non-existent contact ---")
    print(table.search("Chris")) 
