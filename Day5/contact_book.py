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
# Starter Code
# class ContactNode:
#  def __init__(self, name, phone, email):
#  self.name=name; self.phone=phone; self.email=email
#  self.left=None; self.right=None
# class ContactBook:
#  def insert(self, name, phone, email): ...
#  def search(self, name): ...
#  def delete(self, name): ...
#  def list_all(self) -> list: ... # inorder
# Constraints
# • Insert uses name as key (alphabetical)
# • list_all must use inorder traversal
# • delete handles all 3 cases: leaf, 1 child, 2 children
# Bonus: Add height() and balance() methods.


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
                # Update existing contact
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

    # LIST ALL (ITERATIVE INORDER TRAVERSAL)
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

            child = current.left if current.left else current.right

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
            else:
                successor_parent.right = child

        return True
    

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

    print("\nContacts after deletion:")
    for name, phone, email in contacts.list_all():
        print(f"{name}: {phone}, {email}")


if __name__ == "__main__":
    main()