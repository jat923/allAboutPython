#scatter plot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams
name=r"cluster\spiral"
file=pd.read_csv(name+".csv")
data=file.to_numpy()
x=data[:,0]
y=data[:,1]
my_dpi=141
res=1024
#plt.figure(frameon=False,figsize=(res/my_dpi, res/my_dpi), dpi=my_dpi)
ax=plt.gca() #taking axis
ax.set_xlim([x.min()-0.2, x.max()+0.2])
ax.set_ylim([y.min()-0.2, y.max()+0.2])
#ax.set_aspect('equal', adjustable='box')
fig=plt.gcf()
ax.scatter(x,y,color='black')
fig.set_size_inches(24, 24.16)
#adding size let the image be square

#rcParams['figure.figsize'] =[res/my_dpi, res/my_dpi]
#rcParams['figure.dpi'] =my_dpi


ax.set_facecolor('white')
ax.axis('off')
'''
#The four border lines of the plot are called spines.by doing following all or either of them can be removed
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set(frame_on=False)
'''
#extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(name+".png",facecolor=ax.get_facecolor(), transparent=True,bbox_inches="tight")
#bbox_inches="tight" doesnt add padding
#savefig changes plot facecolor to none. so have to refer facecolor as ax.facecolor()