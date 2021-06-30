from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from config.settings import DRIVER_HOME, LINKS
from os.path import join
import unittest


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        # Step 1) Open Chrome
        self.drivers = dict()
        self.driver = webdriver.Chrome(join(DRIVER_HOME, 'chromedriver'))

        # Wait implicitly for elements to be ready before attempting interactions
        self.driver.implicitly_wait(10)

        # self.browser = webdriver.Chrome(
        #    executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        # self.drivers['Firefox'] = webdriver.Firefox(join(DRIVER_HOME, 'firefox'))
        # self.drivers['Edge'] = webdriver.Edge(join(DRIVER_HOME, 'msedgedriver'))
        # self.drivers['Opera'] = webdriver.Opera(join(DRIVER_HOME, 'operadriver'))

    def test_links(self):
        # Step 2) Navigate to fiware.org
        links = LINKS['links']
        for link in links:
            self.driver.get(link['url'])

            # Step 3) Search elements to put data
            name = self.driver.find_element_by_id("happyforms-92014_single_line_text_1")
            assert name is not None

            surname = self.driver.find_element_by_id("happyforms-92014_single_line_text_18")
            assert surname is not None

            email = self.driver.find_element_by_id("happyforms-92014_email_2")
            assert email is not None

            checkbox = self.driver.find_element_by_id("happyforms-92014_legal_29")
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
                # identify element
                # <a href="https://www.fiware.org/wp-content/uploads/FF_PositionPaper_FIWARE4DataSpaces.pdf" target="_blank"
                href = self.driver.find_element_by_xpath("//h2[contains(text(),'Thanks for your request.')]/a").get_attribute(
                    'href')
                # 'https://www.fiware.org/wp-content/uploads/FF_PositionPaper_FIWARE4DataSpaces.pdf'
                # rel="noopener noreferrer">Download your copy here!</a>
                assert href == link['link']

            # NoSuchElementException thrown if not present
            except NoSuchElementException:
                print("Element does not exist")

    def tearDown(self):
        self.driver.close()
        # driver.quit()
        # self.driver.close()
