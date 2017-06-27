# coding: utf-8

from leancloud import HttpsRedirectMiddleware
from leancloud import Engine
from leancloud import LeanEngineError

from app import app


# 需要重定向到 HTTPS 可去除下一行的注释。
# app = HttpsRedirectMiddleware(app)
engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'