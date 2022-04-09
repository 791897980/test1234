# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_get_token.py

import requests

class TestToken:

    def test_get_token(self):
        """
        获取 access_token
        """
        # 定义凭证
        corpid = "ww876064acebf0fa3c"
        corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

        # 发 get 请求
        r = requests.get(url)

        # 打印响应
        print(r.json())

        # 获取 access_token
        access_token = r.json()['access_token']
        print(access_token)

    def test_get_token2(self):
        """
        获取 access_token 的第二种方法
        """
        # 定义凭证
        corpid = "ww876064acebf0fa3c"
        corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发 get 请求
        r = requests.get(url, params=params)
        # 打印响应
        print(r.json())

        access_token = r.json()['access_token']
        return access_token
