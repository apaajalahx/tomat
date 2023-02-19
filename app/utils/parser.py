# # # # # # # # # # # # # # # # # # # # #
# Name: Parser Handler                  #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
import functools
from .response import MakeJsonError, InvalidLocationException

try:
    from flask import request, Flask
except ImportError:
    print("Error: please install package flask >= 2.2.3")
    exit()

class Options:
    """
        Global Option for Parser.
    """
    def __init__(self, *args, **kwargs):
        self.missing = kwargs.get('missing', None)
        self.length = kwargs.get('length', 0)

class ParsingError:
    pass


class ParsingLocation:
    
    def __init__(self, location) -> None:
        self.location = location
    
    def parser(self):
        if self.location == 'form':
            return request.form
        elif self.location == 'query':
            return request.args
        elif self.location == 'json':
            return request.get_json()
        else:
            InvalidLocationException('Request() Location Error: {}'.format(self.location))


class String:

    def __init__(self, name: str | None =None, 
                       required: bool = False,
                       **options) -> None:
        self.optionParser = Options(**options)
        self.name = name
        self.required = required
    
    def handler(self, location: str, key: str):
        parser = ParsingLocation(location)
        parser = parser.parser()
        
        # if key not in request.args:
        return 'memek'

def Request(arg, location: str = 'form'):
    def decorator(f):
        @functools.wraps(f)
        def parser(*args, **kwargs):
            create_return = {}
            for key, value in arg.items():
                print(key, value)
                if 'class' in str(type(value)):
                    create_return[key] = value.handler(location, key)
            return f(create_return, *args, **kwargs)
        return parser
    return decorator

app = Flask(__name__)

@app.route('/test/<id>', methods=['GET'])
@Request({'data' : String(required=True), 'error': String(required=True)}, location='query')
def test(args, id):
    print(args)
    print(id)
    return 'oke'

app.run('127.0.0.1', 8000, debug=True)