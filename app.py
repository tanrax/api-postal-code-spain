# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from flask import Flask, request
from flask_cors import CORS
import pandas as pd

# =========================
# Extensions initialization
# =========================
app = Flask(__name__)
POSTALS = pd.read_csv('postal.csv', delimiter=',')

# =========================
# Configurations
# =========================
app.config['DEBUG'] = True if os.environ.get('DEBUG') == 'True' else False
PRE_URL = '/api/v1/'
CORS(app, resources={r"/api/*": {"origins": "*"}})

# =========================
# Routes
# =========================

# Get data from index
@app.route(PRE_URL + 'index/<int:id>')
def index(id):
    match = POSTALS.loc[[id]]
    results = match.filter(items=['postal_code', 'poblacion', 'lat', 'lng'])
    return results.reset_index().to_json(orient='records')


# Get data from postal code
@app.route(PRE_URL + 'postal_code/<int:code>')
def postal_code(code):
    match = POSTALS[POSTALS['postal_code'].isin([code])]
    results = match.filter(items=['postal_code', 'poblacion', 'lat', 'lng'])
    return results.reset_index().to_json(orient='records')



if __name__ == "__main__":
    app.run()
