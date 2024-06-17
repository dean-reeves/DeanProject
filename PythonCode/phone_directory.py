class PhoneDirectory:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_number(self, name):
        return self.contacts.get(name, "Contact not found")

    def display_contacts(self):
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

def main():
    directory = PhoneDirectory()
    directory.add_contact("Alice", "123-456-7890")
    directory.add_contact("Bob", "098-765-4321")
    directory.display_contacts()
    print(directory.get_number("Alice"))

if __name__ == "__main__":
    main()
