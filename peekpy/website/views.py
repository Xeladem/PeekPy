# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

website = Blueprint('website', __name__, url_prefix='/')


#Register the main page
@website.route('/', defaults={'page': 'index'})
def show_index(page):
    return render_template('%s.html' % page)