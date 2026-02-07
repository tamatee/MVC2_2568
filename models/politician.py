import csv
import os

class Politician:
    def __init__(self, politician_id, name, party):
        self.politician_id = politician_id
        self.name = name
        self.party = party

    def __str__(self):
        return f"Politician(id={self.politician_id}, name='{self.name}', party='{self.party}')"

class PoliticianRepository:
    def __init__(self, filename='database/politicians.csv'):
        self.filename = filename
        self.politicians = []
        self.ensure_database_directory()
        self.load_politicians()

    def ensure_database_directory(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'party'])

    def load_politicians(self):
        self.politicians = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                try:
                    next(reader) 
                except StopIteration:
                    pass
                for row in reader:
                    if row and len(row) >= 3:
                        self.politicians.append(Politician(row[0], row[1], row[2]))

    def save_politicians(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'party'])
            for p in self.politicians:
                writer.writerow([p.politician_id, p.name, p.party])

    def generate_id(self):
        existing_ids = [10000000]
        for p in self.politicians:
            try:
                existing_ids.append(int(p.politician_id))
            except (ValueError, TypeError):
                continue
        
        max_id = max(existing_ids)
        return str(max_id + 1)

    def add_politician(self, politician_id, name, party):
        politician = Politician(politician_id, name, party)
        self.politicians.append(politician)
        self.save_politicians()
        return politician

    def get_all_politicians(self):
        return sorted(self.politicians, key=lambda x: int(x.politician_id))
    
    def get_politician_by_id(self, politician_id):
        for p in self.politicians:
            if p.politician_id == politician_id:
                return p
        return None
