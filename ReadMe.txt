For better organizing the main part of Flask application were splitted into 3 parts: view,
controllers and scripts that need to run. All of this parts present in app folder.
view.py - for rendering html-file, accepting requests and rendering response(in JSON format)
controller.py - for finding and calling scripts
scripts - the folder for script



The server start => "python run.py"

Examples:   GET http://127.0.0.1:5000/run?name=script_2&args=0,10,5&type=html
            POST { "name": "script_2", "args": "0,10,5", "type": "html"} http://127.0.0.1:5000/run


