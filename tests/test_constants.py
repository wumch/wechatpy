# -*- coding: utf-8 -*-
import unittest

from aiowechatpy.constants import WeChatErrorCode


class WeChatErrorCodeTestCase(unittest.TestCase):
    """ensure python compatibility"""

    def test_error_code(self):
        self.assertEqual(-1000, WeChatErrorCode.SYSTEM_ERROR.value)
        self.assertEqual(42001, WeChatErrorCode.EXPIRED_ACCESS_TOKEN.value)
        self.assertEqual(48001, WeChatErrorCode.UNAUTHORIZED_API.value)

    def test_enum(self):
        self.assertEqual(WeChatErrorCode.SYSTEM_BUSY, WeChatErrorCode(-1))
