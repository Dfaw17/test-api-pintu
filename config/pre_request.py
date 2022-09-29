# IMPORT
import config.data as data
import requests


# VARIABLE
def req_otp():
    param = {
        "auth": {
            "type": "email",
            "email": data.email,
            "password": data.pwd
        }
    }
    header = {
        'Accept': 'application/json, text/plain, /',
        'Content-Type': 'application/json',
        'x-pintu-device-id': '6DDD7F0A-8C5F-4556-9319-24D4FEE46839',
        'x-pintu-device-is-jailbreak': 'undefined',
        'x-pintu-app-version': '3.20.0.3147',
        'x-datadog-sampled': 'undefined',
        'User-Agent': 'AUTOMATION API',
        'X-Pintu-Staging': 'undefined',
        'x-datadog-trace-id': '5628501733',
        'x-datadog-parent-id': '3196239874',
        'x-datadog-origin': 'rum',
    }
    req = requests.post("https://api.staging.pintu.co.id/v1/users/login", json=param, headers=header)
    jwt = req.headers.get("authorization")
    resp = {
        'Accept': 'application/json, text/plain, /',
        'Content-Type': 'application/json',
        'x-pintu-device-id': '6DDD7F0A-8C5F-4556-9319-24D4FEE46839',
        'x-pintu-device-is-jailbreak': 'undefined',
        'x-pintu-app-version': '3.20.0.3147',
        'x-datadog-sampled': 'undefined',
        'User-Agent': 'AUTOMATION API',
        'authorization': jwt,
        'X-Pintu-Staging': 'undefined',
        'x-datadog-trace-id': '5628501733',
        'x-datadog-parent-id': '3196239874',
        'x-datadog-origin': 'rum'
    }
    return resp
