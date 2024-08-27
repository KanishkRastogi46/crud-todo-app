from webapp import create_app
from webapp import db


app = create_app()

if __name__=="__main__":
    app.run(debug=True)
    db.create_all()