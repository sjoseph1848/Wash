#pip install datascience
from datascience import *
import numpy as np

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

wash = Table.read_table('WashSale.csv')
print(wash)

#test
