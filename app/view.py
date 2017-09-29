from flask import render_template, request, jsonify # iimport from flask library
from flask_cors import cross_origin

from app import app # import from __init__.py

from app import controller # import from controller.py


@app.route('/')
def root():
    """Rendering index.html from folder 'templates'."""

    return render_template('index.html')

@app.route('/run')
@cross_origin()
def run_script():
    """Accepting CORS and rendering JSON response
    in format:
    data = {
        'name': '', <= Name that accepted from request
        'data': None, <= Data from the script
        'message': '' <= OK if everything is good, else Not found this function
    }

    """
    data = {
        'name': '',
        'data': None,
        'message': ''
    }
    script_name = request.args['script_name']
    data['name'] = script_name
    data_script = controller.run_script(script_name)
    if data_script:
        data['message'] = 'OK'
        data['data'] = data_script
    else:
        data['message'] = 'Not found this function'
    return jsonify(data)



