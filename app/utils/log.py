# # # # # # # # # # # # # # # # # # # # #
# Name: Function Handler                #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
import os


class Log:

    def __init__(self, app=None, as_email: bool = False, as_sentry: bool = False) -> None:
        if as_email:
            self.setEmail(app)
        if as_sentry:
            self.setSentry()

    def setEmail(self, app):
        try:
            import logging
            from logging.handlers import SMTPHandler
        except ImportError:
            print("Error: import error aborted")
            exit(0)

        if app is None:
            print("Error: App is required in as_email")
            exit(0)

        mail_handler = SMTPHandler(
            mailhost=os.getenv('ERROR_MAIL_HOST', '127.0.0.1'),
            fromaddr=os.getenv('ERROR_FROM_ADDR', 'admin@example.com'),
            toaddrs=os.getenv('ERROR_TO_ADDR', 'error@example.com'),
            credentials=(os.getenv('ERROR_MAIL_USERNAME', 'admin@example.com'), os.getenv('ERROR_MAIL_PASSWORD', 'password'))
        )

        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    def setSentry(self):
        try:
            import sentry_sdk
            from sentry_sdk.integrations.flask import FlaskIntegration
        except ImportError:
            print("Error: try \npip install 'sentry-sdk[flask]'")
            exit(0)
        
        sentry_sdk.init(
            dsn=os.getenv('SENTRY_DSN', None),
            integrations=[
                FlaskIntegration(),
            ],
            traces_sample_rate=1.0,
        )

        