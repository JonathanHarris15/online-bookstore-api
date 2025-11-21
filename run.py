from dotenv import load_dotenv
load_dotenv()

from app import create_app, db
from app.models import User, Book, Orders, OrderItems, Managers

app = create_app()

@app.cli.command('create-tables')
def create_tables():
    with app.app_context():
        db.create_all()
        print("Database tables created.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)