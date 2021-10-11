from projectweek_app.config.MySQLConnection import connectToMySQL
from projectweek_app import app 
from datetime import date, datetime
from flask import flash
import re

class Postu:
    