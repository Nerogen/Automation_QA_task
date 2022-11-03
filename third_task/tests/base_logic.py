from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseLogic:
    """Contain all necessary methods to testing ui part of testable site"""

    def __init__(self, driver: webdriver, max_wait_time: float, access_timing: float):
        self.driver: webdriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, max_wait_time, access_timing)

    def get_type_of_locator(self, find_by: str) -> dict:
        """Return type of locator for some element on page"""
        find_by = find_by.lower()
        locator_types = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locator_types[find_by]

    def check_needful_variant_of_payment(self, variants: list[str]) -> int:
        """Get variants list and search needful variant, then return pos of variant in list,
         if not find, raise exception with details"""
        position: int = 0  # pos of variant
        needful_variant: str = "6 мес по"  # constant variant
        for variant_number in range(len(variants)):
            if needful_variant in variants[variant_number]:
                position = variant_number
                break
            elif needful_variant not in variants[variant_number] and variant_number == len(variants) - 1:
                raise Exception("In drop down menu hasn't needful variant!")

        return position

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting visibility of element and return WebElement"""
        return self.wait.until(ec.visibility_of_element_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting when element become clickable and return WebElement"""
        return self.wait.until(ec.element_to_be_clickable((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting on element and return WebElement, if it is present in DOM tree"""
        return self.wait.until(ec.presence_of_element_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> list[WebElement]:
        """Waiting on elements and return WebElements, if they are visible"""
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> list[WebElement]:
        """Waiting on elements and return WebElements, if they are present in DOM tree"""
        return self.wait.until(ec.presence_of_all_elements_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)
