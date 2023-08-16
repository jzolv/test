from flask import *
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def uploadPage():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploadMethod():
    if request.method == 'POST':
        files = request.files.to_dict(flat=False)

        for f in files['file']:
            f.save('uploads/' + f.filename)

        return 'file uploaded successfully'


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()