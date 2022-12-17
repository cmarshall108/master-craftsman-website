import os

from flask import render_template, redirect, url_for, flash, request

from . import app


@app.route('/')
@app.route('/index')
def render_index_page():
    return render_template('index.html', is_index=True)

@app.route('/about')
def render_about_page():
    return render_template('about.html', is_about=True)

@app.route('/services')
def render_service_page():
    return render_template('services.html', is_services=True)

@app.route('/portfolio')
def render_portfolio_page():
    return render_template('portfolio.html', is_portfolio=True)

@app.route('/contact')
def render_contact_page():
    return render_template('contact.html', is_contact=True)
