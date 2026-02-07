from models.politician import PoliticianRepository
from models.promise import PromiseRepository
from models.user import UserRepository
from models.campaign import CampaignRepository
import os

def seed_data():
    # Initialize Repositories
    politician_repo = PoliticianRepository()
    promise_repo = PromiseRepository()
    user_repo = UserRepository()
    campaign_repo = CampaignRepository()

    # Clear existing data for a clean seed
    politician_repo.politicians = []
    politician_repo.save_politicians()
    promise_repo.promises = []
    promise_repo.save_promises()
    user_repo.users = []
    user_repo.save_users()
    campaign_repo.campaigns = []
    campaign_repo.save_campaigns()

    print("Seeding Politicians...")
    # 5 Politicians
    politicians_data = [
        ("Somsak Jaidee", "Pracharat"),
        ("Mana Rakchart", "Puea Thai"),
        ("Piti Gingeng", "Move Forward"),
        ("Chujai Meeboon", "Democrat"),
        ("Malee Suayngam", "Bhumjaithai")
    ]

    created_politicians = []
    for name, party in politicians_data:
        pid = politician_repo.generate_id()
        p = politician_repo.add_politician(pid, name, party)
        created_politicians.append(p)
        print(f"Added Politician: {p.name} (ID: {p.politician_id})")

    print("\nSeeding Promises...")
    # 10 Promises
    promises_data = [
        (created_politicians[0].politician_id, "Increase minimum wage to 500 THB", "2025-05-01", "In Progress"),
        (created_politicians[0].politician_id, "Reduce electricity bills", "2025-06-01", "Not Started"),
        (created_politicians[1].politician_id, "Free education for all", "2025-05-15", "Silent"),
        (created_politicians[1].politician_id, "Build high-speed train", "2025-07-01", "In Progress"),
        (created_politicians[2].politician_id, "Reform military", "2025-05-20", "In Progress"),
        (created_politicians[2].politician_id, "Decentralize power", "2025-08-01", "Not Started"),
        (created_politicians[3].politician_id, "Subsidize rubber prices", "2025-05-10", "Silent"),
        (created_politicians[3].politician_id, "Clean water for every village", "2025-09-01", "Not Started"),
        (created_politicians[4].politician_id, "Legalize cannabis for medical use", "2025-04-01", "Silent"),
        (created_politicians[4].politician_id, "Improve healthcare facilities", "2025-10-01", "In Progress")
    ]

    for pid, desc, date, status in promises_data:
        promise = promise_repo.add_promise(pid, desc, date, status)
        print(f"Added Promise: {desc} [{status}] (ID: {promise.promise_id})")
        
    print("\nSeeding Users...")
    users_data = [
        ("user1", "user1@example.com", "1234"),
        ("user2", "user2@example.com", "1234"),
        ("user3", "user3@example.com", "1234")
    ]
    
    for username, email, password in users_data:
        u = user_repo.add_user(username, email, password)
        print(f"Added User: {u.username}")

    print("\nSeeding Campaigns...")
    campaigns_data = [
        ("2025", "Bangkok District 1"),
        ("2025", "Chiang Mai District 1"),
        ("2025", "Khon Kaen District 2"),
        ("2025", "Phuket District 1"),
        ("2025", "Chonburi District 3")
    ]

    for year, constituency in campaigns_data:
        c = campaign_repo.add_campaign(year, constituency)
        print(f"Added Campaign: {c.election_year} - {c.constituency} (ID: {c.campaign_id})")


    print("\nSeed data created successfully!")

if __name__ == "__main__":
    seed_data()
