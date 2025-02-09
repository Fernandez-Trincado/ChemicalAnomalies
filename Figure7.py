#!/usr/bin/python

import numpy as np 
import pylab as plt
import scipy as sc
import pyfits
from matplotlib.ticker import AutoMinorLocator
from scipy import stats
import scipy.stats

HP1    = pyfits.open('Table_Bacchus_abund_HP1.fits')
error  = pyfits.open('Table_error_Bacchus_abundances.fits') 


fig    = plt.figure(figsize=(17, 17))
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.1, top=0.92,hspace=0.25, wspace=0.35)

######################################################################################################################################################################
# Panel (a) ##################################
ax = plt.subplot(1,1,1)
######################################################################################################################################################################
ax.spines["bottom"].set_linewidth(3)
ax.spines["top"].set_linewidth(3)
ax.spines["left"].set_linewidth(3)
ax.spines["right"].set_linewidth(3)

plt.plot(HP1[1].data['CaFe'], HP1[1].data['AlFe'], 'o', mew=4, ms=30 , mec='black', color='cyan', zorder = 5000)
plt.errorbar(0.06, -0.1, xerr=error[1].data['eCaFe'], yerr=error[1].data['eAlFe'], color='black', capsize=10, mew=2, lw=2, zorder=1000, alpha=0.6)

ax.tick_params(which='both', direction='in',labelsize=35)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.tick_params(which='both', width=1.)
ax.tick_params(which='major', length=22)
ax.tick_params(which='minor', length=11)

plt.xlabel(r'[Ca/Fe]', fontsize=45)#, fontweight='bold')
plt.ylabel(r'[Al/Fe]', fontsize=45)#, fontweight='bold')
plt.xlim(-0.05, 0.5)
plt.ylim(-0.3, 1.1)

plt.savefig('Figure7.png')
