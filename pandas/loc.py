import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(10), index=pd.date_range("20180101", periods=10, freq="H"))
df.loc["01:00:00"]
df
