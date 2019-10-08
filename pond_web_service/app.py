import platform #to get system info
import lxml
import traceback
import urllib2 # to fetch data from url

from flask import Flask, jsonify, request
from lxml import html
from bs4 import BeautifulSoup # webscraping result

from PIL import Image


app = Flask(__name__)


@app.route('/ping')
def ping():
    try:
        return jsonify("pong!!!")
    except Exception as ex:
        return "Page Error!!!!", 400

@app.route('/system')
def get_system_info():
    try:
        context = dict()
        context['version'] = platform.version()
        context['plaform'] = platform.platform()
        context['system'] = platform.system()
        context['uname'] = platform.uname()
        context['processor'] = platform.processor()

        return jsonify(context)
    except Exception as ex:
        return "Page Error!!!!", 400

@app.route('/mediainfo/<image_id>', methods=['GET'])
def get_media_info(image_id):
    try:
        url = "https://www.pond5.com/photo/" + image_id
        page = urllib2.urlopen(url)
    
        page_data = BeautifulSoup(page)
        context = dict()
        context['title'] = page_data.img['alt']
        context['file_name'] = page_data.img['src'].split("/")[-1]
        return jsonify(context)
    
    except Exception as ex:
        return "Page Error!!!!", 400
        

if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)




