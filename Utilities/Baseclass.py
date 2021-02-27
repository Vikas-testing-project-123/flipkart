import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Baseclass:
    #pass #Pass is a keyword in the python to say that we are not doing andy operation here
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("C:/Users/DELL/PycharmProjects/pythonProject/utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") #asctime is used for the current time and date of the execution
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def waitbylinktest(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def waitbyxpath(self, text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, text)))

    def selectvisibletext(self, text):
        gender = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        gender.select_by_visible_text(text)

