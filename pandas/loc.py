import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(10), index=pd.date_range("20180101", periods=10))
df.loc["01-01"]
