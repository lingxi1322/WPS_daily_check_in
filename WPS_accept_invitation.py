invite_userids = [244668941]

import json, os, time
import requests


sids = [
    "V02Sw9-goMQAxyEQu_EULMetb-INZo000af1142c00479959d8",
    "V02S0R96lUd8ZEzQtyjxZX-kHQ2_tpk00a28f1650047c345ee",
    "V02SBxbHOhf4rcYlBaXzTfJ8WC3B6PE00aa5f34d0038de5bac",
    "V02SRvwTFf68enT4JrOPhQkKrKKqv5k00ab38f8500380673c8",
    "V02SS1Aj322-C9Z-P36iZF2epL78zOQ00a7ea26400300425d3",
    "V02S96aSosktKJiRKwEwBhqiWKHhxkE00a01300600374985fe",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02SzpPttrDh9DtVZZjuSixmKOYsAuU00a98ee4a0047756591",
    "V02SkTszoOYP88gtXvH1cXoDrMGoEGg00af1f571004626b252",
    "V02SEdbqgnwva8UpfFOiw5BmksbY_JY00a53a2c300461f24f7",
    "V02S6UQdQhot5IO9pmvBnEuiiVGcCYU00a6bc19c0047b369fa",
#     "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]
mk = 0

def request_re(sid, invite_userid, rep = 31):
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    r = requests.post( invite_url, headers={ 'sid': sid }, data={ 'invite_userid': invite_userid, "client_code": "040ce6c23213494c8de9653e0074YX30", "client": "alipay" } )
    js = json.loads(r.content)
    if js['msg'] == 'tryLater' and rep > 0:
        rep -= 1
        time.sleep(20)
        r = request_re(sid, invite_userid, rep)
    return r

for i in invite_userids:
    for j in sids:
        try:
            r = request_re(j, i)
            js = json.loads(r.content)
            if js['result'] == 'ok':
                mk += 1
        except:pass
            
print('成功邀请%d位好友'%(mk))   

SERVER_KEY = os.getenv('SERVER_KEY')
if SERVER_KEY:
    data = {
        'text':'WPS邀请好友任务：成功邀请到%d位好友'%(mk),
        'desp':'成功邀请%d位好友'%(mk)
    }
    requests.post('https://sc.ftqq.com/%s.send'%(SERVER_KEY.strip()), data = data)

BARK_URL = os.getenv('BARK_URL')
if BARK_URL:
    text = 'WPS邀请好友任务：成功邀请到%d位好友'%(mk)
    bark_url = BARK_URL[:-1] if BARK_URL.endswith('/') else BARK_URL
    requests.get(bark_url + '/%s'%(text))
    
QMSG_KEY = os.getenv('QMSG_KEY')
if QMSG_KEY:
    text = 'WPS邀请好友任务：成功邀请到%d位好友'%(mk)
    requests.get('https://qmsg.zendee.cn/send/%s?msg=%s'%(QMSG_KEY.strip(), text))
