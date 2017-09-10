from WxRobot.webwxapi import WebWxAPI
from WxRobot.wxrobot import WxRobot

api = WebWxAPI()
robot = WxRobot(api)

@api.allMsg
def TextMsgHandler(message):
    items=['腾讯新闻', '汇跑赛事']
    subject_set = frozenset(items)
    if message.fromUserName in subject_set:
        api.sendTextMsg("softidy",message.content)
        print('send msg to softidy')
    #print('%s给%s发了一条消息 all :%s'%(message.fromUserName,message.toUserName,message.content))
    return 'Hello World'


@robot.command('send','send [name] [message]')
def sendCommand(name,text):
    api.sendTextMsg(name,text)

if __name__ == '__main__':
    robot.start()
