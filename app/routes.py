from flask import Blueprint, jsonify
from .database import mysql

main = Blueprint('main', __name__)

@main.route('/events', methods=['GET'])
def get_events():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM eventos")
    rows = cur.fetchall()
    eventos = []
    for row in rows:
        eventos.append({
            'id': row[0],
            'nombre': row[1],
            'descripcion': row[2],
            'fecha': row[3].strftime('%Y-%m-%d'),
            'hora': str(row[4]),
            'lugar': row[5],
            'tipo_actividad': row[6]
        })
    return jsonify(eventos)
