# run.py

from waitress import serve
from wsgimain import app

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
