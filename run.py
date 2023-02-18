from app import create_app
import os

app = create_app(os.getenv('APP_ENV', 'development'))

if __name__ == '__main__':
    app.run('127.0.0.1', port=8000)