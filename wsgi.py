#  As a shortcut, if the file is named app.py or wsgi.py, you don’t
#  have to set the FLASK_APP environment variable.
#  See Command Line Interface for more details.
#
#  Otherwise, if for example have hello.py:
#
#  $ export FLASK_APP=hello
#  $ flask run
#  * Running on http://127.0.0.1:5000/
#
#  This tells your operating system to listen on all public IPs
#
#  $ flask run --host=0.0.0.0


from src.api import app


if __name__ == "__main__":
    app.run()
