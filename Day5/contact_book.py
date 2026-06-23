# BST -- Contact Book
# Binary Search Tree -> insert search inorder delete
# Phone contacts / address book
# Overview
# BST keyed alphabetically by contact name. 
# insert() walks left (name less) or right (name greater) to find the insertion point.
# list_all() uses inorder traversal (left-root-right) to return contacts in A-Z order automatically.
# delete() handles all three BST deletion cases.
# BSTs power database indexes and autocompletion systems.
# Problem
# BST contact book keyed alphabetically by name. Support insert, search, delete, and list all A-Z (inorder traversal).
# Constraints
# • Insert uses name as key (alphabetical)
# • list_all must use inorder traversal
# • delete handles all 3 cases: leaf, 1 child, 2 children
# Bonus: Add height() and balance() methods.

import random
import timeit


class ContactNode:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.left = None
        self.right = None


class ContactBook:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, name, phone, email):
        new_node = ContactNode(name, phone, email)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if name < current.name:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif name > current.name:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                # Updating existing contact
                current.phone = phone
                current.email = email
                return

    # SEARCH
    def search(self, name):
        current = self.root

        while current:
            if name == current.name:
                return current

            if name < current.name:
                current = current.left
            else:
                current = current.right

        return None 

    # LIST ALL
    def list_all(self):
        result = []
        stack = []
        current = self.root

        while stack or current:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            result.append(
                (current.name, current.phone, current.email)
            )

            current = current.right

        return result
    

# def preorder(self):
#     if self.root is None:
#         return []

#     result = []
#     stack = [self.root]

#     while stack:
#         current = stack.pop()

#         result.append(
#             (current.name, current.phone, current.email)
#         )

#         if current.right:
#             stack.append(current.right)

#         if current.left:
#             stack.append(current.left)

#     return result

    # DELETE
    def delete(self, name):
        parent = None
        current = self.root

        # Find node to delete
        while current and current.name != name:
            parent = current

            if name < current.name:
                current = current.left
            else:
                current = current.right 

        if current is None:
            return False

        # CASE 1 & 2: Node has 0 or 1 child
        if current.left is None or current.right is None:

            # child = current.left if current.left else current.right

            if current.left:
                child = current.left
            else:
                child = current.right

            if parent is None:
                self.root = child

            elif parent.left == current:
                parent.left = child

            else:
                parent.right = child

        # CASE 3: Node has 2 children
        else:
            successor_parent = current
            successor = current.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.name = successor.name
            current.phone = successor.phone                
            current.email = successor.email

            child = successor.right

            if successor_parent.left == successor:    
                successor_parent.left = child          
            else:                                                 # Go to the node's right child
                successor_parent.right = child                    # Keep moving left
                                                                  # Stop when there is no more left child
        return True
    

def benchmark():

    names = [f"User{i}" for i in range(1000)] # generates test data 
    random.shuffle(names) # shuffling the names inorder ot balance the tree 

    def build_contact_book():
        book = ContactBook() # creating an empty tree 

        for name in names:
            book.insert(
                name,
                "9999999999",
                f"{name}@mail.com"
            ) # inserts all contacts 

        return book 

    contacts = build_contact_book() #contact book object contains BST 
    context = globals() | locals()

    search_time = timeit.timeit(
        stmt='contacts.search("User500")',
        globals=context,
        number=10000
    )

    list_time = timeit.timeit(
        stmt='contacts.list_all()',
        globals=context,
        number=1000
    )

    insert_time = timeit.timeit(
        stmt='''
book = ContactBook() 
for name in names:
    book.insert(name, "9999999999", f"{name}@mail.com")
''', # creates a new tree 
        globals=context,
        number=100
    )

    delete_time = timeit.timeit(
        stmt='''
book = build_contact_book()
book.delete("User500")
''',
        globals=context,
        number=1000
    )

    print("\nBenchmark Results")
    print("-" * 30)
    print(f"Insert : {insert_time:.6f} sec")
    print(f"Search : {search_time:.6f} sec")
    print(f"Delete : {delete_time:.6f} sec")
    print(f"List   : {list_time:.6f} sec")
    print()
    print("Global keys:\n" ,globals().keys())
    print("Local keys:\n",locals().keys())

def main():
    contacts = ContactBook()

    # Insert contacts
    contacts.insert("John", "9876543210", "john@gmail.com")
    contacts.insert("Alice", "9123456780", "alice@gmail.com")
    contacts.insert("David", "9988776655", "david@gmail.com")
    contacts.insert("Bob", "9000011111", "bob@gmail.com")
    contacts.insert("Emma", "9111222233", "emma@gmail.com")
    contacts.insert("Sam", "9555666777", "sam@gmail.com")

    print("\nAll contacts (A-Z):")
    for name, phone, email in contacts.list_all():
        print(f"{name}: {phone}, {email}")

    # Search
    print("\nSearching for 'David':")
    contact = contacts.search("David")

    if contact:
        print(f"Found: {contact.name} - {contact.phone} - {contact.email}")
    else:
        print("Contact not found")

    # Delete leaf node
    print("\nDeleting 'Bob' (leaf node)")
    contacts.delete("Bob")

    # Delete node with one child
    print("Deleting 'Alice' (one child)")
    contacts.delete("Alice")

    # Delete node with two children
    print("Deleting 'David' (two children)")
    contacts.delete("David")

    print("Deleting Sam")
    contacts.delete("Sam")


    print("\nContacts after deletion:")
    for name, phone, email in contacts.list_all():
        print(f"{name}: {phone}, {email}")


if __name__ == "__main__":
    main()
    benchmark()
    




# list

# | Action     | Stack                | Result                                 |
# | ---------- | -------------------- | -------------------------------------- |
# | Push John  | `[John]`             | `[]`                                   |
# | Push Alice | `[John, Alice]`      | `[]`                                   |
# | Pop Alice  | `[John]`             | `[Alice]`                              |
# | Push David | `[John, David]`      | `[Alice]`                              |
# | Push Bob   | `[John, David, Bob]` | `[Alice]`                              |
# | Pop Bob    | `[John, David]`      | `[Alice, Bob]`                         |
# | Pop David  | `[John]`             | `[Alice, Bob, David]`                  |
# | Push Emma  | `[John, Emma]`       | `[Alice, Bob, David]`                  |
# | Pop Emma   | `[John]`             | `[Alice, Bob, David, Emma]`            |
# | Pop John   | `[]`                 | `[Alice, Bob, David, Emma, John]`      |
# | Push Sam   | `[Sam]`              | `[Alice, Bob, David, Emma, John]`      |
# | Pop Sam    | `[]`                 | `[Alice, Bob, David, Emma, John, Sam]` |


# benchmark()

# ├── globals()
# │   ├── ContactBook
# │   ├── ContactNode
# │   ├── random
# │   └── timeit
# │
# ├── locals()
# │   ├── names
# │   ├── contacts
# │   └── build_contact_book
# │
# └── context = globals() | locals()

# globals() and locals() do not improve speed or accuracy.
# They simply provide the variables that timeit() needs to run the code being measured.




# The smallest node in the right subtree (inorder successor)

# The largest node in the left subtree (inorder predecessor





