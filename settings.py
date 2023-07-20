
#----------------------GLOBAL ACROSS ALL MODULES-------------------------------#

#PACKAGES
from datetime import datetime

import yfinance as yf
import pandas as pd

#Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# PRINT SEPARATIONS
def print_break(message=''):
    print('')
    print("[_________________" + message + "_________________]")
    print('')


#----------------------GLOBAL ACROSS ALL MODULES-------------------------------#


if __name__ == '__main__':
    from os.path import expanduser
    import sys
    sys.path.append(expanduser("~") + "\Desktop")

    for item in sys.path:
        print(item)

