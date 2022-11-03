import random

import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from third_task.base.base_logic import BaseLogic


@pytest.mark.usefixtures("setup")
class TestUi:

    def test_for_phone_cards(self):
        """Test random phone card on 'go to purchase', 'drop-down menu', 'access and buy'"""
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        # get all buttons from phone cards
        phones: list[WebElement] = test_object.are_present("class_name", "button--primary")
        # choose random one
        phone = random.choice(phones)
        # go to element on page
        test_object.driver.execute_script("arguments[0].scrollIntoView();", phone)
        # go to phone card
        phone.click()

        # make selector object for select item
        menu: Select = Select(test_object.is_present('xpath', '//*[@id="priceBlock_selector_CURRENT_CONTRACT"]'))
        # get items from selector form
        variants: list[str] = [option.get_attribute("textContent") for option in menu.options]
        # get needful pos of item
        position: int = test_object.check_needful_variant_of_payment(variants)

        # select needful item, but this doesn't work, I don't known why
        # menu.select_by_visible_text(variants[position])

        # solving of selection item problem, find all options from select form
        options = test_object.are_present('tag_name', 'option')
        # get value attributes
        options = [option.get_attribute("value") for option in options]
        # configure url line for select item ;)
        test_object.driver.get(f"{test_object.driver.current_url}" + f"?productOffering={options[position]}")

        # forming a string of phone parameters
        phone_parameters: str = f'\nВыбран {test_object.is_present("class_name", "pdp-header-heading").text}'
        # forming a string of variant of paying
        variant_of_paying: str = f", вариант оплаты:{variants[position]}'"
        print(phone_parameters + variant_of_paying)

        # get current url of page
        page_url = test_object.driver.current_url

        # get button object to manipulation
        btn = test_object.is_clickable("xpath",
                                       '//*[@id="CURRENT_CONTRACT"]/div[1]/div[2]/div[3]/form/div[2]/div/button')
        # move to button element
        test_object.driver.execute_script("arguments[0].scrollIntoView();", btn)
        # go to redirect page
        btn.click()
        # check what previous url != current url
        assert page_url != test_object.driver.current_url
