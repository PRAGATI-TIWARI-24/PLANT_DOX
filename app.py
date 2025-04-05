from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

app = Flask(__name__)

# Function to process plant images
def process_image(image_path):
    image = cv2.imread(image_path)
    resized = cv2.resize(image, (500, 500))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5,5), 0)

    # Edge Detection (Canny)
    edges = cv2.Canny(blurred, 50, 150)

    return edges

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    file_path = "uploaded_leaf.jpg"
    file.save(file_path)

    processed_image = process_image(file_path)

    return jsonify({"message": "Image processed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

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
  return jsonify(PLANTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
