import numpy as np
import matplotlib.pyplot as plt

def check_if_inside_C1(x,y):
    return 1 if((((x**2+y**2>0.6) and (x**2+y**2<0.8)) or ((x**2+y**2>0.35) and (x**2+y**2<0.5))) and (not((x>y) and (x>-y)))) else 0

def check_if_inside_C2(x,y):
    return 1 if((((x**2+y**2>0.6) and (x**2+y**2<0.8)) or ((x**2+y**2>0.35) and (x**2+y**2<0.5))) and (not((x>y) and (x>-y)))) else 0

def sample_letter_C(nsteps=5000):
    ret_x, ret_y, ret_col, ret_alpha = np.zeros(0), np.zeros(0), np.zeros(0), np.zeros(0)
    for n in range(nsteps):
        _x, _y = np.random.rand(2)*4-1
        ret_x   = np.append(ret_x, _x)
        ret_y   = np.append(ret_y, _y)
        _col_alpha = ('fuchsia', 1) if (check_if_inside_C1(_x,_y) or check_if_inside_C2(_x-1.5,_y)) else ('gold', 0.15)
        ret_col, ret_alpha = np.append(ret_col, _col_alpha[0]), np.append(ret_alpha,  _col_alpha[1])
    return ret_x, ret_y, ret_col, ret_alpha

params_keynote = {
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": '#222222',
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": 'white',
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": '#222222',
    "figure.edgecolor": 'lightgray',
    "savefig.facecolor":'#222222',
    "savefig.edgecolor": 'lightgray'
    }

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update(params_keynote)

fig, ax = plt.subplots(1, 1, figsize=(8, 4), sharex=False, sharey=False)
x, y, _col, _alpha = sample_letter_C()
ax.scatter(x, y, color=_col, alpha=_alpha, label='All code is welcome')
ax.set_xlim((-1,3))
ax.set_ylim((-1,1))
plt.axis('off')
plt.legend(loc='center right', framealpha=0, labelcolor='fuchsia',prop=dict(weight='bold', size=15))
plt.show()