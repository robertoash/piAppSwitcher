from flask import Flask
from flask import request
from SeasonsCalc import Seasons_Calculation as sc
from RunWear import RunWear as rw
from LukasCal import Lukas_Cal as lc
from MovieFinder import Movie_Finder as mf
app = Flask(__name__)


@app.route('/season')
def season():
    return sc.S_Calc()
    # return sc.S_Calc.currs


@app.route('/runwearnow')
def wear_now():
    return rw.runwearnow()
    # return rw.runwearnow.phrase


@app.route('/runwearlater')
def wear_later():
    req_day = request.args.get('req_day')
    req_hour = request.args.get('req_hour')
    return rw.runwearlater(req_day, req_hour)
    # return rw.runwearlater.phrase


@app.route('/lukascal')
def lukascal():
    return lc.L_Cal()


@app.route('/moviefinder')
def moviefinder():
    movie = request.args.get('movie')
    return mf.MovieFinder(movie)


@app.route('/test')
def test():
    return 'Server is reachable'


if __name__ == "__main__":
    app.run()
