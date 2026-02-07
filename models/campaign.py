import csv
import os

class Campaign:
    def __init__(self, campaign_id, election_year, constituency):
        self.campaign_id = campaign_id
        self.election_year = election_year
        self.constituency = constituency

    def __str__(self):
        return f"Campaign(id={self.campaign_id}, year={self.election_year}, constituency='{self.constituency}')"

class CampaignRepository:
    def __init__(self, filename='database/campaigns.csv'):
        self.filename = filename
        self.campaigns = []
        self.ensure_database_directory()
        self.load_campaigns()

    def ensure_database_directory(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'election_year', 'constituency'])

    def load_campaigns(self):
        self.campaigns = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                try:
                    next(reader) 
                except StopIteration:
                    pass
                for row in reader:
                    if row and len(row) >= 3:
                        self.campaigns.append(Campaign(row[0], row[1], row[2]))

    def save_campaigns(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'election_year', 'constituency'])
            for c in self.campaigns:
                writer.writerow([c.campaign_id, c.election_year, c.constituency])

    def generate_id(self):
        if not self.campaigns:
            return "1"
        max_id = 0
        for c in self.campaigns:
            try:
                cid = int(c.campaign_id)
                if cid > max_id:
                    max_id = cid
            except ValueError:
                continue
        return str(max_id + 1)

    def add_campaign(self, election_year, constituency):
        campaign_id = self.generate_id()
        campaign = Campaign(campaign_id, election_year, constituency)
        self.campaigns.append(campaign)
        self.save_campaigns()
        return campaign

    def get_all_campaigns(self):
        return self.campaigns
