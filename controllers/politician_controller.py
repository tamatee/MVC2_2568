from models.politician import Politician

class PoliticianController:
    def __init__(self, model, view, promise_model):
        self.model = model
        self.view = view
        self.promise_model = promise_model

    def add_politician(self):
        name, party = self.view.get_politician_input()
        politician = self.model.add_politician(name, party)
        self.view.show_message(f"Politician '{name}' added successfully with ID {politician.politician_id}!")

    def show_politicians(self):
        politicians = self.model.get_all_politicians()
        self.view.show_politicians(politicians)

    def view_politician_detail(self):
        pid = self.view.get_politician_id()
        politician = self.model.get_politician_by_id(pid)
        if politician:
            promises = self.promise_model.get_promises_by_politician(pid)
            self.view.show_politician_detail(politician, promises)
        else:
            self.view.show_message("Politician not found.")

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.add_politician()
            elif choice == '2':
                self.show_politicians()
            elif choice == '3':
                self.view_politician_detail()
            elif choice == '4':
                break
            else:
                self.view.show_message("Invalid selection. Please try again.")
