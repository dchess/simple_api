from flask import Flask, jsonify, render_template
from sqlsorcery import MSSQL
import pandas as pd

app = Flask(__name__)
db = MSSQL()


@app.route("/api")
def index():
    tables = db.engine.table_names(schema=db.schema)
    return render_template("index.html", tables=tables)


@app.route("/api/<table>", methods=["GET"])
def endpoint(table):
    data = pd.read_sql_table(table, con=db.engine, schema=db.schema)
    data = data.to_dict(orient="records")
    return jsonify(data)
