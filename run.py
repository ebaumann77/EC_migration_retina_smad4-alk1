import sys
from skimage import io
import pandas as pd
import time

sys.path.append("src/")
import functions
import plotResults

#======================================================================================================================
#=                                            STEP 1: COMPUTE ALL RESULTS                                             =
#======================================================================================================================

print('Computing results...')
functions.compute_res(parameters, key_file)
print('Finished computing.')


