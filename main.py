import pytest
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages import UrbanRoutesPage
import helpers
import data

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument("--start-maximized")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)
        else:
            raise Exception("URL not reachable")

        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_address(self):
        self.page.set_from(data.address_from)
        self.page.set_to(data.address_to)
        self.page.click_call_a_taxi_button()
        time.sleep(1)  # Optional delay to observe UI response

    def test_select_plan(self):
        self.page.select_supportive_plan()
        assert self.page.is_supportive_plan_selected()

    def test_fill_phone_number(self):
        self.page.set_phone_number(data.phone_number)
        self.page.set_sms_code("0000")  # Assuming fake/test code works
        assert self.page.is_phone_number_set()

    def test_fill_card(self):
        self.page.click_add_card_button()
        self.page.set_card_number(data.card_number)
        self.page.set_card_expiry(data.card_expiry)
        self.page.set_card_code(data.card_code)
        self.page.click_link_button()
        assert self.page.is_card_added()

    def test_comment_for_driver(self):
        self.page.set_message_for_driver(data.message_for_driver)
        assert self.page.get_message_for_driver() == data.message_for_driver

    def test_order_blanket_and_handkerchiefs(self):
        self.page.click_blanket_and_handkerchiefs_slider()
        assert self.page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.page.order_ice_cream(2)
        assert self.page.get_ice_cream_count() == 2

    def test_car_search_modal_appears(self):
        self.page.click_order_button()
        assert self.page.is_car_search_modal_visible()
