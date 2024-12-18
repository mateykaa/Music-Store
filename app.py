from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import db, Ensemble, Musician, Album
from datetime import datetime


def create_app():
    app = Flask(__name__)

    # Конфигурация подключения к PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:new_password@db:5432/mydatabase'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()
        # Регистрация маршрутов
    @app.route('/')
    def index():
        ensembles = Ensemble.query.all()
        return render_template('index.html', ensembles=ensembles)

    @app.route('/ensemble/<int:ensemble_id>/works_count')
    def works_count(ensemble_id):
        ensemble = Ensemble.query.get(ensemble_id)
        count = len(ensemble.albums)
        return f'Количество музыкальных произведений ансамбля {ensemble.name}: {count}'

    @app.route('/ensemble/<int:ensemble_id>/albums')
    def ensemble_albums(ensemble_id):
        ensemble = Ensemble.query.get(ensemble_id)
        return render_template('ensemble_albums.html', ensemble=ensemble)

    @app.route('/top_sellers')
    def top_sellers():
        current_year = datetime.now().year
        top_albums = Album.query.filter(Album.sales_current_year > 0).order_by(Album.sales_current_year.desc()).all()
        return render_template('top_sellers.html', top_albums=top_albums)

    @app.route('/add_album', methods=['POST'])
    def add_album():
        data = request.form
        new_album = Album(
            title=data['title'],
            release_date=datetime.strptime(data['release_date'], '%Y-%m-%d'),
            wholesale_price=float(data['wholesale_price']),
            retail_price=float(data['retail_price']),
            quantity_available=int(data['quantity_available'])
        )
        db.session.add(new_album)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/add_ensemble', methods=['POST'])
    def add_ensemble():
        data = request.form
        new_ensemble = Ensemble(name=data['name'])
        db.session.add(new_ensemble)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/check_db')
    def check_db():
        try:
            db.session.execute('SELECT 1')
            return "Database connection successful"
        except Exception as e:
            return f"Error: {str(e)}"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
