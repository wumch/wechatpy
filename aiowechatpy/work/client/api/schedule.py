# -*- coding: utf-8 -*-


import operator as op

from aiowechatpy.client.api.base import BaseWeChatAPI


class WeChatSchedule(BaseWeChatAPI):
    def add(
        self,
        organizer,
        start_time,
        end_time,
        attendees=(),
        summary="",
        description="",
        is_remind=True,
        remind_before_event_secs=3600,
        is_repeat=False,
        repeat_type=0,
        location="",
        calendar_id="",
    ):
        """
        创建日程

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E5%88%9B%E5%BB%BA%E6%97%A5%E7%A8%8B

        :param organizer: 组织者
        :param start_time: 日程开始时间，Unix时间戳
        :param end_time: 日程结束时间，Unix时间戳
        :param attendees: 日程参与者列表。最多支持2000人
        :param summary: 日程标题。0 ~ 128 字符。不填会默认显示为“新建事件”
        :param description: 日程描述。0 ~ 512 字符
        :param is_remind: 是否需要提醒
        :param remind_before_event_secs: 日程开始（start_time）前多少秒提醒，当is_remind为1时有效
        :param is_repeat: 是否重复日程
        :param repeat_type: 重复类型，当is_repeat为1时有效。目前支持如下类型：
            0 - 每日
            1 - 每周
            2 - 每月
            5 - 每年
            7 - 工作日
        :param location: 日程地址。0 ~ 128 字符
        :param calendar_id: 日程所属日历ID。注意，这个日历必须是属于组织者(organizer)的日历；如果不填，那么插入到组织者的默认日历上

        :type organizer: str
        :type start_time: int
        :type end_time: int
        :type attendees: list[str]
        :type summary: str
        :type description: str
        :type is_remind: bool
        :type remind_before_event_secs: int
        :type is_repeat: bool
        :type repeat_type: int
        :type location: str
        :type calendar_id: str

        :return: 日程ID
        :rtype: str
        """

        data = {
            "schedule": {
                "organizer": organizer,
                "start_time": start_time,
                "end_time": end_time,
                "attendees": [{"userid": userid} for userid in attendees],
                "summary": summary,
                "description": description,
                "reminders": {
                    "is_remind": int(is_remind),
                    "remind_before_event_secs": remind_before_event_secs,
                    "is_repeat": int(is_repeat),
                    "repeat_type": repeat_type,
                },
                "location": location,
                "cal_id": calendar_id,
            }
        }
        return self._post("oa/schedule/add", data=data, result_processor=op.itemgetter("schedule_id"))

    def update(
        self,
        organizer,
        schedule_id,
        start_time,
        end_time,
        attendees=(),
        summary="",
        description="",
        is_remind=True,
        remind_before_event_secs=3600,
        is_repeat=False,
        repeat_type=0,
        location="",
        calendar_id="",
    ):
        """
        更新日程

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E6%9B%B4%E6%96%B0%E6%97%A5%E7%A8%8B

        :param organizer: 组织者
        :param schedule_id: 日程ID
        :param start_time: 日程开始时间，Unix时间戳
        :param end_time: 日程结束时间，Unix时间戳
        :param attendees: 日程参与者列表。最多支持2000人
        :param summary: 日程标题。0 ~ 128 字符。不填会默认显示为“新建事件”
        :param description: 日程描述。0 ~ 512 字符
        :param is_remind: 是否需要提醒
        :param remind_before_event_secs: 日程开始（start_time）前多少秒提醒，当is_remind为1时有效
        :param is_repeat: 是否重复日程
        :param repeat_type: 重复类型，当is_repeat为1时有效。目前支持如下类型：
            0 - 每日
            1 - 每周
            2 - 每月
            5 - 每年
            7 - 工作日
        :param location: 日程地址。0 ~ 128 字符
        :param calendar_id: 日程所属日历ID。注意，这个日历必须是属于组织者(organizer)的日历；如果不填，那么插入到组织者的默认日历上

        :type organizer: str
        :type schedule_id: str
        :type start_time: int
        :type end_time: int
        :type attendees: list[str]
        :type summary: str
        :type description: str
        :type is_remind: bool
        :type remind_before_event_secs: int
        :type is_repeat: bool
        :type repeat_type: int
        :type location: str
        :type calendar_id: str
        """

        data = {
            "schedule": {
                "organizer": organizer,
                "schedule_id": schedule_id,
                "start_time": start_time,
                "end_time": end_time,
                "attendees": [{"userid": userid} for userid in attendees],
                "summary": summary,
                "description": description,
                "reminders": {
                    "is_remind": int(is_remind),
                    "remind_before_event_secs": remind_before_event_secs,
                    "is_repeat": int(is_repeat),
                    "repeat_type": repeat_type,
                },
                "location": location,
                "cal_id": calendar_id,
            }
        }
        return self._post("oa/schedule/update", data=data)

    def get(self, schedule_ids):
        """
        获取日程

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E8%8E%B7%E5%8F%96%E6%97%A5%E7%A8%8B%E8%AF%A6%E6%83%85

        :param schedule_ids: 日程ID列表。一次最多可获取1000条
        :type schedule_ids: list[str]

        :return: 日程列表
        :rtype: list[dict]
        """
        return self._post(
            "oa/schedule/get",
            data={"schedule_id_list": schedule_ids},
            result_processor=op.itemgetter("schedule_list"),
        )

    def delete(self, schedule_id):
        """
        取消日程（删除日程）

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E5%8F%96%E6%B6%88%E6%97%A5%E7%A8%8B

        :param schedule_id: 日程ID
        """
        return self._post("oa/schedule/del", data={"schedule_id": schedule_id})

    def get_by_calendar(self, calendar_id, offset=0, limit=500):
        """
        获取日历下的日程列表

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E8%8E%B7%E5%8F%96%E6%97%A5%E5%8E%86%E4%B8%8B%E7%9A%84%E6%97%A5%E7%A8%8B%E5%88%97%E8%A1%A8
        （注意，被取消的日程也可以拉取详情，调用者需要检查status）

        :param calendar_id: 日历ID
        :param offset: 分页，偏移量, 默认为0
        :param limit: 分页，预期请求的数据量，默认为500，取值范围 1 ~ 1000

        :return: 日程列表
        :rtype: list[dict]
        """
        return self._post(
            "oa/schedule/get_by_calendar",
            data={"cal_id": calendar_id, "offset": offset, "limit": limit},
            result_processor=op.itemgetter("schedule_list"),
        )

    def del_users(self, schedule_id, users):
        """
        删除日程参与者

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93648#%E5%88%A0%E9%99%A4%E6%97%A5%E7%A8%8B%E5%8F%82%E4%B8%8E%E8%80%85

        :param schedule_id: 日程 ID
        :param users: 日程参与者 ID 列表

        :type users: list[str]
        """
        attendees = [{"userid": i for i in users}]
        return self._post("oa/schedule/del_attendees", data={"schedule_id": schedule_id, "attendees": attendees})
