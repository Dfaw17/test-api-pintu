# IMPORT
import pytest
import config.data
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

    # VERIFY
    verify_email = req.json().get("payload")["user"]["email"]
    verify_status_code = req.status_code

    # ASSERT
    assert_that(verify_email).is_equal_to(config.data.email)
    assert_that(verify_status_code).is_equal_to(200)


@pytest.mark.PintuTestRail(11396)
def test_login_wrong_otp():
    """Test Login Wrong OTP"""
    param = {
        "otp": data.otp_wrong,
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd
        }
    }
    req = requests.post(url.login, json=param, headers=pre.req_otp())

    # VERIFY
    verify_status_code = req.status_code
    verify_msg = req.json().get("message")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(400)
    assert_that(verify_msg).is_equal_to(config.data.err_OTP)


@pytest.mark.PintuTestRail(11397)
def test_login_wrong_password():
    """Test Login Wrong Password"""
    param = {
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd_wrong
        }
    }
    req = requests.post(url.login, json=param)
    # VERIFY
    verify_status_code = req.status_code
    verify_msg = req.json().get("message")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(401)
    assert_that(verify_msg).is_equal_to(config.data.wrong_password)
