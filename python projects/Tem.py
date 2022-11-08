import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import json
import requests
#from bs4 import BeautifulSoup
from pathlib import Path 
import pickle
import seaborn as sns 
import matplotlib.pyplot as plt 
#%matplotlib inline 
import category_encoders as ce
# scaling  
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import StandardScaler 
from datetime import date
# linear regression 
from sklearn import linear_model 
import numpy as np # linear algebra
from pandastable import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import nfl_data_py as nfl
import tkinter as tk
from pybaseball import *
from tkinter import ttk
from pybaseball import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pybaseball.lahman import *
import tksheet as Tsheet
import warnings
warnings.filterwarnings('ignore')
from PIL import ImageTk, Image
import nfl_data_py as nfl
from nba_api.stats.static import teams

print('===================================================')


# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
Tdf = pd.DataFrame(nba_teams)
print(Tdf)
print('===================================================')
