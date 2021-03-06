from constants.enum import *


class MyInfo(object):
    """"信息类"""

    # 好友信息表(包括群) remark_name -> user_id //global_friends_list
    user_name_to_user_id = dict()

    # 聊天信息 chat_id -> chat_info() //global_chat_info
    chat_id_to_chat_info = dict()

    # 用户ID与聊天ID映射表 user_id -> chat_id // global_name_id_map
    user_id_to_chat_id = dict()

    # 好友信息 user_id -> friend_info() // global_friend_info
    user_id_to_friend_info = dict()

    def __init__(self):
        self.user_name_to_user_id = dict()
        self.chat_id_to_chat_info = dict()
        self.user_id_to_chat_id = dict()
        self.user_id_to_friend_info = dict()

    def set_user_name_to_user_id(self, user_name, user_id):
        self.user_name_to_user_id[user_name] = user_id

    def get_user_name_to_user_id(self, user_name):
        return self.user_name_to_user_id[user_name]

    def del_user_name_to_user_id(self, user_name):
        self.user_name_to_user_id.pop(user_name)

    def check_user_name_to_user_id(self, user_name):
        if user_name in self.user_name_to_user_id:
            return True
        else:
            return False

    def set_chat_id_to_chat_info(self, chat_id, chat_info):
        self.chat_id_to_chat_info[chat_id] = chat_info

    def get_chat_id_to_chat_info(self, chat_id):
        return self.chat_id_to_chat_info[chat_id]

    def del_chat_id_to_chat_info(self, chat_id):
        self.chat_id_to_chat_info.pop(chat_id)

    def check_chat_id_to_chat_info(self, chat_id):
        if chat_id in self.chat_id_to_chat_info:
            return True
        else:
            return False

    def set_user_id_to_chat_id(self, user_id, chat_id):
        self.user_id_to_chat_id[user_id] = chat_id

    def get_user_id_to_chat_id(self, user_id):
        return self.user_id_to_chat_id[user_id]

    def del_user_id_to_chat_id(self, user_id):
        self.user_id_to_chat_id.pop(user_id)

    def check_user_id_to_chat_id(self, user_id):
        if user_id in self.user_id_to_chat_id:
            return True
        else:
            return False

    def set_user_id_to_friend_info(self, user_id, friend_info):
        self.user_id_to_friend_info[user_id] = friend_info

    def get_user_id_to_friend_info(self, user_id):
        return self.user_id_to_friend_info[user_id]

    def del_user_id_to_friend_info(self, user_id):
        self.user_id_to_friend_info.pop(user_id)

    def check_user_id_to_friend_info(self, user_id):
        if user_id in self.user_id_to_friend_info:
            return True
        else:
            return False


class ChatUnit(object):
    """聊天信息"""

    # 密钥信息
    aes_key = ""
    rsa_public_key_name = ""
    rsa_private_key_name = ""

    # 主聊天者(发起加密聊天的好友)
    is_master = False

    # 期望确认消息个数
    expect_ack_count = 0

    # 实际已确认消息个数
    actual_ack_count = 0

    # 密钥数组
    key_info_list = list()

    # 协商成功标志
    is_chat_ready = False

    # 聊天id协商成功标志
    is_id_ready = False

    # 时间戳
    time = 0

    # 好友ID
    user_id = ""

    # 好友名称
    user_name = ""

    # 当前协商步骤
    agreement_step = AGREEMENT_INIT

    # 更新密钥中
    is_update_key = False

    def __init__(self):
        """"初始化"""
        self.is_chat_ready = False
        self.is_id_ready = False
        self.expect_ack_count = 0
        self.actual_ack_count = 0
        self.chat_user_name = ""
        self.rsa_public_key_name = ""
        self.rsa_private_key_name = ""
        self.is_master = False
        self.time = 0
        self.user_name = ""
        self.agreement_step = AGREEMENT_INIT
        self.is_update_key = False

    def set_aes_key(self, key):
        self.aes_key = key

    def get_aes_key(self):
        return self.aes_key

    def set_rsa_key(self, public_key, private_key):
        self.rsa_public_key_name = public_key
        self.rsa_private_key_name = private_key

    def get_rsa_key(self):
        return self.rsa_public_key_name, self.rsa_private_key_name

    def get_rsa_public_key(self):
        return self.rsa_public_key_name

    def get_rsa_private_key(self):
        return self.rsa_private_key_name

    def gen_new_rsa_key(self):
        # todo
        return

    def set_agreement_step(self, agreement_step):
        self.agreement_step = agreement_step

    def is_agreement_processing(self):
        if self.agreement_step != AGREEMENT_INIT:
            return True
        else:
            return False


class FriendInfo:
    """
    微信好友信息
    """
    user_id = ""
    nick_name = ""
    remark_name = ""
    friend_count = 0

    def __init__(self, user_id='', nick_name='', remark_name='', friend_count=0):
        self.user_id = user_id
        self.nick_name = nick_name
        self.remark_name = remark_name
        self.friend_count = friend_count


class KeyInfo:
    """
        密钥信息
    """
    user_id = ""
    aes_key = ""
    time_stamp = ""

    def __init__(self, user_id='', aes_key='', time_stamp=''):
        self.user_id = user_id
        self.aes_key = aes_key
        self.time_stamp = time_stamp


class ChatterInfo(object):
    """当前聊天者信息"""
    user_id = ""
    user_name = ""

    def __init__(self, user_id="", user_name=""):
        self.user_id = user_id
        self.user_name = user_name

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def is_current_empty(self):
        if self.user_name == "" or self.user_id == "":
            return True
        else:
            return False
