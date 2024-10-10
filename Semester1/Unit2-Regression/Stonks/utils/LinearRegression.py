import pandas as pd
import matplotlib.pyplot as plt
class linearRegression:
    col1 = ""
    col2 = ""

    def __init__(self, data, col1, col2):
        self.col1 = col1
        self.col2 = col2

        m = 0
        b = 0
        L = 0.0001
        epochs = 300

        for i in range(epochs):
            if i % 50:
                print(f"Epoch: {i}")
            m,b = gradient_descent(m, b, data, L)

        print(m,b)

        x = merged_Df[[col1]].values
        y = merged_Df[col2].values

        plt.scatter(x, y,  color='black')
        plt.plot(list(range(len(data))), [m * x + b for x in range(len(data))], color='blue', linewidth=3)

    def loss_function(self, m, b, points):
        total_error = 0
        for i in range(len(points)):
            x = points.loc[i, col1]
            y = points.loc[i, col2]
            total_error += (y - (m * x + b)) ** 2
        total_error / float(len(points))

    def gradient_descent(self, m_now, b_now, points, L):
        m_gradient = 0
        b_gradient = 0

        n = len(points)

        for i in range(n):
            x = points.loc[i, col1]
            y = points.loc[i, col2]

            m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
            b_gradient += -(2/n) * (y - (m_now * x + b_now))

        m = m_now - m_gradient * L
        b = m_now - b_gradient * L

        return m, b