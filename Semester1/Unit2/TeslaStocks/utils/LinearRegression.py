import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class linear_regression:
    def __init__(self, df, x_col, y_col):
        self.x_col = x_col
        self.y_col = y_col
        self.df = df
        self.slope, self.intercept = self.Calculate_LinearRegression()
        print(f"Slope: {self.slope}, Intercept: {self.intercept}")

        # Optional: Making predictions
        df['predictions'] = self.intercept + self.slope * self.df[self.x_col]

    def PlotGraph(self):
        sns.regplot(x=self.x_col, y=self.y_col, data=self.df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        
    def GetSlope(self) -> float:
        return self.slope
    
    def GetIntercept(self) -> float:
        return self.intercept
        
    def GetEquation(self) -> str:
        return f"Y = {self.slope}x + {self.intercept}"
        
    def Calculate_LinearRegression(self):
        # Extract x and y values
        x = self.df[self.x_col].values
        y = self.df[self.y_col].values
        N = len(x)

        # Calculate necessary sums
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum(x * y)
        sum_x_squared = np.sum(x ** 2)

        # Calculate slope (m) and intercept (b)
        m = (N * sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x ** 2)
        b = (sum_y - m * sum_x) / N

        return m, b
