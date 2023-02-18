# # # # # # # # # # # # # # # # # # # # #
# Name: File Handler                    #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
import os
import base64
from .response import InvalidExtensionException
from .function import randomString


class File:

    def __init__(self) -> None:
        pass

    def __getExtensionFromb64(self, b64: str):
        enum = {
            'JVBERi0' : 'pdf',
            'R0lGODdh' : 'gif',
            'R0lGODlh' : 'gif',
            'iVBORw0KGgo' : 'png',
            '/9j/' : 'jpg'
        }
        for key, value in enumerate(enum):
            if b64.startswith(key):
                return value
        return None

    
    def __b64CheckExtAndMime(self, tenChar: str, mimeType: str) -> bool:
        get_allowed_ext = str(os.getenv('ALLOWED_EXTENSION', 'jpg,png')).split(',')
        get_allowed_mime = str(os.getenv('ALLOWED_MIME', 'image')).split(',')
        is_allowed_mime = False
        is_allowed_ext = False
        get_extension = self.__getExtensionFromb64(tenChar)
        
        if get_extension is None:
            raise InvalidExtensionException('Cannot Get Extension.')
        
        if get_extension in get_allowed_ext:
            is_allowed_ext = True

        for mime in get_allowed_mime:
            for ext in get_allowed_ext:
                if '/'.join(mime, ext) == mimeType:
                    is_allowed_mime = True
                    break

        if is_allowed_ext and is_allowed_mime:
            return get_extension

        raise InvalidExtensionException('Extension is not allowed')

    def upload(self, b64: str, upload_path: str, name: str | None = None) -> bool:
        try:
            split_b64 = b64.split(',')
            if len(split_b64) < 2:
                return False

            mimeType = split_b64[0].split(';')[0].split(':')[-1]
            get_extension = self.__b64CheckExtAndMime(split_b64[1][0:25], mimeType)
            
            name = name if name is not None else randomString(12)
            with open(os.path.join(upload_path, '.'.join(name, get_extension)), 'wb') as openfile:
                openfile.write(base64.decodebytes(split_b64[1]))
            openfile.close()
            
            return True
        except:
            return False