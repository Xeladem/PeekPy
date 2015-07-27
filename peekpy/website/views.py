# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

website = Blueprint('website', __name__)


#Register the main page
@website.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')