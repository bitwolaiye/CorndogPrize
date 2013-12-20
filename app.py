# encoding:utf-8
import codecs
import json
import urllib
from urllib2 import Request, urlopen
import sys

__author__ = 'zhouqi'

verified_type_dict_str = u'''
-1 屌丝
0 名人
1 政府
2 企业
3 媒体
4 校园
5 网站
6 应用
7 团体（机构）
8 待审企业
200 初级达人
220 中高级达人
400 已故V用户
10 微女郎
'''

verified_type_dict = dict([e.split(' ') for e in verified_type_dict_str.split('\n') if len(e)>0])
print verified_type_dict

base_api_url = 'https://api.weibo.com/2/'

access_token = '2.00jObfECIurWlC0e2627358fH1DWGD'
def get_base(url, params=None):
    if params is None:
        params = {'access_token': access_token}
    else:
        params['access_token'] = access_token
    if params:
        full_url = base_api_url + url + '?' + urllib.urlencode(params)
    else:
        full_url = base_api_url + url
    print full_url
    req = Request(full_url)
    return urlopen(req).read()



def get_comments(id='3634493107297962'):
    f = open('1.json', 'w')
    content = get_base('comments/show.json', {'id':id})
    f.write(content)
    f.close()
    return json.loads(content)


def get_status_id_from_mid(mid, type = 1, isBase62 = 1):
    return json.loads(get_base('statuses/queryid.json', {'mid': mid, 'type': type, 'isBase62': isBase62}))['id']


def get_verified_type(verified_type):
    verified_type = str(verified_type)
    if verified_type_dict.has_key(verified_type):
        return verified_type_dict[verified_type]
    else:
        return u'未知生物'


def gen_user_list_html(users):
    # f = open('1.md', 'w')
    f = codecs.open("1.md", "w", "utf-8")
    f.write(u'昵称|性别|主页|相册|认证\n')
    f.write(u'-|-|-|-|-\n')
    for u in users:
        u_str = u'%s|%s|%s|%s|%s\n' % (u['name'], u['gender'], 'http://weibo.com/' + u['profile_url'],
                                       'http://photo.weibo.com/%d/albums/index' % u['id'],
                                       get_verified_type(u['verified_type']))
        f.write(u_str)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        arg = dict([e.split('=') for e in arg.split('&')])
        comments = get_comments(get_status_id_from_mid(arg['mid']))
        gen_user_list_html([c['user'] for c in comments['comments']])
    else:
        get_comments()