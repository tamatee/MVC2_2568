class UserView:
    def show_menu(self):
        print("\n--- User Management System ---")
        print("1. Add User")
        print("2. List Users")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def get_user_input(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/user): ")
        return username, email, password, role

    def show_users(self, users):
        print("\n--- List of Users ---")
        if not users:
            print("No users found.")
        else:
            # Sort locally for display if model doesn't sort
            sorted_users = sorted(users, key=lambda u: int(u.user_id))
            print(f"{'ID':<10} {'Username':<20} {'Role':<10} {'Email'}")
            print("-" * 60)
            for user in sorted_users:
                 print(f"{user.user_id:<10} {user.username:<20} {user.role:<10} {user.email}")

    def show_message(self, message):
        print(f"\n{message}")
