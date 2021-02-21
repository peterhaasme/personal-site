# app.py

from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix
from flask_site import app as flask_site

application = DispatcherMiddleware(flask_site)

'''
application = DispatcherMiddleware(flask_app_1, {
    '/flask_app_2': flask_app_2
})
'''
