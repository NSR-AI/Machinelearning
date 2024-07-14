import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED=1234
num_samples=50
np.random.seed([SEED])

def generate_data(num_samples):
    X=np.array(range(num_samples))
    random_noise=np.random.uniform(-10,20,size=num_samples)
    y=3.5*X+random_noise
    return X,y

X,y=generate_data(num_samples=num_samples)
data=np.vstack([X,y]).T
print(data[:5])