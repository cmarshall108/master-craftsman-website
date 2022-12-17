import os

from flask import render_template, redirect, url_for, flash, request

from . import appvar


@appvar.route('/')
@appvar.route('/index')
def render_index_page():
    return render_template('index.html', is_index=True)

@appvar.route('/about')
def render_about_page():
    return render_template('about.html', is_about=True)

@appvar.route('/services')
def render_service_page():
    return render_template('services.html', is_services=True)

@appvar.route('/contact')
def render_contact_page():
    return render_template('contact.html', is_contact=True)
