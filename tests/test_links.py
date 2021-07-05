from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import DRIVER_HOME, LINKS
import unittest


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        # Step 1) Open Chrome
        self.drivers = dict()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # self.driver = webdriver.Ie(IEDriverManager().install())
        # self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())

        # Wait implicitly for elements to be ready before attempting interactions
        self.driver.implicitly_wait(10)

    def test_data_spaces(self):
        page = 'fiware-for-data-spaces'
        name = 'happyforms-92014_single_line_text_1'
        surname = 'happyforms-92014_single_line_text_18'
        email = 'happyforms-92014_email_2'
        checkbox = 'happyforms-92014_legal_29'

        self.__happy_forms__(page=page,
                             name=name,
                             surname=surname,
                             email=email,
                             checkbox=checkbox)

    def test_digital_twins(self):
        page = 'fiware-for-digital-twins'
        name = 'happyforms-92143_single_line_text_1'
        surname = 'happyforms-92143_single_line_text_18'
        email = 'happyforms-92143_email_2'
        checkbox = 'happyforms-92143_legal_29'

        self.__happy_forms__(page=page,
                             name=name,
                             surname=surname,
                             email=email,
                             checkbox=checkbox)

    def __happy_forms__(self, page, name, surname, email, checkbox):
        link = LINKS[page]

        # Step 2) Navigate to fiware.org
        self.driver.get(link['url'])

        # Step 3) Search elements to put data
        name = self.driver.find_element_by_id(name)
        assert name is not None

        surname = self.driver.find_element_by_id(surname)
        assert surname is not None

        email = self.driver.find_element_by_id(email)
        assert email is not None

        checkbox = self.driver.find_element_by_id(checkbox)
        assert checkbox is not None

        # <input type="submit" class="happyforms-submit happyforms-button--submit " value="Get your copy">
        submit = self.driver.find_element_by_xpath("//input[@value='Get your copy']")
        assert submit is not None

        name.send_keys("test")
        surname.send_keys("test")
        email.send_keys("test@test.test")

        # Step 4) Click checkbox and submit
        actions = ActionChains(self.driver)
        assert actions is not None

        actions.move_to_element(checkbox).perform()
        self.driver.execute_script("arguments[0].click();", checkbox)

        actions.move_to_element(submit).perform()
        self.driver.execute_script("arguments[0].click();", submit)

        wait = WebDriverWait(self.driver, 5)

        # Step 5) Check that the link content exist
        try:
            href = self.driver.find_element_by_xpath(
                "//h2[contains(text(),'Thanks for your request.')]/a").get_attribute(
                'href')
            assert href == link['link']

        # NoSuchElementException thrown if not present
        except NoSuchElementException:
            print("Element does not exist")

    def tearDown(self):
        self.driver.close()
        # driver.quit()
        # self.driver.close()
