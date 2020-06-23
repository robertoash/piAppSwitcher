# Imports

from datetime import datetime
from SeasonsCalc.Brain import Get_SMHI_Data


def S_Calc():

    pasttemp = Get_SMHI_Data.temps

    # Preparation

    currentmonth = datetime.now().month
    results7 = []

    # Calculation

    for x in pasttemp:
        if x <= 0.0:
            results7.append("Winter")
        elif (x >= 10.0):
            results7.append("Summer")
        elif (x > 0.0) & (x < 10.0):
            if currentmonth <= 6:
                results7.append("Spring")
            else:
                results7.append("Fall")
        else:
            results7.append("Error")

    results5 = results7[2:5]

    if all(x == "Winter" for x in results5):
        currentseason = "Winter"
    elif all(x == "Spring" for x in results7):
        currentseason = "Spring"
    elif all(x == "Summer" for x in results5):
        currentseason = "Summer"
    elif all(x == "Fall" for x in results5):
        currentseason = "Fall"
    else:
        if currentmonth in [12, 1, 2]:
            currentseason = "Winter"
        elif currentmonth in [3, 4, 5]:
            currentseason = "Spring"
        elif currentmonth in [6, 7, 8]:
            currentseason = "Summer"
        else:
            currentseason = "Fall"

    # S_Calc.currs = currentseason

    try:
        with open("/var/www/piAppSwitcher/SeasonsCalc/SeasonResponses.txt", mode='a+') as txtfile:
            txtfile.write('On ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' SeasonsCalc sent response "' + currentseason + '".\n')
            txtfile.close()
    except IOError:
        print("Couldn't write to file!")

    return currentseason
