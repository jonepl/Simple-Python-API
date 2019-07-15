import os
from functools import wraps
from flask import request, request, abort

try:
    from config.creds import api_keys
except(AttributeError, ModuleNotFoundError) as e:
    api_keys = os.environ["api_keys"]

def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') in api_keys:
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function