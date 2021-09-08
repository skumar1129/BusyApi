from app import app as application
if __name__ == '__main__':
    application.run(ssl_context='adhoc', host='127.0.0.1')