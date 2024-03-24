from flask import Flask, render_template
from models import storage
app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    states = storage.all("State").values()
    return render_template('9-states.html', states=states, id=None)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    states = storage.all("State")
    key = "State." + id
    if key in states:
        state = states[key]
    else:
        state = None
    return render_template('9-states.html', states=states, id=id, state=state)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
