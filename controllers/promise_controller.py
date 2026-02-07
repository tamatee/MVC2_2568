from models.promise import Promise
from models.promise_update import PromiseUpdate

class PromiseController:
    def __init__(self, promise_model, update_model, view, politician_model):
        self.promise_model = promise_model
        self.update_model = update_model
        self.view = view
        self.politician_model = politician_model

    def view_promise_detail_by_id(self, pid):
        promise = self.promise_model.get_promise_by_id(pid)
        if promise:
            updates = self.update_model.get_updates_by_promise(pid)

            politician = self.politician_model.get_politician_by_id(promise.politician_id)
            politician_name = politician.name if politician else "Unknown"
            
            self.view.show_promise_detail(promise, updates, politician_name)
        else:
            self.view.show_message("Promise not found.")

    def add_promise(self):
        pid, desc, date, status = self.view.get_promise_input()
        
        politician = self.politician_model.get_politician_by_id(pid)
        if not politician:
            self.view.show_message(f"Error: Politician ID {pid} not found. Cannot add promise.")
            return

        promise = self.promise_model.add_promise(pid, desc, date, status)
        self.view.show_message(f"Promise added successfully with ID {promise.promise_id}!")

    def show_promises(self):
        promises = self.promise_model.get_all_promises_sorted_by_date()
        self.view.show_sorted_promises(promises)

    def view_promise_detail(self):
        pid = self.view.get_promise_id()
        self.view_promise_detail_by_id(pid)

    def add_update(self):
        pid = self.view.get_promise_id()
        promise = self.promise_model.get_promise_by_id(pid)
        
        if not promise:
            self.view.show_message("Promise ID not found.")
            return

        if promise.status == "Silent":
            self.view.show_message("Cannot update a promise with status 'Silent'.")

            self.view_promise_detail_by_id(pid)
            return

        date, detail = self.view.get_update_detail_input()
        self.update_model.add_update(pid, date, detail)
        self.view.show_message(f"Update added for Promise {pid}!")
        
        self.view_promise_detail_by_id(pid)


    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.add_promise()
            elif choice == '2':
                self.show_promises()
            elif choice == '3':
                self.add_update()
            elif choice == '4':
                self.view_promise_detail()
            elif choice == '5':
                break
            else:
                self.view.show_message("Invalid selection. Please try again.")
