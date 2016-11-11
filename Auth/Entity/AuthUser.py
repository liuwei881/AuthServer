#coding=utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime,Date
from lib.Route import BaseModel

class UserList(BaseModel):
    """
    用户信息列表
    """
    __tablename__ = 'bk_user_list'

    UserId = Column('fi_id', Integer, primary_key=True)             #用户ID
    Department = Column('fs_department', String(100))             #部门ID
    CompanyName = Column('fs_companyname', String(100))              #公司名称
    Position = Column('fs_position', String(255))                   #职位名称
    UserName = Column('fs_username', String(100))                   #用户名称
    Sex = Column('fs_sex', String(50))                                 #性别
    UserAccount = Column('fs_user_account', String(50))              #用户账号
    PassWord = Column('fs_password', String(100))                   #密码
    TelePhone = Column('fs_telephone', String(50))                  #电话
    Area = Column('fs_area', String(100))                           #区域ID
    Address = Column('fs_address', String(200))                     #地址
    Phone = Column('fs_phone', String(50))                          #手机
    Email = Column('fs_email', String(100))                         #Email
    Postcode = Column('fs_postcode', String(10))                    #邮编
    OutsideLogin = Column('fi_outside_login', Integer)               #是否允许外网登录
    BirthDay = Column('ft_birthday', Date)                      #生日
    LastLogin = Column('ft_last_login', DateTime)                    #最近登录时间
    LastUpdatePwd = Column('ft_last_update_pwd', DateTime)      #最近修改密码时间
    Is_valid = Column('fi_valid', Integer)                          #是否有效
    Comment = Column('fs_comment', String(255))                     #备注
    Create = Column('fs_create', String(100))                       #创建人ID
    CreateTime = Column('ft_create_time', DateTime)                 #创建时间
    Update = Column('fs_update', String(100))                       #修改人ID
    UpdateTime = Column('ft_update_time', DateTime)                 #修改时间

    def toDict(self):
        return {
            'UserId': self.UserId,
            'Department':self.Department,
            'CompanyName':self.CompanyName,
            'Position':self.Position,
            'UserName': self.UserName,
            'Sex':self.Sex,
            'UserAccount':self.UserAccount,
            'PassWord': self.PassWord,
            'TelePhone':self.TelePhone,
            'Area':self.Area,
            'Address': self.Address,
            'Phone':self.Phone,
            'Email':self.Email,
            'Postcode': self.Postcode,
            'OutsideLogin':self.OutsideLogin,
            'BirthDay':self.BirthDay.strftime('%Y/%m/%d') if self.BirthDay else '',
            'LastLogin':self.LastLogin.strftime('%Y-%m-%d %H:%M:%S') if self.LastLogin else '',
            'LastUpdatePwd': self.LastUpdatePwd.strftime('%Y-%m-%d %H:%M:%S') if self.LastUpdatePwd else '',
            'Is_valid':{0:"否",1:"是"}.get(self.Is_valid),
            'Comment':self.Comment,
            'Create':self.Create,
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'Update':self.Update,
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else ''
        }