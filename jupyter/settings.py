import pandas as pd
import numpy as np
import os
import logging


# suppress warnings
import warnings;
warnings.filterwarnings('ignore');

from tqdm.autonotebook import tqdm

# register `pandas.progress_apply` and `pandas.Series.map_apply` with `tqdm`
tqdm.pandas()

# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
# adjust pandas display
pd.options.display.max_columns = 30 # default 20
pd.options.display.max_rows = 200 # default 60
pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.precision = 2
pd.options.display.max_colwidth = 200 # default 50; None = all

# Number of array items in summary at beginning and end of each dimension
# np.set_printoptions(edgeitems=3) # default 3
np.set_printoptions(suppress=True) # no scientific notation for small numbers

# IPython (Jupyter) setting: 
# Print out every value instead of just "last_expr" (default)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import matplotlib as mpl
from matplotlib import pyplot as plt

# defaults: mpl.rcParamsDefault
rc_params = {'figure.figsize': (8, 4),
               'axes.labelsize': 'large', 
               'axes.titlesize': 'large',
               'xtick.labelsize': 'large',
               'ytick.labelsize': 'large',
               'savefig.dpi': 100,
               'figure.dpi': 100 }
# adjust matplotlib defaults
mpl.rcParams.update(rc_params)

import seaborn as sns
sns.set_style("darkgrid")
# sns.set()
