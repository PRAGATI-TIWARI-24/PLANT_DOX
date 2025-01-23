from flask import Flask, render_template, jsonify 

app = Flask(__name__)

PLANTS=[

  {
    'id': 1,
    'title': 'lotus',
    'breed': 'Nelumbo lutea',
    'disease': 'Leaf Spot Disease',
  },
  
  {
    'id': 2,
    'title': 'rose',
    'breed': 'Mr. Lincoln',
    'disease': 'Black Spot',
  },
  {
    'id': 3,
    'title': 'sunflower',
    'breed': 'Mammoth',
    'disease': 'Downy Mildew',
  },
  {
    'id': 4,
    'title': 'daisy',
    'breed': 'Shasta Daisy',
    'disease': 'Powdery Mildew',
  },
]

@app.route("/")
def hello_plants():
  return render_template('home.html', plants=PLANTS, plant_name='PLANT')

@app.route("/api/plants")
def list_plants():
  return jsonify(plants)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)