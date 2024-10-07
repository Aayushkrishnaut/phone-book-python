class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None

class ContactNode:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None

class PhoneBook:
    def __init__(self):
        self.root = None
        self.contact_array = []

    def add_contact(self, name, number):
        new_contact = Contact(name, number)
        self.contact_array.append(new_contact)
        self._insert_to_tree(new_contact)
        print(f"Contact {name} added successfully.")

    def _insert_to_tree(self, contact):
        if not self.root:
            self.root = ContactNode(contact)
        else:
            self._insert_recursive(self.root, contact)

    def _insert_recursive(self, node, contact):
        if contact.name < node.contact.name:
            if node.left is None:
                node.left = ContactNode(contact)
            else:
                self._insert_recursive(node.left, contact)
        else:
            if node.right is None:
                node.right = ContactNode(contact)
            else:
                self._insert_recursive(node.right, contact)

    def search_contact(self, name):
        return self._search_recursive(self.root, name)

    def _search_recursive(self, node, name):
        if node is None or node.contact.name == name:
            return node
        if name < node.contact.name:
            return self._search_recursive(node.left, name)
        return self._search_recursive(node.right, name)

    def update_contact(self, name, new_number):
        node = self.search_contact(name)
        if node:
            node.contact.number = new_number
            for contact in self.contact_array:
                if contact.name == name:
                    contact.number = new_number
                    break
            return f"Contact {name} updated successfully."
        else:
            return f"Contact {name} not found."

    def delete_contact(self, name):
        self.root = self._delete_recursive(self.root, name)
        self.contact_array = [contact for contact in self.contact_array if contact.name != name]
        return f"Contact {name} deleted successfully."

    def _delete_recursive(self, node, name):
        if not node:
            return node
        if name < node.contact.name:
            node.left = self._delete_recursive(node.left, name)
        elif name > node.contact.name:
            node.right = self._delete_recursive(node.right, name)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.contact = temp.contact
            node.right = self._delete_recursive(node.right, temp.contact.name)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display_all_contacts(self):
        if self.contact_array:
            print("All Contacts:")
            self._inorder_traversal(self.root)
        else:
            print("Phone book is empty.")

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(f"{node.contact.name}: {node.contact.number}")
            self._inorder_traversal(node.right)

    def sort_contacts(self):
        self.contact_array.sort(key=lambda x: x.name)
        print("Contacts sorted successfully.")

    def create_linked_list(self):
        if not self.contact_array:
            return None
        head = self.contact_array[0]
        current = head
        for contact in self.contact_array[1:]:
            current.next = contact
            current = contact
        return head

    def display_linked_list(self):
        head = self.create_linked_list()
        if not head:
            print("Phone book is empty.")
            return
        print("Contacts as Linked List:")
        current = head
        while current:
            print(f"{current.name}: {current.number}")
            current = current.next

def main():
    phone_book = PhoneBook()

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Sort Contacts")
        print("7. Display as Linked List")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            phone_book.add_contact(name, number)

        elif choice == '2':
            name = input("Enter contact name to search: ")
            result = phone_book.search_contact(name)
            if result:
                print(f"Contact found: {result.contact.name}: {result.contact.number}")
            else:
                print(f"Contact {name} not found.")

        elif choice == '3':
            name = input("Enter contact name to update: ")
            new_number = input("Enter new contact number: ")
            print(phone_book.update_contact(name, new_number))

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            print(phone_book.delete_contact(name))

        elif choice == '5':
            phone_book.display_all_contacts()

        elif choice == '6':
            phone_book.sort_contacts()

        elif choice == '7':
            phone_book.display_linked_list()

        elif choice == '8':
            print("Thank you for using the Phone Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
