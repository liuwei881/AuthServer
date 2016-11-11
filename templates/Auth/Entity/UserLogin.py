#coding=utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel

class UserLoginList(BaseModel):
    """
    用户登录日志
    """
    __tablename__ = 'bk_user_login_list'

    LoginId = Column('fi_login_id', Integer, primary_key=True)      #登录记录ID
    UserId = Column('fi_user_id', Integer)                          #用户ID
    LoginIp = Column('fs_login_ip',String(50))                      #登录IP
    LoginTime = Column('ft_login_time', DateTime)                   #登录时间
    ExitTime = Column('ft_exit_time', DateTime)                     #退出时间

    def toDict(self):
        return {
            'LoginId': self.LoginId,
            'UserId':self.UserId,
            'LoginIp':self.LoginIp,
            'LoginTime': self.LoginTime.strftime('%Y-%m-%d %H:%M:%S') if self.LoginTime else '',
            'ExitTime': self.ExitTime.strftime('%Y-%m-%d %H:%M:%S') if self.ExitTime else ''
        }