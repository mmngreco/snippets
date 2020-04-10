# !pip install tqdm
from tqdm import tqdm
from time import sleep
it = [*range(10)]

for i in tqdm(it):
    print(i)
    sleep(0.2)


