# encoding: utf-8
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, jsonify
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

