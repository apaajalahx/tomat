# # # # # # # # # # # # # # # # # # # # #
# Name: Auth Handler                    #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
import functools
from .route import route, Route
from .response import MakeJsonError, MakeJsonSuccess


class Auth:

    def __init__(self, app=None, db=None, route: bool = False) -> None:
        if app is not None:
            self.init_app(app, route)
    
    def init_app(self, app, db, route: bool = False):
        
        if route:
            AuthRoute().register(app)
    
    @staticmethod
    def auth(username: str, password: str) -> None:
        try:
            
            MakeJsonSuccess({
                'token' : 'jwt',
                'expired' : 86000
            }, 'success login', 200)
        except:
            pass
    
    @staticmethod
    def validate(jwt: str):
        pass


def auth_required(roles=['*']):
    def auth_decorated(f):
        @functools.wraps(f)
        def decorated(f, *args, **kwargs):

            return f(*args, **kwargs)
        return decorated
    return auth_decorated


class AuthRoute(Route):

    def __init__(self) -> None:
        super().__init__()
    
    @auth_required(roles=['*']) 
    @route(endpoint='/me', methods=['GET'])
    def me(self):
        pass