from flask import Flask
from flask import request
from SeasonsCalc import Seasons_Calculation as sc
from RunWear import RunWear as rw
from LukasCal import LukasCal as lc
app = Flask(__name__)

# @app.route('/')
# def root_command():
#     cmd = ["/etc/init.d/cups", "start"]
#     p = Seasons_Calculation.Popen(cmd, stdout=Seasons_Calculation.PIPE, stderr=Seasons_Calculation.PIPE, stdin=Seasons_Calculation.PIPE)
#     out,err = p.communicate()
#     return out


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
    return lc.LukasCal()


@app.route('/test')
def test():
    return 'Server is reachable'


if __name__ == "__main__":
    app.run()

lukascal()