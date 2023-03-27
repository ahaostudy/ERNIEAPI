import re

from .wenxin import WenXinBot

wenxin_cookies_dict_list = [
    {
        "name": "BAIDUID_BFESS",
        "value": "FF758D61491ADB1FCF458A4B902D65E7:FG=1",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-03-23T03:02:40.431Z",
        "httpOnly": False,
        "secure": True,
        "sameSite": "None"
    },
    {
        "name": "BAIDU_WISE_UID",
        "value": "wapp_1675862307387_597",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-03-14T13:18:25.349Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "__bid_n",
        "value": "1869253f4012c776244207",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-29T10:53:48.412Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "__xsptplus861",
        "value": "861.1.1678170687.1678170687.1%234%7C%7C%7C%7C%7C%23%23KUeQoIrp-hpme0RBg1FPTBBCDqJsxmoQ%23",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-10T06:31:27.031Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "BDUSS",
        "value": "djRGtvdmZSNVpjbmlhYS1oUG85UkJmazZCMlh2bTkzc016Ulp-cVJxcW83VHRrSVFBQUFBJCQAAAAAAQAAAAEAAADoztUoYWhhb3N0dWR5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKhgFGSoYBRkQ2",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-20T12:44:23.102Z",
        "httpOnly": True,
        "secure": False
    },
    {
        "name": "BDUSS_BFESS",
        "value": "djRGtvdmZSNVpjbmlhYS1oUG85UkJmazZCMlh2bTkzc016Ulp-cVJxcW83VHRrSVFBQUFBJCQAAAAAAQAAAAEAAADoztUoYWhhb3N0dWR5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKhgFGSoYBRkQ2",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-27T03:02:40.431Z",
        "httpOnly": True,
        "secure": True,
        "sameSite": "None"
    },
    {
        "name": "BIDUPSID",
        "value": "FF758D61491ADB1FCF458A4B902D65E7",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-27T03:02:22.135Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "PSTM",
        "value": "1679626941",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-27T03:02:22.135Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "ZFY",
        "value": ":AtbdCFKwVxUn:BOlzk92:AuXuqAFutIiCrs8Oe:BeufF:BE:C",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-03-23T03:02:36.535Z",
        "httpOnly": False,
        "secure": True,
        "sameSite": "None"
    },
    {
        "name": "arialoadData",
        "value": "False",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2023-03-27T06:06:17.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "FPTOKEN",
        "value": "N7lIG7n7xitR0gy3VY2QnQcFu+A6W/Id5emrzXAwlEaTHMnLEXMQ1PSk1BRJmOclQjeAAJquUYpgkG9h+TCByqLMySh6SYSU5bYtFo15aJbzGKYPHovRl26Fkj81Q9VDfC4pl8om7DI/JLVof/Ah9RegOkX33BGxfuxYIXKM4Ixc7Rlph4/LPGCpsukjjXWGRLi/IpR3olz9TYPUb4MyYjiOY7iJRpK8Ueu8L4+Dpub2u/eHBXCu4mnTO6C9sigCvR6Edrn9cpQnRoL792Xu8ChrWBTmYdkeXkRiC4c8P1zPvOXCebu9hS4N49OiFp7y1OQS2T6DK/hwljymi5HXEvxIKAsgT38j2/RoUiGS51meMETvl+CxHjVyghENcHldd+ptYqyuouOUGbwwg3x2Cj1sCSH+tjUof4JYQVkVaIH5CCVRyn9ZZw4h1aM7/ROd|ikNEenbpjRERmxKXocNGsVTDzybDVFQSQgAJZpSXeCE=|10|9770b7f452ce7521d1c7b42d41e8b136",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2024-04-29T06:06:19.792Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "XFI",
        "value": "797d8090-cbc4-11ed-9396-31e78923eb34",
        "path": "/",
        "domain": "yiyan.baidu.com",
        "expires": "1969-12-31T23:59:59.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "Hm_lvt_01e907653ac089993ee83ed00ef9c2f3",
        "value": "1679199636,1679280425,1679814896,1679828025",
        "path": "/",
        "domain": ".yiyan.baidu.com",
        "expires": "2024-03-25T10:53:45.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "Hm_lpvt_01e907653ac089993ee83ed00ef9c2f3",
        "value": "1679828025",
        "path": "/",
        "domain": ".yiyan.baidu.com",
        "expires": "1969-12-31T23:59:59.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "XFCS",
        "value": "CE4547532A70CAD25C7D5C548897F9C6A018C4D7CE0FCF2D24236A7655EB791D",
        "path": "/",
        "domain": "yiyan.baidu.com",
        "expires": "1969-12-31T23:59:59.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "XFT",
        "value": "Ym0tfXLq8R2Um04B4fdl5cfqFlmMnQwPlJfApHJr12Y=",
        "path": "/",
        "domain": "yiyan.baidu.com",
        "expires": "1969-12-31T23:59:59.000Z",
        "httpOnly": False,
        "secure": False
    },
    {
        "name": "ab_sr",
        "value": "1.0.1_YzM0M2I1NmU2ODQ3NjhhZGZjZWE2MTI1OTNmZWUxMjNmNTYyMTA2YjA2MjBhZWRmN2JiNzA0YzUyZTg2NGQ0OTdiMTMyYjA4NTdmYzhkMWY0MGM1YmI1NmFiZWYwNjg4OGNlNmE5ZjcyMWJlYWQ4Nzk5MzllZTQ0ZWM3MmFlY2RiYjNkYmNmMDQ2NWFlMjI0Y2I0OTEzOWNjOThmZTRjMThlZGQyNzdhMjM2MmQwZTEwMTkwODIyY2M3YWNhZWZh",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2023-03-26T12:53:48.607Z",
        "httpOnly": True,
        "secure": True,
        "sameSite": "None"
    },
    {
        "name": "RT",
        "value": "\"z=1&dm=baidu.com&si=380ec76a-6824-4500-a0ee-604aca34cb0c&ss=lfp9yhob&sl=1q&tt=1q6v&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=axu5\"",
        "path": "/",
        "domain": ".baidu.com",
        "expires": "2023-04-02T10:54:31.000Z",
        "httpOnly": False,
        "secure": False,
        "sameSite": "Lax"
    }
]

wx = WenXinBot(wenxin_cookies_dict_list)

wx.init_selenium(headless=False)


def chat(text: str) -> (str, bool):
    answer = wx.chat_via_selenium(text)
    urls = re.findall(r"<img src=\"(.+?)\" />", answer)
    print(urls)
    if len(urls) > 0:
        return urls[0], True
    else:
        return answer, False
