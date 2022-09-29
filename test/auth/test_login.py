# IMPORT
import pytest
import config.data as data
import config.endpoint as url
import config.pre_request as pre
from assertpy import assert_that
from config.testrail import *


@pytest.mark.PintuTestRail(7551)
def test_login_normal():
    """Test Login Normal"""
    param = {
        "otp": data.otp,
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd
        }
    }
    req = requests.post(url.login, json=param, headers=pre.req_otp())
    assert_that(req.status_code).is_equal_to(200)


@pytest.mark.PintuTestRail(7551)
def test_login_normal_2():
    """Test Login Wrong"""
    param = {
        "otp": data.otp,
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd
        }
    }
    req = requests.post(url.login, json=param, headers=pre.req_otp())
    assert_that(req.status_code).is_equal_to(200)


@pytest.mark.PintuTestRail(7551)
def test_login_normal_3():
    """Test Login Failed"""
    param = {
        "otp": data.otp,
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd
        }
    }
    req = requests.post(url.login, json=param, headers=pre.req_otp())
    assert_that(req.status_code).is_equal_to(200)
