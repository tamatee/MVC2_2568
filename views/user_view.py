from utils.input_helper import get_valid_string, get_valid_choice

class UserView:
    def show_menu(self):
        print("\n--- User Management System ---")
        print("1. Add User")
        print("2. List Users")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def get_user_input(self):
        username = get_valid_string("Enter username: ")
        email = get_valid_string("Enter email: ")
        password = get_valid_string("Enter password: ")
        return username, email, password

    def show_users(self, users):
        print("\n--- List of Users ---")
        if not users:
            print("No users found.")
        else:
            # Sort locally for display if model doesn't sort
            sorted_users = sorted(users, key=lambda u: int(u.user_id))
            print(f"{'ID':<10} {'Username':<20} {'Email'}")
            print("-" * 60)
            for user in sorted_users:
                 print(f"{user.user_id:<10} {user.username:<20} {user.email}")

    def show_message(self, message):
        print(f"\n{message}")
