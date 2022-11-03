import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_options() -> Options:
    """Setup chrome options and return this object"""
    options: Options = Options()
    options.add_argument('chrome')  # Run in "headless" mode, if not need a browser UI
    options.add_argument('--start-maximized')  # Starts the browser maximized, regardless of any previous settings
    return options


@pytest.fixture
def get_web_driver(get_chrome_options) -> webdriver:
    """Making web driver with our setup options"""
    options: Options = get_chrome_options  # get chrome options
    driver: webdriver = webdriver.Chrome(options=options, executable_path=r'../drivers/chromedriver.exe')
    return driver


@pytest.fixture(scope='function')
def setup(request, get_web_driver: webdriver):
    """Get request and our web driver and """
    driver: webdriver = get_web_driver  # get driver
    url: str = 'https://www.a1.by/ru/shop/c/phones'  # url of testable site
    if request.cls is not None:  # if our test written in class
        request.cls.driver = driver
    driver.get(url)  # get request to start page
    yield driver
    driver.quit()  # close chrome
