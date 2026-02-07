from models.user import User

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self):
        username, email, password, role = self.view.get_user_input()
        # ID is generated inside the model now
        user = self.model.add_user(username, email, password, role)
        self.view.show_message(f"User {username} added successfully with ID {user.user_id}!")

    def show_users(self):
        users = self.model.get_all_users()
        self.view.show_users(users)

    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.show_users()
            elif choice == '3':
                break
            else:
                self.view.show_message("Invalid choice. Please try again.")
