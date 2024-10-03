from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="specify the browser: chrome or firefox or edge")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True, scope="class", params=['chrome'])
def _drivers(browser):

    global driver
    # browser = request.param
    if browser == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
    elif browser == "edge":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opts)

    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.close()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        now = datetime.now()
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        now = datetime.now()
        report_dir = Path('Reports', now.strftime("%S%H%d%m%Y"))
        report_dir.mkdir(parents=True, exist_ok=True)
        pytest_html = report_dir / f"report_{now.strftime('%H%M%S')}.html"
        config.option.htmlpath = pytest_html
        config.option.self_contained_html = True

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

    def pytest_html_report_title(report):
        report.title = "Automation Report"
