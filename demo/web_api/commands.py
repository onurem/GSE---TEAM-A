from sqlalchemy.orm.session import Session
from database import db

def create_db():
    """
        Migrate db
    """
    db.create_all()

def drop_db():
    """Cleans database"""
    db.drop_all()

def create_account_table():
    """
        Create `account` table
    """
    from account import Account
    Account.__table__.create(db.engine, checkfirst=True)

    sample_admin = Account('sample@company.com', 'abc123456', True)
    sample_user = Account('user@company2.com', 'abc123456')
    
    # Seeding mock data
    with Session(db.engine) as session:
        session.add(sample_admin)
        session.add(sample_user)
        session.commit()


def init_app(app):
    for cmd in [create_db, drop_db, create_account_table]:
        app.cli.add_command(app.cli.command()(cmd))