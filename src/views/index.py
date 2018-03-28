# -*- coding: utf-8 -*-

import random
from flask import current_app as app
from flask import render_template


@app.route('/')
def hello_world():
    names = ["Danny", "Atila", "Julius", "Steffen"]
    return render_template('index.html', name=random.choice(names))
