#راح اشرح سحب اتصال اضهار يوزر حساب تيك من ايميل 


import requests,SignerPy
from typing import Any
def xor(String:str) -> Any:
    return "".join([hex(ord(c)^5)[2:]for c in String])

url = "https://api32-normal-alisg.tiktokv.com/passport/account_lookup/email/"
params = {
    "request_tag_from": "h5",
    "fixed_mix_mode": "1",
    "mix_mode": "1",
    "account_param": xor("atro@gmail.com"),
    "scene": "1", #هذا راح اسويه واحد اذا سويتها واحد راح يصير يوزر "" بدل ******
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": "1755466425423",
    "cdid": "cefe6f9c-d9d9-4107-9543-f5226d5b3ccd",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "1600*900",
    "dpi": "240",
    "device_type": "SM-S908E",
    "device_brand": "samsung",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "DE",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1754825061",
    "mcc_mnc": "26202",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "262",
    "residence": "DE",
    "app_language": "en",
    "carrier_region": "DE",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "en",
    "content_language": "en,",
    "ac2": "wifi",
    "uoo": "1",
    "op_region": "DE",
    "build_number": "37.8.5",
    "region": "US",
    "ts": "1755466424",
    "iid": "7536212628504381192",
    "device_id": "7536211658156213782",
    "openudid": "4196494d5939fa86",
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "type":"3736",
    "app_version":"37.8.5"
}
cookies = {
    "passport_csrf_token": "d52c500f67607c862972a043a4662972",
    "passport_csrf_token_default": "d52c500f67607c862972a043a4662972",
    "install_id": "7536212628504381192",
}
#راح استخدم اصطناعي يقسم ال url الى url و params الي يريد يسويه يدوي اكو بل url بيه علامة استفهام الي بعده هو params
m=SignerPy.sign(params=params,cookie=cookies)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
  'x-tt-pba-enable': "1",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket':m['x-ss-req-ticket'],
  'x-bd-client-key': "#LFLluN0wIdQaDxIXUUvEDzSMeYqmuwelaqRmzYJxN3Sl5PDfyg0ZQMCLkYm+QRisqBm2hpAXzDekRo0e",
  'x-tt-passport-csrf-token': "d52c500f67607c862972a043a4662972",
 
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",

  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon':m['x-ladon'],
  'x-khronos':m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon':m['x-gorgon'],
  'content-type': "application/x-www-form-urlencoded",
  'content-length': m['content-length'],

}

response = requests.post(url, headers=headers,params=params,cookies=cookies)

print(response.text)
passport_ticket=response.json()["data"]["accounts"][0]["passport_ticket"]
email = requests.post("https://api.internal.temp-mail.io/api/v3/email/new").json()["email"]
params.update({"email":xor(email),"not_login_ticket":passport_ticket})
#not_login_ticket 

#نتضرونا بي شروحات قادمه 
#نسخه تلكوها بي قناتي تلكو رابطها بي اول تعليق
#by => s1
url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"

# payload = {
#   'rules_version': "v2",
#   'account_sdk_source': "app",
#   'mix_mode': "1",
#   'multi_login': "1",
#   'type': "3436",
#   'email': "6471776a456268646c692b666a68",
#   'email_theme': "2",
#   'use_passport_ticket': "1"
# }
m=SignerPy.sign(params=params,cookie=cookies)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)",
  'Accept-Encoding': "gzip",
  'x-ss-stub':m['x-ss-stub'],
  'x-tt-pba-enable': "1",
  'x-tt-multi-sids': "6639559680287080453%3Af67dac7231a906f233a957f8965344ba",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket': m['x-ss-req-ticket'],
  'x-bd-client-key': "#LFLluN0wIdQaDxIXUUvEDzSMeYqmuwelaqRmzYJxN3Sl5PDfyg0ZQMCLkYm+QRisqBm2hpAXzDekRo0e",
  'x-tt-passport-csrf-token': "d52c500f67607c862972a043a4662972",
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'x-tt-bypass-dp': "1",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon':m['x-ladon'],
  'x-khronos':m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon':m['x-gorgon'],
}

response = requests.post(url,params=params, headers=headers,cookies=cookies)

print(response.text)
import time
time.sleep(5)

message = requests.get("https://api.internal.temp-mail.io/api/v3/email/{}/messages".format(email))
print(message.text)
username = message.text.split("generated for")[1].split("\n")[0].strip().rstrip(".")
#يمكن يصير بيه خلل اذا يوزر بيه نقاط مثلا اذا يوزر بيه نقاط يجب نص الي قبله  ته صلحوها

print(username)