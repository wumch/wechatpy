# -*- coding: utf-8 -*-
import os
import json
import unittest

from httmock import HTTMock, response, urlmatch

from aiowechatpy import WeChatOAuth
from aiowechatpy.exceptions import WeChatClientException

_TESTS_PATH = os.path.abspath(os.path.dirname(__file__))
_FIXTURE_PATH = os.path.join(_TESTS_PATH, "fixtures")


@urlmatch(netloc=r"(.*\.)?api\.weixin\.qq\.com$")
def wechat_api_mock(url, request):
    path = url.path[1:].replace("/", "_")
    res_file = os.path.join(_FIXTURE_PATH, f"{path}.json")
    content = {"errcode": 99999, "errmsg": f"can not find fixture: {res_file}"}
    headers = {"Content-Type": "application/json"}
    try:
        with open(res_file) as f:
            content = json.loads(f.read())
    except (IOError, ValueError):
        content["errmsg"] = f"Fixture {res_file} json decode error"
    return response(200, content, headers, request=request)


class WeChatOAuthTestCase(unittest.TestCase):
    app_id = "123456"
    secret = "123456"
    redirect_uri = "http://localhost"

    def setUp(self):
        self.oauth = WeChatOAuth(self.app_id, self.secret, self.redirect_uri)

    def test_get_authorize_url(self):
        authorize_url = self.oauth.authorize_url
        self.assertEqual(
            "https://open.weixin.qq.com/connect/oauth2/authorize?appid=123456&redirect_uri=http%3A%2F%2Flocalhost"
            "&response_type=code&scope=snsapi_base#wechat_redirect",
            authorize_url,
        )

    def test_get_qrconnect_url(self):
        url = self.oauth.qrconnect_url
        self.assertEqual(
            "https://open.weixin.qq.com/connect/qrconnect?appid=123456&redirect_uri=http%3A%2F%2Flocalhost"
            "&response_type=code&scope=snsapi_login#wechat_redirect",
            url,
        )

    def test_fetch_access_token(self):
        with HTTMock(wechat_api_mock):
            res = self.oauth.fetch_access_token("123456")
            self.assertEqual("ACCESS_TOKEN", res["access_token"])

    def test_refresh_access_token(self):
        with HTTMock(wechat_api_mock):
            res = self.oauth.refresh_access_token("123456")
            self.assertEqual("ACCESS_TOKEN", res["access_token"])

    def test_get_user_info(self):
        with HTTMock(wechat_api_mock):
            self.oauth.fetch_access_token("123456")
            res = self.oauth.get_user_info()
            self.assertEqual("OPENID", res["openid"])

    def test_check_access_token(self):
        with HTTMock(wechat_api_mock):
            self.oauth.fetch_access_token("123456")
            res = self.oauth.check_access_token()
            self.assertEqual(True, res)

    def test_reraise_requests_exception(self):
        @urlmatch(netloc=r"(.*\.)?api\.weixin\.qq\.com$")
        def _wechat_api_mock(url, request):
            return {"status_code": 404, "content": "404 not found"}

        try:
            with HTTMock(_wechat_api_mock):
                self.oauth.fetch_access_token("123456")
        except WeChatClientException as e:
            self.assertEqual(404, e.response.status_code)
