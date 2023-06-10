import json
import urllib.request, urllib.error, urllib.parse
from unittest import TestCase
from flyers3.flyers3 import F3

""" 
Slackとの連携をテストするための関数
"""
def exec_api(req):
    """
    explanation:
        exec Slack API
    Args:
        req: urllib request object
    Return:
        body: Json object (dict)
    正常に完了した場合は Responsbody(json) を返す
    失敗した場合は、エラーjson(dict) を返す
    {"ok": false, "err":{"code": $err.code, "reason": $err.reason}}
    """
    body = {"ok": False}
    try:
        with urllib.request.urlopen(req) as res:
            body = json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError:
        time.sleep(61)
        try:
            with urllib.request.urlopen(req) as res:
                body = json.loads(res.read().decode("utf-8"))
        except urllib.error.HTTPError as err:
            err_d = {"reason": str(err.reason), "code": str(err.code)}
            body = {"ok": False, "err": err_d}
    except urllib.error.URLError:
        time.sleep(11)
        try:
            with urllib.request.urlopen(req) as res:
                body = json.loads(res.read().decode("utf-8"))
        except urllib.error.URLError as err:
            err_d = {"reason": str(err.reason)}
            body = {"ok": False, "err": err_d}
    return body

def auth_test(token: str) -> dict:
    """
    https://api.slack.com/methods/auth.test
    """
    url = "https://slack.com/api/auth.test"
    params = {"token": token}
    req = urllib.request.Request(
        "{}?{}".format(url, urllib.parse.urlencode(params))
    )
    body = exec_api (req)
    return body

def chat_postMessage(token: str, channel: str) -> dict:
    """
    https://api.slack.com/methods/chat.postMessage
    """
    url = "https://slack.com/api/chat.postMessage"
    params = {"token": token, "channel": channel, "text": "this is test bt test_f3.py"}
    req = urllib.request.Request(
        "{}?{}".format(url, urllib.parse.urlencode(params))
    )
    body = exec_api (req)
    return body


"""
テスト本体
"""

class TestF3(TestCase):

    def test_get_slack_conf(self):
        res = F3.get_slack_conf()
        self.assertEqual(type(res), list)

    def test_slack_token_enable(self):
        SLACK_BOT_TOKEN, SLACK_CHANNEL = F3.get_slack_conf()
        res = auth_test(SLACK_BOT_TOKEN)
        self.assertEqual(res["ok"], True)

    def test_slack_token_enable2(self):
        SLACK_BOT_TOKEN, SLACK_CHANNEL = F3.get_slack_conf()
        res = chat_postMessage(SLACK_BOT_TOKEN, SLACK_CHANNEL)
        self.assertEqual(res["ok"], True)


if __name__ == '__main__':
    unittest.main()
