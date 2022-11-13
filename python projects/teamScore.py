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
from nba_api.stats.endpoints import leaguegamefinder, playbyplay, leaguegamelog,boxscoresummaryv2,boxscorematchups,playbyplayv2,boxscoretraditionalv2
from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba import endpoints
from nba_api.stats.static import teams, players
# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
Tdf = pd.DataFrame(nba_teams)
print("nba1")


from nba_api.stats.endpoints import leaguegamefinder, playbyplay, leaguegamelog,boxscoresummaryv2,boxscorematchups,playbyplayv2,boxscoretraditionalv2
from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba import endpoints
from nba_api.stats.static import teams

LGL = leaguegamelog.LeagueGameLog()
DFL = LGL.get_data_frames()[0]
gamefinder17 = leaguegamefinder.LeagueGameFinder(season_nullable='2017-18', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')
gamefinder19 = leaguegamefinder.LeagueGameFinder(season_nullable='2019-20', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')
gamefinder18 = leaguegamefinder.LeagueGameFinder(season_nullable='2018-19', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')
gamefinder20 = leaguegamefinder.LeagueGameFinder(season_nullable='2020-21', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')
gamefinder21 = leaguegamefinder.LeagueGameFinder(season_nullable='2021-22', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')

print("nba2")
gamesa = gamefinder18.get_data_frames()[0]
#gamesa1 = gamefinder18.get_data_frames()[0]
gamesb = gamefinder19.get_data_frames()[0]
gamesc = gamefinder20.get_data_frames()[0]
gamesd = gamefinder21.get_data_frames()[0]
gamese = gamefinder17.get_data_frames()[0]
#gamesf = gamefinder22.get_data_frames()[0]
DF = [gamesa,gamesb,gamesc,gamesd,DFL,gamese]
RST = pd.concat(DF)
print("nba3")

T1 = 'CHA'
DFS = RST[RST['TEAM_ABBREVIATION'].str.contains(T1)]
print(DFS['PTS'].mean())
print('===================================================')
#DFS.plot(x='GAME_DATE', y='PTS', kind='line')	
#plt.show()

TM = ['IND','DEN']

#for I in TM:
DFS = RST[RST['TEAM_ABBREVIATION'].str.contains('IND')]
DFID = RST[['GAME_ID','GAME_DATE','PTS']]
print(DFID)
data = []
for I in DFID['GAME_ID']:
    ID = I
    DSF = DFID[DFID['GAME_ID'] == I]
    Date = DFS['GAME_DATE'].values[0]
    Total = DFS['PTS'].values[0]

    BS = boxscoresummaryv2.BoxScoreSummaryV2(I)
    YS = BS.get_data_frames()[5]
    TDS = YS[YS['TEAM_ABBREVIATION']== T1]
    print(TDS)


df = pd.DataFrame(data, 'Game ID','Game Date','Abbr','QTR1','QTR2','QTR3','QTR4','Total' )
print(df)
print('===================================================')

