# coding:utf-8

from . import api
from ihome import db
# import logging
from flask import current_app

@api.route("/index")
def index():
    # print ("hello")
    # logging.error()     #记录错误信息
    # logging.warn()      # 警告
    # logging.info()      # 信息
    # logging.debug()     # 调试
    current_app.logger.error("error info")
    current_app.logger.warn("error info")
    current_app.logger.info("error info")
    current_app.logger.debug("error info")
    return "index page"