import os

from flask import render_template, redirect, url_for, flash, request

from . import app
from .data import *


@app.route('/')
@app.route('/index')
def render_index_page():
    (portfolio_images, rows) = get_portfolio_images()
    return render_template('index.html', is_index=True, portfolio_images=portfolio_images, portfolio_rows=rows)

@app.route('/about')
def render_about_page():
    return render_template('about.html', is_about=True)

@app.route('/services')
def render_service_page():
    return render_template('services.html', is_services=True)

@app.route('/portfolio')
def render_portfolio_page():
    (portfolio_images, rows) = get_portfolio_images()
    return render_template('portfolio.html', is_portfolio=True, portfolio_images=portfolio_images, portfolio_rows=rows)

@app.route('/contact')
def render_contact_page():
    return render_template('contact.html', is_contact=True)
