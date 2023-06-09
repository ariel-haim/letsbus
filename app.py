from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
db = SQLAlchemy(app)


class Reports(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    timeOfReport = db.Column(db.String)
    typeOfReport = db.Column(db.String)
    stationOfReport = db.Column(db.Integer)
    lineOfReport = db.Column(Integer)
    directionOfLine = db.Column(String)

@app.route('/api/data', methods=['GET'])
def get_data():
    rows = Reports.query.all()
    data = []
    for row in rows:
        data.append({
            'id': row.id,
            'timeOfReport': row.timeOfReport,
            'typeOfReport': row.typeOfReport,
            'stationOfReport': row.stationOfReport,
            'lineOfReport': row.lineOfReport,
            'directionOfLine': row.directionOfLine
        })
    return jsonify(data)


@app.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    row = YourModel.query.get(id)
    if not row:
        return jsonify({'message': 'Row not found'}), 404

    data = request.get_json()
    row.field1 = data['field1']
    row.field2 = data['field2']
    db.session.commit()

    return jsonify({'message': 'Row updated successfully'}), 200

@app.route('/reports', methods=['POST'])
def newReport(typeOfReport, station, line, direction):
    # update Reports DB
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = Reports(timeOfReport=datetime, typeOfReport=typeOfReport, stationOfReport=station, lineOfReport=line,
                      directionOfLine=direction)
    session.add(new_row)
    session.commit()
    # update lineStop DB



if __name__ == '__main__':
    app.run()

