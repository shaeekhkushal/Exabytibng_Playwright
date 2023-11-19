import pytest
import utils.read_utility as reader
from pages.header_po import Header
from utils.actions import Action

test_data_link = '../test_data/header_data.csv'


@pytest.mark.header
def test_user_will_click_on_the_logo(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    header_obj = Header(page)
    action_obj = Action(page)
    header_obj.click_on_logo()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_our_expertise(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    header_obj = Header(page)
    action_obj = Action(page)
    header_obj.click_service()
    header_obj.click_our_expertise()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_will_click_on_development_practices(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    header_obj = Header(page)
    action_obj = Action(page)
    header_obj.click_service()
    header_obj.click_development_practices()
    action_obj.verify_current_url()


@pytest.mark.header
def test_user_wil_click_on_fin_tech(set_up) -> None:
    csv_data = reader.read_test_data(test_data_link, Action.get_current_test_name())
    var = csv_data[0], csv_data[1]
    page = set_up
    header_obj = Header(page)
    action_obj = Action(page)
    header_obj.click_industries()
    header_obj.click_fin_tech()
    action_obj.verify_current_url()
