from app import app, db

def run():
    db.create_all()
    print("Banco criado.")

if __name__ == '__main__':
    run()
    print("Pronto.")