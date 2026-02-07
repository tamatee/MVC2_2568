class AuthView:
    def get_login_input(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def show_message(self, message):
        print(f"\n{message}")
