import csv
import os

class Promise:
    def __init__(self, promise_id, politician_id, description, date_announced, status):
        self.promise_id = promise_id
        self.politician_id = politician_id
        self.description = description
        self.date_announced = date_announced
        self.status = status

    def __str__(self):
        return f"Promise(id={self.promise_id}, politician_id={self.politician_id}, status='{self.status}')"

class PromiseRepository:
    def __init__(self, filename='database/promises.csv'):
        self.filename = filename
        self.promises = []
        self.ensure_database_directory()
        self.load_promises()

    def ensure_database_directory(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['promise_id', 'politician_id', 'description', 'date_announced', 'status'])

    def load_promises(self):
        self.promises = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                try:
                    next(reader) 
                except StopIteration:
                    pass
                for row in reader:
                    if row and len(row) >= 5:
                        self.promises.append(Promise(row[0], row[1], row[2], row[3], row[4]))

    def save_promises(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['promise_id', 'politician_id', 'description', 'date_announced', 'status'])
            for p in self.promises:
                writer.writerow([p.promise_id, p.politician_id, p.description, p.date_announced, p.status])

    def generate_id(self):
        if not self.promises:
            return "1"
        max_id = 0
        for p in self.promises:
            try:
                pid = int(p.promise_id)
                if pid > max_id:
                    max_id = pid
            except ValueError:
                continue
        return str(max_id + 1)

    def add_promise(self, politician_id, description, date_announced, status):
        promise_id = self.generate_id()
        promise = Promise(promise_id, politician_id, description, date_announced, status)
        self.promises.append(promise)
        self.save_promises()
        return promise

    def get_all_promises(self):
        return self.promises

    def get_promises_by_politician(self, politician_id):
        return [p for p in self.promises if p.politician_id == politician_id]

    def get_promise_by_id(self, promise_id):
        for p in self.promises:
            if p.promise_id == promise_id:
                return p
        return None

    def get_all_promises_sorted_by_id(self):
        return sorted(self.promises, key=lambda x: int(x.promise_id))

    def get_all_promises_sorted_by_date(self):
        # Assumes date format YYYY-MM-DD for correct string sorting
        return sorted(self.promises, key=lambda x: x.date_announced)
