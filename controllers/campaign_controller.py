from models.campaign import Campaign

class CampaignController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_campaign(self):
        year, constituency = self.view.get_campaign_input()
        campaign = self.model.add_campaign(year, constituency)
        self.view.show_message(f"Campaign added successfully with ID {campaign.campaign_id}!")

    def show_campaigns(self):
        campaigns = self.model.get_all_campaigns()
        self.view.show_campaigns(campaigns)

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.add_campaign()
            elif choice == '2':
                self.show_campaigns()
            elif choice == '3':
                break
            else:
                self.view.show_message("Invalid selection. Please try again.")
