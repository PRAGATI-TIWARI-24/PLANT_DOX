from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "plantdox"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# WTForms Form
class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[DataRequired()])
    submit = SubmitField('Upload')

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Index page with upload form
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    uploaded_img = session.get('uploaded_img')

    if form.validate_on_submit():
        file = form.photo.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            session['uploaded_img'] = filename
            flash('Image uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid file type.', 'danger')

    return render_template('index.html', form=form, uploaded_image=uploaded_img)

# Check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
