class PoliticianView:
    def show_menu(self):
        print("\n--- Politician Management ---")
        print("1. Add Politician")
        print("2. List Politicians")
        print("3. View Politician Detail") 
        print("4. Back to Main Menu")
        return input("Enter your choice: ")

    def get_politician_input(self):
        name = input("Enter Name: ")
        party = input("Enter Party: ")
        return name, party

    def show_politicians(self, politicians):
        print("\n--- List of Politicians ---")
        if not politicians:
            print("No politicians found.")
        else:
            print(f"{'ID':<15} {'Name':<30} {'Party'}")
            print("-" * 60)
            for p in politicians:
                print(f"{p.politician_id:<15} {p.name:<30} {p.party}")

    def get_politician_id(self):
        return input("Enter Politician ID: ")

    def show_politician_detail(self, politician, promises):
        print("\n--- Politician Profile ---")
        print(f"ID: {politician.politician_id}")
        print(f"Name: {politician.name}")
        print(f"Party: {politician.party}")
        
        print("\n--- Promises ---")
        if not promises:
            print("No promises made yet.")
        else:
            for p in promises:
                print(f"- [{p.status}] {p.description} (Announced: {p.date_announced})")

    def show_message(self, message):
        print(f"\n{message}")
