import requests
import json
from selenium import webdriver
import time
from browsermobproxy import Server
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, sys

url = 'https://yiyan.baidu.com/'
url_new = "https://yiyan.baidu.com/eb/session/new"
url_new_text = "https://yiyan.baidu.com/eb/chat/new"
url_check = "https://yiyan.baidu.com/eb/chat/check"

abs_path = os.path.dirname(os.path.realpath(sys.argv[0])) + '/'

"""
    错误类
    code:
    0: 其他错误
    1: 未传入cookies
    2: 初始化selenium失败
    3: chat空消息
"""


class WenxinRevError(Exception):
    def __init__(self, value, code=0):
        self.value = value
        self.code = code

    def __str__(self):
        return repr(self.value)


class WenXinBot:
    # 初始化cookies_list
    def __init__(self, wenxin_cookies_dict_list) -> None:
        if not wenxin_cookies_dict_list:
            raise WenxinRevError("cookies list parameter is empty", 1)
        self.proxy = None
        self.driver = None
        self.seleniumDebug = None
        self.session_id = None
        self.wenxin_cookies_dict_list = wenxin_cookies_dict_list

    def new_session(self, name):
        # 已实现
        ts = int(time.time() * 1000)
        data = {
            'deviceType': "pc",
            'sessionName': name,
            'timestamp': ts,
        }
        res = requests.post(url_new, json=data)
        session_id = res.json()['data']['sessionId']
        print(res.text)
        self.session_id = session_id
        return session_id

    """
      初始化selenium
    """

    def init_selenium(self, headless=True, debug=False) -> bool:
        # 启动代理
        server_proxy = Server(abs_path + 'wenxin/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
        server_proxy.start()
        self.seleniumDebug = debug
        print("[Wenxin] start login...\n")
        try:
            self.proxy = server_proxy.create_proxy()
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
            options.add_argument('--incognito')
            options.add_argument('--ignore-certificate-errors')
            if headless:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            options.add_argument('window-size=1920x1080')
            options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片,提升速度
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument('log-level=3')
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
            })
            self.driver.get(url)
            time.sleep(5)
            self.driver.delete_all_cookies()
            for t in self.wenxin_cookies_dict_list:
                self.driver.add_cookie(t)
            self.driver.get(url)
            time.sleep(3)
            print("[Wenxin] loading finished")
        except Exception as e:
            print("[Wenxin] init selenium failed")
            raise WenxinRevError("init selenium failed " + str(e), 2)
        return True

    """
      通过Selenium来进行交互
    """

    def chat_via_selenium(self, text, timeout=15) -> str:
        if text == "":
            raise WenxinRevError("chat input is empty", 3)
        ts = str(time.time())
        self.proxy.new_har(ts, options={'captureContent': True})
        input_area = self.driver.find_element(By.CLASS_NAME, 'wBs12eIN')
        input_area.send_keys(text)
        input_area.send_keys(Keys.ENTER)
        print("[Wenxin] message sent successfully, collecting information...")
        capture_count = 0

        while True:
            time.sleep(2)
            result = self.proxy.har
            res_text = ''
            is_end = False
            for entry in result['log']['entries']:
                if 'request' in entry and \
                        'url' in entry['request'] and \
                        entry['request']['url'] == 'https://yiyan.baidu.com/eb/chat/query':
                    if self.seleniumDebug: print("[Wenxin] [SUCCESS] Get query.")
                    if self.seleniumDebug: print(entry)
                    if 'response' in entry and 'content' in entry['response'] and \
                            'text' in entry['response']['content']:
                        reply_data = json.loads(entry['response']['content']['text'])
                        if self.seleniumDebug: print("[Wenxin] [SUCCESS] Get Reply Data.")
                        if reply_data['data']['content'] != "":
                            res_text += reply_data['data']['content']
                            if self.seleniumDebug: print("isend:" + str(reply_data['data']['is_end']))
                            if reply_data['data']['is_end'] == 1 or reply_data['data']['is_end'] == "1":
                                is_end = True
                                if self.seleniumDebug: print("[Wenxin] [SUCCESS] Get is_end == 1.")
                                break

            if is_end:
                if self.seleniumDebug: print("[Wenxin] [Reply] " + res_text)
                return res_text
            else:
                capture_count += 1
                if self.seleniumDebug: print("[Wenxin] [Replying] " + res_text)

            if capture_count * 2 > timeout:
                if self.seleniumDebug: print("[Wenxin] Timeout.")
                return res_text

    def check(self, text):
        ts = int(time.time() * 1000)
        data = {
            'deviceType': "pc",
            'timestamp': ts,
            'text': text,
        }
        res = requests.post(url_check, json=data)
        print(res.text)

