import pytest

from pages.queue_management_page import QueueManagementPage
from pages.customer_search_page import CustomerSearchPage

@pytest.mark.smoke
def test_errors_on_customer_search(page, config):
    print(config["baseurl"])

    queue_mgmt_page = QueueManagementPage(page)

    queue_mgmt_page.navigate(config["baseurl"])

    if queue_mgmt_page.is_page_visible():
        queue_mgmt_page.select_left_nav("customer search")

    customer_search_page = CustomerSearchPage(page)

    if customer_search_page.is_page_visible():
        customer_search_page.click_search()
        customer_search_page.verify_error_message("CS-1435: Search contains invalid search criteria.")
        customer_search_page.verify_error_message("Last name, First name (opt), DOB (opt)")