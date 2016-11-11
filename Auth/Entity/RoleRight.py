#coding=utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel

class RoleRightList(BaseModel):
    """
    角色权限管理
    """
    __tablename__ = 'bk_role_right_list'

    RightId = Column('fi_right_id', Integer, primary_key=True)      #Right_id
    RoleId = Column('fi_role_id', Integer)                          #角色ID
    MenuId = Column('fi_menu_id',Integer)                           #菜单功能ID
    MenuPost = Column('fs_menu_post', String(100))                  #角色创建权限
    MenuPut = Column('fs_menu_put', String(100))                    #角色修改权限
    MenuGet = Column('fs_menu_get', String(100))                    #角色查看权限
    MenuDel = Column('fs_menu_del', String(100))                    #角色删除权限
    CreateId = Column('fi_create_id', Integer)                      #创建人ID
    CreateTime = Column('ft_create_time', DateTime)                 #创建时间
    UpdateId = Column('fi_update_id', Integer)                       #修改人ID
    UpdateTime = Column('ft_update_time', DateTime)                 #修改时间

    def toDict(self):
        return {
            'RightId': self.RightId,
            'RoleId':self.RoleId,
            'MenuId':self.MenuId,
            'MenuPost': self.MenuPost,
            'MenuPut': self.MenuPut,
            'MenuGet': self.MenuGet,
            'MenuDel': self.MenuDel,
            'CreateId':self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId':self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }