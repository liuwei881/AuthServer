#coding=utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime
from lib.Route import BaseModel

class MenuList(BaseModel):
    """
    菜单管理
    """
    __tablename__ = 'bk_menu_list'

    MenuId = Column('fi_menu_id', Integer, primary_key=True)        #菜单ID
    MenuName = Column('fs_menu_name', String(255))                   #菜单名称
    Url = Column('fs_url',String(255))                              #URL
    ParentMenu = Column('fi_parent_menu', Integer)                  #父菜单
    Desc = Column('fs_desc',String(255))                             #描述
    SerialNumber = Column('fi_sn', Integer)                         #序号
    Show = Column('fi_show', Integer)                               #是否显示
    CreateId = Column('fi_create_id', Integer)                       #创建人ID
    CreateTime = Column('ft_create_time', DateTime)                 #创建时间
    UpdateId = Column('fi_update_id', Integer)                       #修改人ID
    UpdateTime = Column('ft_update_time', DateTime)                 #修改时间

    def toDict(self):
        return {
            'MenuId': self.MenuId,
            'MenuName':self.MenuName,
            'Url':self.Url,
            'ParentMenu':self.ParentMenu,
            'Desc':self.Desc,
            'SerialNumber':self.SerialNumber,
            'Show':self.Show,
            'CreateId':self.CreateId,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId':self.UpdateId,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }
