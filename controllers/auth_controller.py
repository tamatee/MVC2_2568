class AuthController:
    def __init__(self, view, user_repo):
        self.view = view
        self.user_repo = user_repo
        self.current_user = None

    def login(self):
        print("\n--- Login ---")
        username, password = self.view.get_login_input()

        user = self.user_repo.find_user_by_username(username)

        if user and user.password == password:
            self.current_user = {'username': user.username, 'role': user.role}
            self.view.show_message(f"Login successful! Welcome, {username} ({user.role}).")
            return True
        

        self.view.show_message("Invalid username or password.")
        return False

    def logout(self):
        self.current_user = None
        self.view.show_message("Logged out successfully.")

    def is_admin(self):
        return self.current_user and self.current_user["role"] == "admin"

    def is_logged_in(self):
        return self.current_user is not None
