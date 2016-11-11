#coding=utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel

class UserRoleList(BaseModel):
    """
    用户角色列表
    """
    __tablename__ = 'bk_user_role_list'

    UserRoleId = Column('fi_user_role_id', Integer, primary_key=True)    #用户角色ID
    UserId = Column('fi_user_id', Integer)                          #用户ID
    RoleId = Column('fi_role_id',Integer)                           #角色ID
    CreateId = Column('fi_create_id', Integer)                      #创建人ID
    CreateTime = Column('ft_create_time', DateTime)                 #创建时间
    UpdateId = Column('fi_update_id', Integer)                      #修改人ID
    UpdateTime = Column('ft_update_time', DateTime)                 #修改时间

    def toDict(self):
        return {
            'UserRoleId': self.UserRoleId,
            'UserId':self.UserId,
            'RoleId':self.RoleId,
            'CreateId':self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId':self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }
