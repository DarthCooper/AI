import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
from enum import Enum

class KeyMethods:
    def getFiveData(dataFrame : pd.DataFrame(), key : str) -> dict:
        """
        dataFrame : the dataframe used to get the data. Works best when converted to a numeric value
        key : the key, aka. column, used to find the data.
        """
        summary = {
            "max": dataFrame[key].max(),
            "Q3" : dataFrame[key].quantile(0.75),
            "Median" : dataFrame[key].median(),
            "Q1" : dataFrame[key].quantile(0.25),
            "Min" : dataFrame[key].min(),
        }
        return summary
    
    def getMean(*args, **kwds) -> float:
        """
        args:
            dataFrame : the dataframe used to store the data
            column : the column where the data is stored
        """
        mean = 0
        if len(args) == 1 and isinstance(args[0], pd.DataFrame()):
            mean = args[0].mean()
        elif len(args) == 2 and isinstance(args[1], str):
            mean = args[0].loc[:, args[1]].mean()
        else:
            raise TypeError('Parameter 1 should be a dataFrame and parameter 2 should be a string or omitted entirely')
        return mean
    
    def getMedian(*args, **kwds) -> float:
        """
        args:
            dataFrame : the dataframe used to store the data
            column : the column where the data is stored
        """
        median = 0
        if len(args) == 1 and isinstance(args[0], pd.DataFrame()):
            median = args[0].median()
        elif len(args) == 2 and isinstance(args[1], str):
            median = args[0][args[1]].median()
        else:
            raise TypeError('Parameter 1 should be a dataFrame and parameter 2 should be a string or omitted entirely')
        return median
    
    def getStandardDeviation(*args, **kwds):
        """
        args:
            dataFrame : the dataframe used to store the data
            column : the column where the data is stored
        """
        deviation = 0
        if len(args) == 1 and isinstance(args[0], pd.DataFrame()):
            deviation = args[0].std()
        elif len(args) == 2 and isinstance(args[1], str):
            deviation = args[0][args[1]].std()
        else:
            raise TypeError('Parameter 1 should be a dataFrame and parameter 2 should be a string or omitted entirely')
        return deviation
    
    def getEmperical(*args, **kwds):
                """
        args:
            dataFrame : the dataframe used to store the data
            column : the column where the data is stored
        """
        #mean = getMean(args)
        #deviation = getStandardDeviation(args)
        #print(f"A majority of songs fall within:  {mean + deviation} and {mean-deviation}")
        
    def getZScore(*args, **kwds):
        zscores = 0
        if len(args) == 3 and isinstance(args[0], float):
            zscores = (args[0] - args[1]) / args[2]
        elif len(args) == 3 and isinstance(args[0], list):
            zscores = [(value - arsg[1]) / args[2] for value in args[0]]
        else:
            raise TypeError('Parameter 1 should be a float or an array of floats')
        return zscores
                            
    def OverlayHistograms(dataSets, x, bins, colors):
        for i in range(len(dataSets)):
            color = colors[i]
            sns.histplot(data = dataSets[i], x = x, bins = bins, color = color)
            
    def RemoveOutliers(dataSet, column : str):
        q_low = dataSet[column].quantile(0.01)
        q_hi  = dataSet[column].quantile(0.99)
        df_filtered = dataSet[(dataSet[column] < q_hi) & (dataSet[column] > q_low)]
        return df_filtered
    
    def calcCorr(df : pd.DataFrame, x : str, y : str, style : str):
        fixedX = KeyMethods.RemoveOutliers(df, x)
        fixedDF = KeyMethods.RemoveOutliers(fixedX, y)
        
        subDf = fixedDF[[x,y]]
        
        return subDf.corr(method = CorrMethods[style].value)
    
class CorrMethods(Enum):
    pearson = 'pearson'
    kendall = 'kendall'
    spearman = 'spearman'