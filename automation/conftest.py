import pytest
import config.config as config


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    get_error = request.session.testsfailed
    yield
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
    test_success = len(request.session.items) - request.session.testsfailed
    test_failed = request.session.testsfailed
    test_all = len(request.session.items)
    success_rate = test_success / test_all * 100

    if test_failed > 0:
        color = "FF1E00"
    else:
        color = "2B7A0B"

    config.webhook_slack(color, test_success, test_failed, test_all, success_rate)
