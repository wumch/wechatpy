# -*- coding: utf-8 -*-
import unittest
import time
from datetime import datetime


class MessagesTestCase(unittest.TestCase):
    def test_base_message(self):
        from aiowechatpy.messages import TextMessage

        timestamp = int(time.time())
        msg = TextMessage(
            {
                "MsgId": 123456,
                "MsgType": "text",
                "FromUserName": "user1",
                "ToUserName": "user2",
                "CreateTime": timestamp,
            }
        )

        self.assertEqual(123456, msg.id)
        self.assertEqual("user1", msg.source)
        self.assertEqual("user2", msg.target)
        self.assertTrue(isinstance(msg.create_time, datetime))

    def test_text_message(self):
        from aiowechatpy.messages import TextMessage

        msg = TextMessage(
            {
                "Content": "test",
            }
        )

        self.assertEqual("test", msg.content)

    def test_image_message(self):
        from aiowechatpy.messages import ImageMessage

        msg = ImageMessage(
            {
                "PicUrl": "http://www.qq.com/1.png",
            }
        )

        self.assertEqual("http://www.qq.com/1.png", msg.image)

    def test_voice_message(self):
        from aiowechatpy.messages import VoiceMessage

        msg = VoiceMessage(
            {
                "MediaId": "123456",
                "Format": "aac",
                "Recognition": "test",
            }
        )

        self.assertEqual("123456", msg.media_id)
        self.assertEqual("aac", msg.format)
        self.assertEqual("test", msg.recognition)

    def test_video_message(self):
        from aiowechatpy.messages import VideoMessage

        msg = VideoMessage(
            {
                "MediaId": "123456",
                "ThumbMediaId": "123456",
            }
        )

        self.assertEqual("123456", msg.media_id)
        self.assertEqual("123456", msg.thumb_media_id)

    def test_location_message(self):
        from aiowechatpy.messages import LocationMessage

        msg = LocationMessage(
            {
                "Location_X": "123",
                "Location_Y": "456",
                "Scale": "1",
                "Label": "test",
            }
        )

        self.assertEqual("123", msg.location_x)
        self.assertEqual("456", msg.location_y)
        self.assertEqual("1", msg.scale)
        self.assertEqual("test", msg.label)

    def test_link_message(self):
        from aiowechatpy.messages import LinkMessage

        msg = LinkMessage(
            {
                "Title": "test",
                "Description": "test",
                "Url": "http://www.qq.com",
            }
        )

        self.assertEqual("test", msg.title)
        self.assertEqual("test", msg.description)
        self.assertEqual("http://www.qq.com", msg.url)

    def test_miniprogrampage_message(self):
        from aiowechatpy.messages import MiniProgramPageMessage

        msg = MiniProgramPageMessage(
            {
                "ToUserName": "toUser",
                "FromUserName": "fromUser",
                "CreateTime": 1482048670,
                "MsgType": "miniprogrampage",
                "MsgId": 1234567890123456,
                "Title": "title",
                "AppId": "appid",
                "PagePath": "path",
                "ThumbUrl": "thumburl",
                "ThumbMediaId": "thumbmediaid",
            }
        )
        self.assertEqual("appid", msg.app_id)
        self.assertEqual("title", msg.title)
        self.assertEqual("path", msg.page_path)
        self.assertEqual("thumburl", msg.thumb_url)
        self.assertEqual("thumbmediaid", msg.thumb_media_id)
