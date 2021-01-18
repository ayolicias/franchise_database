from flask import Flask, render_template, jsonify, url_for, flash, request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import json

app = Flask(__name__)
app.secret_key = '99d0*93/>-23@#'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:demo@localhost/franchises'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Province = Base.classes.Provinces
Franchise = Base.classes.Franchises

def as_dict(row):
    data = vars(row)
    del data['_sa_instance_state']
    return data

def ramp(row):
    raw = None
    if len(row) == 1:
        raw = vars(row[0])
    else:
        raw = vars(row)
    data = raw
    del data['_sa_instance_state']
    return data

@app.route("/", methods=['GET'])
def index():
    return render_template("dashboard/index.html")


@app.route("/dashboard/metrics", methods=['GET'])
def dashboard_metric():
    data = db.session.query(province).all()
    return jsonify({'raw': data})


@app.route("/franchises", methods=['GET'])
def franchises_index():
    return render_template("franchises/home.html")


@app.route("/franchises/entry", methods=['GET'])
def franchises_add():
    return render_template("franchises/entry.html")


@app.route("/franchises/delete", methods=['POST'])
def franchises_del():
    return "Franchise Delete"


@app.route("/franchises/add", methods=['POST'])
def franchises_edit():
    return "Franchises Edit"


@app.route("/franchises/all", methods=['GET', 'POST'])
def franchises_all():
    data = db.session.query(franchises).all()
    raw = ramp(data)
    return json.dumps([raw])


@app.route("/provinces", methods=['GET'])
def provinces_index():
    return render_template("provinces/home.html")


@app.route("/provinces/entry", methods=['GET'])
def provinces_add():
    return render_template("provinces/entry.html")


@app.route('/provinces/add', methods=['POST'])
def provinces_insert():
    try:
        data = request.args.get('proname')
        rmks = request.args.get('prodesc')
        print(data)
        print(rmks)
        print(request.args.get('proname'))
        if len(data) == 0:
            # Check if no data was passed to the methods
            flash('Oops! No values were specified')
        else:
            count = db.session.query(province).filter_by(pro_name == data).first()
            if count == 0:
                # When all data has been specified save it into the database
                new_province = province(pro_name=data, remarks=rmks)
                db.session.add(new_province)
                db.session.commit()
                flash('Done! Province saved successfully!')
            else:
                flash('Oops! Province record already exist')
    except Exception as ex:
        # Show Error when all criteria are not met
        flash('Error! Failed to record province info')
    return render_template("provinces/entry.html")


@app.route("/provinces/delete", methods=['POST'])
def provinces_del():
    return "Provinces Delete"


@app.route("/provinces/all", methods=['GET'])
def Provinces_all():
    data = db.session.query(Provinces).all()
    data = ramp(data)
    return jsonify({'data': data})

if __name__ == "__main__":
    app.run(debug=True)