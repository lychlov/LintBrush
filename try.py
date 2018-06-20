import requests

for i in range(2):
    res = requests.get('http://www.gsdata.cn/member/checkmcaptcha?captcha=%s'% i)
    print(res.text)