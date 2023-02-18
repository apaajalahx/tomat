# # # # # # # # # # # # # # # # # # # # #
# Name: Route Handler                   #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
from flask import Flask, Blueprint
from .response import InvalidMethodsException
from functools import wraps


class Route:

    def __init__(self) -> None:
        self.route_prefix = self.__class__.__name__.replace('View', '')
        self.blueprint = Blueprint(self.__class__.__name__, __name__, url_prefix='/{}'.format(self.route_prefix.lower()))

    def register(self, app: Flask = None):
        self.app = app
        get_all_function = [c for c in self.__class__.__dict__.keys() if '__' not in c]

        if 'index' in get_all_function:
            self.blueprint.add_url_rule('/', view_func=self.__class__().index, methods=['GET'])
        
        if 'show' in get_all_function:
            self.blueprint.add_url_rule('/show/<id>', view_func=self.__class__().show, methods=['GET'])

        if 'update' in get_all_function:
            self.blueprint.add_url_rule('/update/<id>', view_func=self.__class__().update, methods=['POST'])
        
        if 'store' in get_all_function:
            self.blueprint.add_url_rule('/store', view_func=self.__class__().store, methods=['POST'])
        
        if 'destroy' in get_all_function:
            self.blueprint.add_url_rule('/destroy/<id>', view_func=self.__class__().destroy, methods=['DELETE'])

        remove_function_list = ('index', 'show', 'update', 'store', 'destroy')
        for remove_func in remove_function_list:
            if remove_func in get_all_function:
                get_all_function.remove(remove_func)

        list_available_methods = ['GET', 'POST', 'DELETE', 'PUT']
        for func in get_all_function:
            d = getattr(self.__class__(), func)
            if hasattr(d.__func__, 'methods') and hasattr(d.__func__, 'endpoint'):
                def validate_available_method(methods):
                    if len(methods) == 0:
                        raise InvalidMethodsException('array methods cannot be empty')
                    for method in methods:
                        if method not in list_available_methods:
                            raise InvalidMethodsException('method {} is not allowed'.format(method))
                    return False
                
                validate_available_method(d.__func__.methods)

                if d.__func__.endpoint is not None:
                    self.blueprint.add_url_rule(d.__func__.endpoint, view_func=d, methods=d.__func__.methods)
                    
                
        app.register_blueprint(self.blueprint)

def route(endpoint=None, methods=['GET']):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        wrapper.methods = methods
        wrapper.endpoint = endpoint
        return wrapper
    return decorator