
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
#import nflfastpy as NFP

Year=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]

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


gamesa = gamefinder18.get_data_frames()[0]
gamesb = gamefinder19.get_data_frames()[0]
gamesc = gamefinder20.get_data_frames()[0]
gamesd = gamefinder21.get_data_frames()[0]
gamese = gamefinder17.get_data_frames()[0]
#gamesf = gamefinder22.get_data_frames()[0]
DF = [gamesa,gamesb,gamesc,gamesd,DFL,gamese]
RST = pd.concat(DF)


#CLE
#LAL
print("nba2")
#TOR CHI
T1 = 'WAS'
T2 = 'CHA'

DFS = RST[RST['MATCHUP'].str.contains(T1)]
DFA = DFS[DFS['MATCHUP'].str.contains(T2)]
DFA
DFR = DFA[DFA['GAME_ID'] == '0021801212']
#print(DFR['PTS'].sum())
RS = RST[RST['TEAM_ABBREVIATION'] == T1]
R = RS['GAME_ID']
DFA




data = []
print("nba3")
for I in R:
    hs = DFA[DFA['GAME_ID'] == I]
    X,Y = hs.shape
    #print(RST)
    if X != 0:
        TOTAL = hs['PTS'].sum()
        DATE = hs['GAME_DATE'].values[0]
        hsa = hs[hs['TEAM_ABBREVIATION'] == T1]
        hsb = hs[hs['TEAM_ABBREVIATION'] ==  T2]
        T1PTS = hsa['PTS'].values[0]
        T2PTS = hsb['PTS'].values[0]
        points = ['PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4']
        
        BS = boxscoresummaryv2.BoxScoreSummaryV2(I)
        YS = BS.get_data_frames()[5]
        T1DS = YS[YS['TEAM_ABBREVIATION']== T1]
        T2DS = YS[YS['TEAM_ABBREVIATION']== T2]
        T1Q1 = T1DS['PTS_QTR1'].values[0]
        T1Q2 = T1DS['PTS_QTR2'].values[0]
        T1Q3 = T1DS['PTS_QTR3'].values[0]
        T1Q4 = T1DS['PTS_QTR4'].values[0]
        
        T2Q1 = T2DS['PTS_QTR1'].values[0]
        T2Q2 = T2DS['PTS_QTR2'].values[0]
        T2Q3 = T2DS['PTS_QTR3'].values[0]
        T2Q4 = T2DS['PTS_QTR4'].values[0]

        Gdata = [I,DATE,T1,T2,T1PTS,T2PTS,T1Q1,T1Q2,T1Q3,T1Q4,T2Q1,T2Q2,T2Q3,T2Q4,TOTAL]
        data.append(Gdata)
df = pd.DataFrame(data, columns=['GameID','Game_Date','T1', 'T2','T1Score','T2Score','T1Q1','T1Q2','T1Q3','T1Q4','T2Q1','T2Q2','T2Q3','T2Q4','Total'])
print("nba4")
DFJ = df.sort_values('Game_Date')
print(DFJ['Total'].mean())
DFJ

xsize,yszie = DFJ.shape
TT = DFJ['Total'].sum()
P = TT/220
print(TT,P)
#DFJ.groupby(['T1','T2']).mean()
T = DFJ.groupby(['T1','T2']).mean()
print(gamesf.head())

