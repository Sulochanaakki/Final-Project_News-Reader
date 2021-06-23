from app.config import app, db, ma

if __name__ == '__main__':

    db.init_app(app)
    ma.init_app(app)

    app.run(host='127.0.0.1', port='8080', debug=True)