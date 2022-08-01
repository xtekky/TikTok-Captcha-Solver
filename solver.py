import requests
import base64
import time
import random

from urllib.parse import urlencode
from utils.xgorgon import Gorgon
from utils.solver import PuzzleSolver

class Solver:
    def __init__(self, did, iid):
        self.__xgorgon    = Gorgon()
        self.__host       = "verification-va.tiktokv.com"
        self.__device_id  = did 
        self.__install_id = iid 
        self.__cookies    = ""
        self.__client     = requests.Session()

    def __params(self):
        params = {
            "lang": "en",
            "app_name": "musical_ly",
            "h5_sdk_version": "2.26.17",
            "sdk_version": "1.3.3-rc.7.3-bugfix",
            "iid": self.__install_id,
            "did": self.__device_id,
            "device_id": self.__device_id,
            "ch": "beta",
            "aid": "1233",
            "os_type": "0",
            "mode": "",
            "tmp": f"{int(time.time())}{random.randint(111, 999)}",
            "platform": "app",
            "webdriver": "false",
            "verify_host": "https://verification-va.tiktokv.com/",
            "locale": "en",
            "channel": "beta",
            "app_key": "",
            "vc": "18.2.15",
            "app_verison": "18.2.15",
            "session_id": "",
            "region": ["va", "US"],
            "use_native_report": "0",
            "use_jsb_request": "1",
            "orientation": "1",
            "resolution": ["900*1552", "900*1600"],
            "os_version": ["25", "7.1.2"],
            "device_brand": "samsung",
            "device_model": "SM-G973N",
            "os_name": "Android",
            "challenge_code": "1105",
            "app_version": "18.2.15",
            "subtype": "",
        }

        return urlencode(params)

    def __headers(
        self,
        params : str,
        payload: (bool or str) = None,
        cookies: (bool or str) = None
    ):
        
        sign = self.__xgorgon.calculate(
            url    = params,
            body   = payload,
            cookie = cookies,
        )

        headers = {
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "x-ss-req-ticket": f"{int(time.time())}{random.randint(111, 999)}",
            "cookie": self.__cookies,
            "content-type": "application/json; charset=utf-8",
            "host": self.__host,
            "connection": "Keep-Alive",
            "user-agent": "okhttp/3.10.0.1",
            "x-gorgon": sign["X-Gorgon"],
            "x-khronos": sign["X-Khronos"],
        }

        return headers

    def __get_challenge(self) -> dict:
      # removed from preview

    def __post_captcha(self, solve: dict) -> dict:
        # removed from preview

    def solve_captcha(self):
        __captcha_challenge = self.__get_challenge()

        __captcha_id = __captcha_challenge["data"]["id"]
        __tip_y = __captcha_challenge["data"]["question"]["tip_y"]

        solve = self.__solve_captcha(
            __captcha_challenge["data"]["question"]["url1"],
            __captcha_challenge["data"]["question"]["url2"],
        )
        
        solve.update(
                {
                    "id": __captcha_id,
                    "tip": __tip_y
            }
        )
        
        return self.__post_captcha(solve)


if __name__ == "__main__":
    __device_id = ""
    __install_id = ""
    
    print(
        Solver(
            did = __device_id,
            iid = __install_id
        ).solve_captcha()
    )
    
    # >>> {'code': 200, 'data': None, 'message': 'Verification complete'}