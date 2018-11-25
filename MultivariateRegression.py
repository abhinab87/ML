import pandas as pd
import numpy as np
import matplotlib as mb

if __name__ == "__main__":
    print("Hello Python")
    data = pd.read_csv("D:\\Big Data\\Project\\MultivariateRegresion\\USA_Housing.csv")
    data.head(4)
    ar = np.array(data('Avg. Area Income'))
    ar.take(10)
