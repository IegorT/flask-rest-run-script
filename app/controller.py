# export all your scripts running function below
from app.scripts.script_1 import script_1
from app.scripts.script_2 import script_2

# add the name of request and the name of exporting function to the dictionary
scripts_dict = {
    'script_1': script_1,
    'script_2': script_2
}


def run_script(name=None, args=None):
    """Return the data from the running script if it is exists else None"""
    if name in scripts_dict and not args:
        return scripts_dict.get(name)()
    elif args:
        return scripts_dict.get(name)(args)
    return None


if __name__ == "__main__":
    # Here, usually, writing some test for checking if the this function running fell.
    # This part run only if you executing this script from the shell "python controller.py"
    print(run_script('script_1'))
    print(run_script('script_2', (0, 10, 5)))
