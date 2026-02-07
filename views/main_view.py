class MainView:
    def show_main_menu(self):
        print("\n=== Application (Admin Access) ===")
        print("1. Manage Users")
        print("2. Manage Politicians")
        print("3. Manage Campaigns")
        print("4. Manage Promises")
        print("5. Logout")
        
        choice = input("Select an option: ")
        return choice

    def show_message(self, message):
        print(f"\n{message}")
