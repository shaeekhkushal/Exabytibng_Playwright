import pytest
import utils.read_utility as reader
from pages.footer_po import Footer
from utils.actions import Action

test_data_link = '../test_data/footer_data.csv'


@pytest.mark.header
def test_user_wil_click_on_fin_tech(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_fin_tech()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_health_tech(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_health_tech()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_ad_tech(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_ad_tech()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_process_automation(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_process_automation()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_about_us(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_about_us()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_join_us(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_join_us()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_contact_us(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    footer_obj = Footer(page)
    action_obj = Action(page)
    footer_obj.click_contact_us()
    action_obj.verify_current_url()
