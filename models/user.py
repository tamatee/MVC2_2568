import csv
import os

class User:
    def __init__(self, user_id, username, email, password, role="user"):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return f"User(id={self.user_id}, username='{self.username}', role='{self.role}')"

class UserRepository:
    def __init__(self, filename='database/users.csv'):
        self.filename = filename
        self.users = []
        self.ensure_database_directory()
        self.load_users()

    def ensure_database_directory(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'username', 'email', 'password', 'role'])

    def load_users(self):
        self.users = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                try:
                    next(reader) 
                except StopIteration:
                    pass
                for row in reader:
                    if row and len(row) >= 5:
                        self.users.append(User(row[0], row[1], row[2], row[3], row[4]))

    def save_users(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'username', 'email', 'password', 'role'])
            for user in self.users:
                writer.writerow([user.user_id, user.username, user.email, user.password, user.role])

    def generate_id(self):
        if not self.users:
            return "1"
        # improved logic to find max id
        max_id = 0
        for user in self.users:
            try:
                uid = int(user.user_id)
                if uid > max_id:
                    max_id = uid
            except ValueError:
                continue
        return str(max_id + 1)

    def add_user(self, username, email, password, role='user'):
        user_id = self.generate_id()
        user = User(user_id, username, email, password, role)
        self.users.append(user)
        self.save_users()
        return user

    def get_all_users(self):
        return self.users

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
