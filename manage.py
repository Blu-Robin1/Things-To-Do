from app import app
from db import db
from models import *
from datetime import datetime, timedelta
import sys

#Make the table
def create():
    db.create_all()
    
#Remove table
def drop():
    db.drop_all()

#Start session code
if __name__ == "__main__":
    with app.app_context():
        if len(sys.argv) > 0:
            for arg in sys.argv:
                match arg:
                    case "start":
                        drop()
                        create()
        