class MainView:
    def show_main_menu(self, role):
        print(f"\n=== Application (Role: {role}) ===")
        if role == 'admin':
            print("1. Manage Users")
            print("2. Manage Politicians")
            print("3. Manage Campaigns")
            print("4. Manage Promises")
            print("5. Logout")
        else:
            print("1. List Politicians")
            print("2. List Promises")
            print("3. Logout")
        
        choice = input("Select an option: ")
        return choice

    def show_message(self, message):
        print(f"\n{message}")
