from flask import render_template, request, jsonify # iimport from flask library
from flask_cors import cross_origin

from app import app # import from __init__.py

from app import controller # import from controller.py


@app.route('/')
def root():
    """Rendering index.html from folder 'templates'."""

    return render_template('index.html')

@app.route('/run', methods=["GET", "POST"])
@cross_origin()
def run_script():
    """Accepting CORS and rendering JSON response
    in format:
    data = {
        'name': '', <= Name that accepted from request
        'data': None, <= Data from the script
        'message': '' <= OK if everything is good, else Not found this function
        'args': '' <= arguments of the running script
        'type': '' <= if html response type is will be html else json
    }
    """

    data = {
        'name': '',
        'data': None,
        'message': '',
        'args': None,
        'type': ''
    }
    if request.method == "POST":
        script = request.get_json()
    else:
        script = request.args
    print(script)
    data['name'] = script['name']
    if script['args'] != '':
        data['args'] = script['args'].split(",")
    data['type'] = script['type']
    print(data)
    data_script = controller.run_script(data['name'], data['args'])
    if data_script:
        data['message'] = 'OK'
        data['data'] = data_script
    else:
        data['message'] = 'Not found this function'
    if data['type'] == 'html':
        return """<div id="response">
                        <h1>The script name: {0}</h1>
                        <small>This script run with next args: {2}</small>
                        <p>Status: {3}</p>
                        <div style="color:green">{1}</div>
                    </div>""".format(data['name'], data['data'], ', '.join(data['args']), data['message'])
    return jsonify(data)



