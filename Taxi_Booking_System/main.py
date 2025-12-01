# This Python file uses the following encoding: utf-8
from email.mime import application
import sys


if __name__ == "__main__":
    app = application(sys.argv)
    # ...
    sys.exit(app.exec())
