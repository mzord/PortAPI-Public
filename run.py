from app import app
from app.db import db

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)