import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/DELL/PycharmProjects/drivers/chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:/Users/DELL/PycharmProjects/drivers/geckodriver.exe")

    elif browser_name == "Ie":
        print("This is internet explorer")

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.quit()


# Fixture to take the screen shot when the test i failed

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # """"""
    # Generate automatic test fail screenshot and attach to the html report
    # """"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src= "%s" alt="screenshot" style="width:500px;height:336px" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)