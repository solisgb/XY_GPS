# -*- coding: Latin-1 -*-
"""
Created on Sun Mar 25 17:58:36 2018

@author: solis

"""

import XY_GPS_parameters as par


def get_data():
    """
    retrieve data from DB
    """
    from os.path import join
    import pyodbc
    from db_con_str import con_str
    import mpl

    cstr = con_str(par.DB)
    con = pyodbc.connect(cstr)
    cur = con.cursor()
    cur.execute(par.S_IDS)
    ids = [[row.ID, row.X, row.Y] for row in cur]

    ylabel = 'Z (m)'
    for id1 in ids:
        cur.execute(par.S_D, id1[0])
        gpsd = [[row.ID, row.FECHA, row.Z] for row in cur]
        if len(gpsd) < 2:
            continue
        print(id1[0])
        xa = [row[1] for row in gpsd]
        ya = [row[2] for row in gpsd]
        stitle = 'Evolucion de Z en punto GPS {0:d}'.format(id1[0])
        namef = 'GPS_{0:03d}'.format(id1[0])
        dst = join(par.DIR_OUT, namef)
        XYt_1(xa, ya, stitle, ylabel, dst)

        break

    cur.close()
    con.close()


def XYt_1(xdate, y, stitle, ylabel, dst):
    """
    XY x datetime serie, y serie
    """

#    import datetime
#    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    dateFmt = mdates.DateFormatter('%m/%Y')

    fig, ax = plt.subplots()
    ax.plot(xdate, y)

    plt.grid(True)
    plt.ylabel(ylabel)

    # rotate and align the tick labels so they look better
    fig.autofmt_xdate()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # use a more precise date string for the x axis locations in the
    # toolbar
    ax.xaxis.set_major_formatter(dateFmt)
    ax.set_title(stitle)

    plt.tight_layout()
    fig.savefig(dst)
    plt.close('all')


def XYt_3(xdate, y1, y2, stitle, ylabel1, ylabel2, dst):
    """
    XY x datetime serie, y serie
    """

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    dateFmt = mdates.DateFormatter('%m/%Y')

    fig, ax = plt.subplots()
    ax.plot(xdate, y)

    plt.grid(True)
    plt.ylabel(ylabel)

    # rotate and align the tick labels so they look better
    fig.autofmt_xdate()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # use a more precise date string for the x axis locations in the
    # toolbar
    ax.xaxis.set_major_formatter(dateFmt)
    ax.set_title(stitle)

    plt.tight_layout()
    fig.savefig(dst)
    plt.close('all')
