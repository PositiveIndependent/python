import requests
import time
from pprint import pprint
# https://oauth.vk.com/authorize?client_id=51709508&display=page&scope=stats,offline&response_type=token&v=5.131

def get_token(file):
    with open(file, 'r') as file_object:
        object = file_object.read().strip()
        return object

token1 = get_token('token.txt')
token2 = get_token('token2.txt')


class VkUser:
    def __init__(self, token, version=5.131):
        self.token = token
        self.version = version

    def get_friends(self):
        URL = 'https://api.vk.com/method/users.search'
        params = {
            'access_token': self.token,
            'v':'5.131',
            'from_list': 'friends'
        }
        friends = requests.get(URL, params=params).json()
        friends2 = {}
        for friend in friends['response']['items']:
            key = friend['id']
            value = friend['first_name'] + ' ' + friend['last_name']
            friends2[key] = value
        return friends2

    def set_id(object):
        friends = object.get_friends()
        set = {x for x in friends.keys()}
        return set

    def __and__(self, other):
        self_set = self.set_id()
        other_set = other.set_id()
        result_set = self_set & other_set
        self_friends = self.get_friends()
        result = []
        for key, value in self_friends.items():
            if key in result_set:
                result.append(value)
        print(result)


    def __str__(self):
        URL = 'https://api.vk.com/method/users.get'
        params = {
            'access_token': self.token,
            'v': '5.131',
            'fields': 'domain'
        }
        res = requests.get(URL, params=params).json()
        domain = res['response'][0]['domain']
        link = 'https://vk.com/' + domain
        return link



# vk_client1 = VkUser(token1, '5.131')
# vk_client2 = VkUser(token2, '5.131')
#
# print(vk_client2&vk_client2)
# #
# # print(vk_client1.set_id())
# #
# print(vk_client2.get_friends())
# print(vk_client1.get_friends())
#
# print(vk_client2)

URL = 'https://api.vk.com/method/users.get'
params = {
    # 'user_ids': '457750818',
    'access_token': token2,
    'v':'5.131',
    'fields': 'domain, uid'
}
res = requests.get(URL, params=params).json()

# domain = res['response'][0]['domain']
# id = res['response'][0]['id']
pprint(res)
# print(domain)
# print(id)
