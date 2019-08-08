#coding=utf8
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


def main():
    itchat.auto_login()
    itchat.send(u'测试消息发送', 'filetranser')
    print(itchat.get_friends().decode('utf-8''))
    itchat.run()


