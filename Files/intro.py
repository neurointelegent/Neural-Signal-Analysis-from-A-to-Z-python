#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:15:58 2023

@author: ahmedshaheen
"""

#%% 
# import modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import plotly.express as px
import pandas as pd

import os
file_path = os.path.join("pytopo.py")
exec(open(file_path).read())
from pytopo import topoplotIndie

%matplotlib qt
#%% 

# load the EEG data
EEG = sio.loadmat('sampleEEGdata.mat')
#%% 
# explore a bit... what are the different fields? What is the size of the data?
# How many channels/time points/trials?
# What is the earliest and last time point?
# Where is time = 0?
# What is the sampling rate?

print(EEG.keys())

#%% 
# plot ERPs and topographical maps
# compute the ERP of each channel
# (remember that the ERP is the time-domain average across all trials at each time point)

erp = np.mean(EEG['EEG']['data'][0][0], axis=2)

# pick a channel and plot ERP
chan2plot = 'FCz'


plt.figure(1)
plt.plot(np.squeeze(EEG['EEG']['times'][0][0]), erp[np.where(np.concatenate(EEG['EEG']['chanlocs'][0][0]['labels'][0]) == chan2plot )[0][0],:], linewidth=2)
plt.xlabel('Time (ms)')
plt.ylabel('Activity (uV)')
plt.xlim([-400, 1200])


#%% 
chanlocs = EEG['EEG']['chanlocs'][0][0]
# convert time in ms to time in indices
tidx = np.argmin(np.abs(EEG['EEG']['times'][0][0] - time2plot))
time2plot = 300 # in ms


# plot topographical maps
topoplotIndie(erp[:,tidx],chanlocs,title='',ax=0)
plt.title('ERP from ' + str(time2plot) + ' ms')
plt.colorbar()


#%% 
# now for sample CSD V1 data
# load the data
v1 = sio.loadmat('v1_laminar.mat')

#%% 
# check out the variables in this mat file, using the function keys()
# If you don't know what variables are in this file vs. already in the workspace,
#  you can clear the workspace and then load the file in again.
# plot ERP from channel 7 in one line of code!

plt.figure(3)
plt.plot(np.squeeze(v1['timevec']), np.mean(v1['csd'][6,:,:], axis=1))
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.axvline(x=0.5, color='k', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Activity (uV)')
plt.xlim([-0.1, 1.4])

#%% 

# plot depth-by-time image of ERP
plt.figure(4)
plt.contourf(np.squeeze(v1['timevec']), np.arange(1,17), np.mean(v1['csd'], axis=2), 40, cmap='jet')
plt.xlim([0, 1.3])
plt.xlabel('Time (sec.)')
plt.ylabel('Cortical depth')
plt.show()

# done.