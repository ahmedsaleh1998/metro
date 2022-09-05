from tokenize import Name
from flask import Flask
from stations import main_route


app=Flask(__name__)

# @app.route('/metrostations/<source>/<destinamtion>')
@app.route('/<source>/<destination>/')
def Hello(source,destination):
    return main_route(source,destination)

if __name__ == "__main__":
  app.run(port=5000, debug=True)
