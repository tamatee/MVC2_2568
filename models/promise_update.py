import csv
import os

class PromiseUpdate:
    def __init__(self, promise_id, update_date, progress_detail):
        self.promise_id = promise_id
        self.update_date = update_date
        self.progress_detail = progress_detail

    def __str__(self):
        return f"Update(promise={self.promise_id}, date={self.update_date}, detail='{self.progress_detail}')"

class PromiseUpdateRepository:
    def __init__(self, filename='database/promise_updates.csv'):
        self.filename = filename
        self.updates = []
        self.ensure_database_directory()
        self.load_updates()

    def ensure_database_directory(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['promise_id', 'update_date', 'progress_detail'])

    def load_updates(self):
        self.updates = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                try:
                    next(reader) 
                except StopIteration:
                    pass
                for row in reader:
                    if row and len(row) >= 3:
                        self.updates.append(PromiseUpdate(row[0], row[1], row[2]))

    def save_updates(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['promise_id', 'update_date', 'progress_detail'])
            for u in self.updates:
                writer.writerow([u.promise_id, u.update_date, u.progress_detail])

    def add_update(self, promise_id, update_date, progress_detail):
        update = PromiseUpdate(promise_id, update_date, progress_detail)
        self.updates.append(update)
        self.save_updates()
        return update

    def get_updates_by_promise(self, promise_id):
        return [u for u in self.updates if u.promise_id == promise_id]
    
    def get_all_updates(self):
        return self.updates
