from collections import Counter
from pathlib import Path


p = Path("i.txt")
c = Counter(map(str.strip, p.open().readlines()))
c.most_common()
