#!/usr/bin/env python

"""
[AppName]
By Joe Esposito

[Description]
"""

import os
from flask import Flask, render_template, url_for

def static(filename):
    """Provides the 'static' function that also appends the file's timestamp to the URL, usable in a template."""
    url = url_for('.static', filename=filename)
    fname = os.path.join(os.path.join(app.root_path, 'static'), filename)
    st = int(os.path.getmtime(fname))
    # time.strftime('%Y-%m-%d %H:%M', st)
    url += '?' + str(st)
    return url

# Flask application
app = Flask(__name__)
app.jinja_env.globals.update(static=static)

# Views
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

# Run dev server
if __name__ == '__main__':
    app.run('localhost', port=80, debug=True)
