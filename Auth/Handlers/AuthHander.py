#coding=utf-8

import hashlib

from lib.basehandler import BaseHandler
from lib.tools import md5hash
from tornado import web
from Auth.Entity.AuthUser import UserList
from Auth.Entity.UserLogin import UserLoginList
from Auth.Entity.UserRole import UserRoleList
from Auth.Entity.RoleRight import RoleRightList
from Auth.Entity.MenuList import MenuList
from lib.RedisCache import RightsCache
import datetime,json

class MainHandler(BaseHandler):
	@web.asynchronous
	def post(self):
		username = self.get_argument('username')
		password = self.get_argument('password')
		passwd = md5hash("".join(["iprun",md5hash(password),"admin"]))
		try:
			user = self.db.query(UserList).filter(UserList.UserName == username, UserList.PassWord == passwd).first()
			if user:
				self._doLogin(user)
			else:
				self.render("login_fail.html")
		except Exception, e:
			print e
			self.render("login_fail.html")

	def _doLogin(self, user):
		self.set_secure_cookie('user', str(user.UserId), expires_days=0.5)
		self.set_cookie('username', str(user.UserName), expires_days=0.5)
		self.set_cookie('d', str(user.Department))
		try:
			if user.UserId == 1:
				objLogLogin = UserLoginList()
				objLogLogin.UserId = user.UserId
				objLogLogin.LoginIp = self.request.remote_ip 
				objLogLogin.LoginTime = datetime.datetime.now()
				self.db.add(objLogLogin)
				self.db.commit()
				self.set_cookie('logid', str(objLogLogin.LoginId))
			else:
				rights = {}
				roleid = self.db.query(UserRoleList).filter(UserRoleList.UserId == int(user.UserId)).first().RoleId
				menulist = self.db.query(RoleRightList).filter(RoleRightList.RoleId == roleid).all()
				menuurl = [{self.db.query(MenuList).filter(MenuList.MenuId == i.MenuId).first().Url: [i.MenuPost, i.MenuGet, i.MenuPut, i.MenuDel]} for i in menulist]
				username = self.db.query(UserList).filter(UserList.UserId == user.UserId).first().UserName
				rights[username] = menuurl
				RightsCache.set("User{0}Right".format(user.UserId), json.dumps(rights))
				objLogLogin = UserLoginList()
				objLogLogin.UserId = user.UserId
				objLogLogin.LoginIp = self.request.remote_ip
				objLogLogin.LoginTime = datetime.datetime.now()
				self.db.add(objLogLogin)
				self.db.commit()
				self.set_cookie('logid', str(objLogLogin.LoginId))
			client_id = self.get_cookie("client_id")
			d = {"abc": "http://10.10.112.59:8081",
				 "bcd": "http://10.10.112.59:50000",
				 "9fdc2c7a1cee0cca54c150e3e0b822eb": "http://10.10.112.59:8888/#/"}
			self.redirect(d[client_id])
		except Exception, e:
                        print e
			self.render("login_fail.html")
