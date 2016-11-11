#coding=utf-8


import logging
import json
import os
import signal
import urllib
import urlparse
import sys

from multiprocessing.process import Process


from oauth2 import Provider
from oauth2.error import UserNotAuthenticated
from oauth2.grant import AuthorizationCodeGrant
from oauth2.tokengenerator import Uuid4
from oauth2.store.memory import ClientStore, TokenStore
from oauth2.web import AuthorizationCodeGrantSiteAdapter
from oauth2.web.tornado import OAuth2Handler
from tornado.ioloop import IOLoop
from tornado.web import Application, url
from wsgiref.simple_server import WSGIRequestHandler
from Auth.Handlers.AuthHander import MainHandler

logging.basicConfig(level=logging.DEBUG)

class ClientRequestHandler(WSGIRequestHandler):
    """
    Request handler that enables formatting of the log messages on the console.

    This handler is used by the client application.
    """
    def address_string(self):
        return "client app"


class OAuthRequestHandler(WSGIRequestHandler):
    """
    Request handler that enables formatting of the log messages on the console.

    This handler is used by the python-oauth2 application.
    """
    def address_string(self):
        return "python-oauth2"


class TestSiteAdapter(AuthorizationCodeGrantSiteAdapter):
    """
    This adapter renders a confirmation page so the user can confirm the auth
    request.
    """

    CONFIRMATION_TEMPLATE = """
    <html lang="zh-cn">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>平台登录</title>

<link href="static/css/bootstrap.min.css" rel="stylesheet">
<link href="static/css/signin.css" rel="stylesheet">

</head>
<body>

<div class="signin">
        <div class="signin-head"><img src="static/images/icon_zxr.png" alt="" class=""></div>
        <form class="form-signin" action="/" role="form" method="post">
                <input type="text" class="form-control" placeholder="用户名" name="username" required autofocus />
                <input type="password" class="form-control" placeholder="密码" name="password" required />
                <button class="btn btn-lg btn-warning btn-block" type="submit">登录</button>
        </form>
</div>
<div style="text-align:center;margin:50px 0; font:normal 14px/24px 'MicroSoft YaHei';">
</div>
</body>
</html>
    """

    def render_auth_page(self, request, response, environ, scopes, client):
        #url = request.path + "?" + request.query_string
        response.body = self.CONFIRMATION_TEMPLATE

        return response

    def authenticate(self, request, environ, scopes, client):
        if request.method == "POST":
            if request.post_param("confirm") == "confirm":
                return {}
        raise UserNotAuthenticated

    def user_has_denied_access(self, request):
        if request.method == "POST":
            if request.get_param("deny") == "deny":
                return True
        return False

def run_auth_server():
    client_store = ClientStore()
    client_store.add_client(client_id="abc", client_secret="xyz",
                            redirect_uris=["http://10.10.112.59:8081/callback"])
    client_store.add_client(client_id="bcd", client_secret="fff",
                            redirect_uris=["http://10.10.112.59:50000/callback"])
    client_store.add_client(client_id="9fdc2c7a1cee0cca54c150e3e0b822eb", client_secret="zzz",
                            redirect_uris=["http://10.10.112.59:8888/callback"])

    token_store = TokenStore()

    provider = Provider(access_token_store=token_store,
                        auth_code_store=token_store, client_store=client_store,
                        token_generator=Uuid4())
    provider.add_grant(AuthorizationCodeGrant(site_adapter=TestSiteAdapter()))

    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret='61oETzKXQAGaYdkL5gEmGEJJFuYh7EQnp2XdTP1o/Vo=',
    )
    try:
        app = Application([
            url(provider.authorize_path, OAuth2Handler, dict(provider=provider)),
            url(provider.token_path, OAuth2Handler, dict(provider=provider)),
            url("/", MainHandler),
        ], **settings)

        app.listen(8080)
        print "Starting OAuth2 server on http://10.10.112.59:8080/..."
        IOLoop.current().start()

    except KeyboardInterrupt:
        IOLoop.close()


def main():
    auth_server = Process(target=run_auth_server)
    auth_server.start()
    print "Access http://10.10.112.59:8081/app in your browser"

    def sigint_handler(signal, frame):
        print "Terminating servers..."
        auth_server.terminate()
        auth_server.join()

    signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
