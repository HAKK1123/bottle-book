from email.mime import application
import bottle
import routes_login
import routes_list
import routes_login
from utils.session import Session

app = routes_login.app
app_sess = routes_login.app_sess

if __name__ == '__main__':
    bottle.run(app=app_sess, host= '0.0.0.0', port=8888, reloader=True, debug=True)
else:
    application = app_sess