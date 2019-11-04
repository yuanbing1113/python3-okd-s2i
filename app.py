'''
Created on 04-Nov-2019

@author: yuanbing1113
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello, OKD World again! Uses S2I to build the application.'

if __name__ == '__main__':  # Script executed directly?
    print("Hello, OKD World. Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
