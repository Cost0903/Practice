import pandas as pd

arch = pd.read_html('https://zh.wikipedia.org/zh-tw/Arch_Linux')
print(len(arch))
print(arch)