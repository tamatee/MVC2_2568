class CampaignView:
    def show_menu(self):
        print("\n--- Campaign Management ---")
        print("1. Add Campaign")
        print("2. List Campaigns")
        print("3. Back to Main Menu")
        return input("Enter your choice: ")

    def get_campaign_input(self):
        year = input("Enter Election Year: ")
        constituency = input("Enter Constituency: ")
        return year, constituency

    def show_campaigns(self, campaigns):
        print("\n--- List of Campaigns ---")
        if not campaigns:
            print("No campaigns found.")
        else:
            sorted_campaigns = sorted(campaigns, key=lambda c: int(c.campaign_id))
            print(f"{'ID':<10} {'Year':<10} {'Constituency'}")
            print("-" * 50)
            for c in sorted_campaigns:
                print(f"{c.campaign_id:<10} {c.election_year:<10} {c.constituency}")

    def show_message(self, message):
        print(f"\n{message}")
