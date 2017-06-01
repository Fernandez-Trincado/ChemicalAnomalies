Searching for Chemical Anomalies in APOGEE-2
====

** Author(s) ** 

J. G. Fernandez-Trincado, and APOGEE-2 Team

Contact: - jfernandezt@astro-udec.cl and/or jfernandezt87@gmail.com

   **Paper 1: "Atypical Mg-poor Milky Way field stars with second-generation like chemical patters"**
---

This repository is for the public version of the APOGEE red giant catalog containing a subsample of chemically anomalous targets. The catalog is assocated with this paper, and all our spectra can be download at [SDSS Science Archive Server (SAS)](https://dr13.sdss.org/home) 

**Status:** Submitted to ApJL

**Description:**

[MgAlredgiants.fits](https://dr13.sdss.org/home) This is a catalog of 4611 red giant stars that have metallicities in the range -1.8 < [Fe/H] < -0.7 and signal-to-noise SNR > 70 from the SDSS APOGEE ASPCAP pipeline (discussed in this paper). Our potential chemically anomalous stars are selected based on k-means clustering. Then please pay attention to the flags included in the latest column indicating our three main clustering, and tagged as:

  * `disk stars candidates:` Clusteringflag==0
  * `second generation candidates:` Clusteringflag==1
  * `halo stars:` Clusteringflag==2.


![k-means](https://github.com/Fernandez-Trincado/ChemicalAnomalies/blob/master/clustering.pdf)






