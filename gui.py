import os
import smb_lock_manager

from flask import Flask, render_template, redirect, request, flash, url_for
from flask_table import Table, Col

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

class Conn():
    def __init__(self):
        self.host = os.environ['API_HOSTNAME']
        self.port = os.environ['API_PORT']
        self.user = os.environ['API_USER']
        self.passwd = os.environ['API_PASSWORD']

conn = Conn()
qslm = smb_lock_manager.QumuloConnections(conn)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
            if request.form.get("location"):
                qslm.close_location(request.form.get("location"))
                flash("Release Location: %s " % request.form.get("location"))
                return redirect(url_for('index'))
            else:
                flash("A POST without a location to release?")
    else:            
        locks = qslm.get_file_handles()
        return render_template('locks.html', locks=locks, conn=conn)

if __name__ == "__main__":
    app.run(debug=True)

