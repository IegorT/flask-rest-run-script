from flask import render_template, request, jsonify # iimport from flask library

from app import app # import from __init__.py

from app import controller # import from controller.py


@app.route('/')
def root():
    """Rendering index.html from folder 'templates'."""

    return render_template('index.html')

@app.route('/run')
def run_script():
    """Accepting AJAX request and rendering JSON response
    in format:
    data = {
        'name': '', <= Name that accepted from request
        'data': None, <= Data from the script
        'status': '', <= Status if the script is finding 200 else 400
        'message': '' <= OK if everything is good, else Not found this function
    }

    """
    data = {
        'name': '',
        'data': None,
        'status': '',
        'message': ''
    }
    script_name = request.args['script_name']
    data['name'] = script_name
    data_script = controller.run_script(script_name)
    if data_script:
        data['status'] = 200
        data['message'] = 'OK'
        data['data'] = data_script
    else:
        data['status'] = 400
        data['message'] = 'Not found this function'
    return jsonify(data)



