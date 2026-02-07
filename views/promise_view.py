from utils.input_helper import get_valid_string, get_valid_integer, get_valid_date, get_valid_choice

class PromiseView:
    def show_menu(self):
        print("\n--- Promise Management ---")
        print("1. Add Promise")
        print("2. List Promises")
        print("3. Add Promise Update")
        print("4. View Promise Detail")
        print("5. Back to Main Menu")
        return input("Enter your choice: ")

    def get_promise_input(self):
        politician_id = str(get_valid_integer("Enter Politician ID: "))
        description = get_valid_string("Enter Promise Description: ")
        date_announced = get_valid_date("Enter Date Announced (YYYY-MM-DD): ")
        status = get_valid_choice("Enter Status (Not Started/In Progress/Silent): ", ["Not Started", "In Progress", "Silent"])
        return politician_id, description, date_announced, status

    def get_update_input(self):
        promise_id = str(get_valid_integer("Enter Promise ID to update: "))
        update_date = get_valid_date("Enter Update Date (YYYY-MM-DD): ")
        detail = get_valid_string("Enter Progress Detail: ")
        return promise_id, update_date, detail

    def get_update_detail_input(self):
        update_date = get_valid_date("Enter Update Date (YYYY-MM-DD): ")
        detail = get_valid_string("Enter Progress Detail: ")
        return update_date, detail

    def get_promise_id(self):
        return str(get_valid_integer("Enter Promise ID: "))

    def show_promises(self, promises):
        print("\n--- List of Promises ---")
        if not promises:
            print("No promises found.")
        else:
            for p in promises:
                print(p)

    def show_updates(self, updates):
        print("\n--- Promise Updates ---")
        if not updates:
            print("No updates found for this promise.")
        else:
            for u in updates:
                print(u)

    def show_promise_detail(self, promise, updates, politician_name):
        print("\n--- Promise Details ---")
        print(f"ID: {promise.promise_id}")
        print(f"Politician: {politician_name} (ID: {promise.politician_id})")
        print(f"Description: {promise.description}")
        print(f"Date Announced: {promise.date_announced}")
        print(f"Status: {promise.status}")
        
        print("\n--- Update History ---")
        if not updates:
            print("No updates recorded.")
        else:
            for u in updates:
                print(f"- [{u.update_date}] {u.progress_detail}")

    def show_sorted_promises(self, promises):
        print("\n--- All Promises (Sorted by Date) ---")
        if not promises:
            print("No promises found.")
        else:
            print(f"{'ID':<5} {'Date':<12} {'Status':<15} {'Description'}")
            print("-" * 60)
            for p in promises:
                print(f"{p.promise_id:<5} {p.date_announced:<12} {p.status:<15} {p.description}")

    def show_message(self, message):
        print(f"\n{message}")
