#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os.path
import re
from glob import glob
import logging
import logging.config
from logging.handlers import RotatingFileHandler

from datetime import datetime, timedelta

from flask import Flask, render_template, make_response, send_from_directory, request, jsonify, redirect, session
# ~ from flask_session import Session
from flask_minify import minify
from flask_cors import cross_origin
from flask_babel import Babel, gettext, ngettext, force_locale, get_locale


# local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))
# from config.yaziji_config import webConfig
from config.yaziji_config import config_factory

import adaat
# ~ import data_const_arabic as data_const
from data import data_const




# set output logging in utf
import locale
if locale.getpreferredencoding().upper() != 'UTF-8': 
    locale.setlocale(locale.LC_ALL, 'ar_DZ.UTF-8')

# Configurate
mywebconfig = config_factory.facory()
#LOGGING_FILE = mywebconfig.logging_file
# URL_HOST_PATH = mywebconfig.url_host_path

if mywebconfig.MODE_DEBUG:
    # to rotate log 
    try:
        my_handler = RotatingFileHandler(mywebconfig.LOGGING_FILE, mode='a', maxBytes=5*1024*1024,
                                 backupCount=2, encoding=None, delay=0)
    except PermissionError:
        print(__file__, "You may verify the log file permissions")
    else:
        logging.basicConfig(level=logging.DEBUG, handlers=[my_handler]) 
    # ~ logging.basicConfig(filename=LOGGING_FILE, level=logging.DEBUG)
else:
    logging.basicConfig(filename=mywebconfig.LOGGING_FILE, level=logging.INFO)
#------------
# Configure App
#----------------

app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
)
minify(app=app, html=True, js=True, cssless=True)

# used to fix URL path for hosting
#app.config['URL_HOST_PATH'] = mywebconfig.url_host_path
app.config.from_object(mywebconfig)
# set default locale to arabic
# app.config["BABEL_DEFAULT_LOCALE"] = "ar"
# app.config["BABEL_TRANSLATION_DIRECTORIES"] = "locales;web/locales"
# app.config["BABEL_DOMAIN"] = "messages"
# app.config['BABEL_LANGUAGES'] = {'ar':"العربية",
# 'en':"English",
# "id":"Bahasa Indonesia",
# 'fr':"Français",
# 'bn':"বাংলা",
# 'es':"Español",
# 'ja':"日本語",
# 'zh':"中文",
# 'de':"Deutsche",
# "ku":"كوردى",
# }

# create a Bable instance for our app
babel = Babel(app)



def get_locale():
    # Extract language from URL path
    language = request.path.split('/')[1]
    if language in app.config['BABEL_LANGUAGES']:
        #print("user_language", language)        
        return language
    else:
        #print("default_language", app.config['BABEL_DEFAULT_LOCALE'])          
        return app.config['BABEL_DEFAULT_LOCALE']    
# ~ # sessions
# ~ app.config["SESSION_PERMANENT"] = False
# ~ app.config["SESSION_TYPE"] = "filesystem"
# ~ Session(app)

babel.init_app(app)
#babel.init_app(app, locale_selector=get_locale)


@app.route("/index/")
def index():
    return render_template("index.html",current_page='home')


@app.route("/")
@app.route("/<lang>/")
def home(lang="ar"):
    context = {}
    available_languages = app.config['BABEL_LANGUAGES']
    url_host_path = app.config['URL_HOST_PATH']
    with force_locale(lang):  # Set the locale to French
        return render_template("index.html", current_page='home',
                    available_languages=available_languages,
                    url_host_path = url_host_path,
        **context)





@app.route("/ajaxGet", methods=["POST", "GET"])
@app.route("/<lang>/ajaxGet", methods=["POST", "GET"])
@cross_origin()
def ajax(lang="ar"):
    default = ""
    resulttext = u"السلام عليكم"
    text = default
    action = ""
    options = {}
    if request.method == "GET":
        args = request.args
    elif request.method == "POST":
        args = request.get_json(silent=True)["data"]
    else:
        return jsonify({"text": default})
    # Request a random text
    if args.get("response_type", "") == "get_random_text":
        return jsonify({"text": default})

    text = args.get("text", "")
    action = args.get("action", "")
    options = dict(request.args)

    resulttext = adaat.DoAction(text, action, options)
    # ~ results = prepare_result(resulttext, text, action, options,"ajax")
    results = resulttext

    return jsonify({'result':resulttext, 'order':0})



    
    
@app.route("/selectGet", methods=["POST", "GET"])
@app.route("/<lang>/selectGet", methods=["POST", "GET"])
@cross_origin()
def selectget(lang="ar"):
    """
    this is an example of using ajax/json
    to test it visit http://localhost:8080/selectGet"
    """
    #-----------
    # prepare json
    #-------------
    #print("select get lang ", lang)
    with force_locale(lang): 
        return jsonify(data_const.selectValues)#,  default=json_default)


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)


@app.route("/doc/")
def doc():
    return render_template("doc.html",current_page='doc')


@app.route("/contact/")
def contact():
    return render_template("contact.html",current_page='contact')


@app.route("/download/")
def download():
    return render_template("download.html",current_page='download')


@app.route("/projects/")
def projects():
    context = {
        'libraries':qws_const.libraries,
        'websites':qws_const.websites
    }
    return render_template("projects.html",current_page='projects',**context)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.shtml')


@app.route('/<lang>/static', methods=['GET'])
def lang_static():
      return send_from_directory(app.static_folder, request.path[1:])


@app.route('/sitemap.txt', methods=['GET'])
def sitemap_txt():
      return send_from_directory(app.static_folder, request.path[1:])

@app.route('/sitemap.xml', methods=['GET'])
def sitemap_xml():
      return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)
