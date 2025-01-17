from flask import Flask, render_template, jsonify 

app = Flask(__name__)

plants=[

  {
    'id': 1,
    'title': 'plant 1',
    'breed':'breed 1',
    'disease': 'disease 1',
  },
  {
    'id': 2,
    'title': 'plant 2',
    'breed':'breed 2',
    'disease': 'disease 2',
  },
]

@app.route("/")
def hello_plants():
  return render_template('home.html', plants=plants, plant_name='plant')

@app.route("/api/plants")
def list_plants():
  return jsonify(plants)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)