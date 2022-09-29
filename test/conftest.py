import pytest
import config.config as config
from py.xml import html


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div("No log output captured.", class_="empty log"))


def pytest_html_report_title(report):
    report.title = "API PINTU AUTOMATION"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    print("before test")
    get_error = request.session.testsfailed

    yield

    print("after test")
    test_result = request.session.testsfailed - get_error
    marker = request.node.get_closest_marker("PintuTestRail")

    if marker is None:
        print("there is test case id")
    else:
        if test_result == 0:
            config.testrail_success(marker.args[0])
        else:
            config.testrail_failed(marker.args[0])


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("before suite")

    yield

    print("after suite")
    test_success = len(request.session.items) - request.session.testsfailed
    test_failed = request.session.testsfailed
    test_all = len(request.session.items)
    success_rate = test_success / test_all * 100

    if test_failed > 0:
        color = "FF1E00"
    else:
        color = "2B7A0B"

    config.webhook_slack(color, test_success, test_failed, test_all, success_rate)
