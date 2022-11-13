TDS = YS[YS['TEAM_ABBREVIATION']== 'IND']
    #print(YS)
    TQ1 = TDS['PTS_QTR1'].value
    print(TQ1)
    TQ2 = TDS['PTS_QTR2'].values[0]
    TQ3 = TDS['PTS_QTR3'].values[0]
    TQ4 = TDS['PTS_QTR4'].values[0]
    Gdata = [I,Date,T1,TQ1,TQ2,TQ3,TQ4,Total]
    data.append(Gdata)

print('===================================================')