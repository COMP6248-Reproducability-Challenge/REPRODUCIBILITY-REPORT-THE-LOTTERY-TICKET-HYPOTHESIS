import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from tqdm import tqdm
from glob import glob


DPI = 1200
prune_iterations = 35

lt_accr = glob('./logs/dumps/lt/fc1/mnist/lt_all_accuracy_*.dat')
re_accr = glob('./logs/dumps/lt/fc1/mnist/reinit_all_accuracy_*.dat')

_lt_accr = [path for path in lt_accr if '18.7' in path or '10.0' in path or '15.1' in path or '20.7' in path or '23.0' in path]
re_accr = [path for path in lt_accr if '100.0' in path]*5

a = np.arange(100)
press = ['10.0', '15.1', '18.7', '20.7', '23.0']
for i in range(len(re_accr)):
    l = np.load(_lt_accr[i], allow_pickle=True)
    r = np.load(re_accr[i], allow_pickle=True)

    plt.plot(l, c="blue", label="Winning tickets "+press[i])
    plt.plot(r, c="red", label="Winning tickets 100")
    plt.title('compression_'+lt_accr[i].split('_')[-1][:-4])
    plt.legend()
    plt.grid(color="gray")
    plt.savefig("logs/plots/lt/time_compare_100/{}.png".format('compression_'+_lt_accr[i].split('_')[-1][:-4]), dpi=DPI, bbox_inches='tight')
    plt.close()
print('-')