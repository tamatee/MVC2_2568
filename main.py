from models.user import UserRepository
from models.politician import PoliticianRepository
from models.campaign import CampaignRepository
from models.promise import PromiseRepository
from models.promise_update import PromiseUpdateRepository

from views.user_view import UserView
from views.main_view import MainView
from views.politician_view import PoliticianView
from views.campaign_view import CampaignView
from views.promise_view import PromiseView
from views.auth_view import AuthView

from controllers.auth_controller import AuthController
from controllers.user_controller import UserController
from controllers.politician_controller import PoliticianController
from controllers.promise_controller import PromiseController
from controllers.campaign_controller import CampaignController

def main():
    # Initialize Core Components
    main_view = MainView()
    auth_view = AuthView()

    # Initialize Views
    user_view = UserView()
    politician_view = PoliticianView()
    campaign_view = CampaignView()
    promise_view = PromiseView()

    # Initialize Models
    user_model = UserRepository()
    politician_model = PoliticianRepository()
    campaign_model = CampaignRepository()
    promise_model = PromiseRepository()
    promise_update_model = PromiseUpdateRepository()

    # Initialize Controllers
    auth_controller = AuthController(auth_view, user_model)
    user_controller = UserController(user_model, user_view)
    politician_controller = PoliticianController(politician_model, politician_view, promise_model)
    campaign_controller = CampaignController(campaign_model, campaign_view)
    promise_controller = PromiseController(promise_model, promise_update_model, promise_view, politician_model)

    # Login Loop
    while not auth_controller.is_logged_in():
        if not auth_controller.login():
            continue

    while True:
        choice = main_view.show_main_menu()
        
        if choice == '1':
            user_controller.run()
        elif choice == '2':
             politician_controller.run()
        elif choice == '3':
            campaign_controller.run()
        elif choice == '4':
            promise_controller.run()
        elif choice == '5':
            auth_controller.logout()
            while not auth_controller.is_logged_in():
                if not auth_controller.login():
                    continue
        else:
            main_view.show_message("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
