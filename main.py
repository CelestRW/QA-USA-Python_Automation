import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        #Add in S8
        print("Function created for set route")
        pass
    def test_select_plan(self):
        #Add in S8
        print("Function created for select plan")
        pass
    def test_fill_phone_number(self):
        #Add in S8
        print("Function created for fill phone number")
        pass
    def test_fill_card(self):
        #Add in S8
        print("Function created for fill card")
        pass
    def test_comment_for_driver(self):
        #Add in S8
        print("Function created for comment for driver")
        pass
    def test_order_blanket_and_handkerchiefs(self):
        #Add in S8
        print("FUnction created for ordering blanket and handkerchiefs")
        pass
    def test_order_2_ice_cream(self):
        #Add in S8
        print("Function created for ordering 2 ice creams")
        pass
    def test_car_search_model_appears(self):
        #Add in S8
        print("Function created for checking car model appears")
        pass
    def test_order_2_ice_creams(self):
        # This test will eventually automate ordering two ice creams using Selenium
        # For now, we'll prepare the structure with a loop
        for i in range(2):
            #Add in S8
            pass
