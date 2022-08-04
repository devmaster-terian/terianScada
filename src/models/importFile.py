import sys
from datetime import datetime
from email.policy import default
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, null
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def consola(pTexto):
    print (bcolors.WARNING + pTexto)
    sys.stdout.flush()


