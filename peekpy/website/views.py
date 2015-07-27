# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


website = Blueprint('website', __name__, url_prefix='/')


#Register the main page
@website.route('/', defaults={'page': 'index'})
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)