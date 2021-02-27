import time
import pytest
from Utilities.Baseclass import Baseclass
from Testdata.getdata import senddata


class Testflipkart(Baseclass):
    def test_flipkarFlow(self, getdata):
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
        self.driver.find_element_by_css_selector("._3704LK").send_keys("Mens watch")
        self.driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()

        list = []
        time.sleep(3)

# Select the filter and select price low to high
        sortdata = self.driver.find_elements_by_xpath("//div[@class='_5THWM1']/div")
        print(len(sortdata))
        for sort in sortdata:
            if sort.text == getdata["sortby"]:
                sort.click()
                break

        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='QvtND5 _2w_U27']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Search Brand']").send_keys(getdata["searchbrand"])

# Pick all the brands and select a particular brand
        Brands = self.driver.find_elements_by_xpath("//div[@class='_38vbm7']/div")
        print(len(Brands))
        for brand in Brands:
            if brand.text == getdata["Selectbrand"]:
                brand.click()
                break
        self.driver.find_element_by_xpath("//span[contains(text(),'Apply Filters')]").click()
        time.sleep(3)

# Add the prices in the list and pick the lowest price
        prices = self.driver.find_elements_by_xpath("//div/div[@class='_30jeq3']")
        print(len(prices))
        time.sleep(3)
        for price in prices:
            list.append(price.text)
            j = list[0]
            for p in range(len(list)):
                if list[p] < j:
                    j = list[p]

        print(list)
        print(j)
        time.sleep(5)
# Compare the prices with the lowest price we got in the upper loop and click on lowest price
        for low in prices:
            if low.text == j:
                low.click()

        time.sleep(3)
# Move to new tab and click add to cart button
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()
        self.driver.find_element_by_xpath("//span[text()='Place Order']").click()





# Use data with fixture and reture the value and get the values with data[index]
# @pytest.fixture()
# def data():
#     return ["Price -- Low to High", "Fast", "Fastrack"]

# Use data with fixture and reture the value and get the values with data[keyvalue] with parameter
# @pytest.fixture(params=[{"sortby":"Price -- Low to High", "searchbrand":"Fast", "Selectbrand":"Fastrack"}])
# def data(request):
#     return request.param

# Get the data from test data file and use it in this file
@pytest.fixture(params = senddata.test_data)
def getdata(request):
    return request.param