import requests
import os
import json


class DingtalkMessage(object):
    def __init__(self):
        self.dingtalk_urls = {
            'default': 'https://oapi.dingtalk.com/robot/send?access_token=0be38a1f55054f496b40a60dec6a21d7e156c7bbe87e01fa178e9f27b510a762'
        }
    
    @staticmethod
    def _post(url, data, headers={'Content-Type': 'application/json'}, *args, **kwargs):
        res = requests.post(url, data, headers=headers, *args, **kwargs)
        if res.status_code != 200:
            print('Requests Bad. status_code:' + str(res.status_code))
        else:
            # print(res.content)
            return res.text

        return None

    def send_markdown_message(self, title='', text='', at_mobiles=[], at_user_ids=[], is_at_all=False,
                              hook_name='default'):
        msg_body = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {
                "atMobiles": at_mobiles,
                "atUserIds": at_user_ids,
                "isAtAll": is_at_all
            }
        }
        res = self._post(self.dingtalk_urls[hook_name], data=json.dumps(msg_body))
        return res


if __name__ == '__main__':
    import time
    print(time.time())
    ding_msg = DingtalkMessage()

    ding_msg.send_markdown_message('Hello free server.', 'Github 免费服务测试.')