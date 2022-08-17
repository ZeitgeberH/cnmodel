Forked version of CNModel by Manis & Capagnola
===============================================

CNModel is a Python-based (Python 3.6+) interface to NEURON models of cochlear nucleus neurons, synapses, network connectivity. To drive the model with sound stimuli, the Zilany et al (2010, 2014) auditory periphery model is used to generate auditory nerve spike trains (either via the "cochlea" Python package or by the original MATLAB model; see below). The overall goal is to provide a platform for modeling networks of cochlear nucleus neurons with different levels of biological realism in the context of an accurate simulation of auditory nerve input.

At the lowest level are NEURON-based implementations of ion channels and synapses. Ion channel models for potassium channels are derived largely from the measurements and models of Rothman and Manis (2003abc), and Kanold and Manis (1999, 2001); other channels are derived or modified from the literature. Cell models are in turn based on the insertion of ion channels in densities based on measurements in guinea pig and mouse. The "point" somatic cell models, which form the base set of models in CNModel, replicate the data reported in the original papers. 

The postsynaptic receptor/conductance models are based on kinetic models of glutamate (Raman and Trussell, 1992) and glycinergic receptors, as adjusted to match measurements of synaptic conductances from the mouse cochlear nucleus collected in Xie and Manis, 2013. The glutamate receptor models include desensitization and the effects of internal polyamine receptor block, based on the kinetic scheme of Woodhull (1982).

The presynaptic release model includes a multisite, probabilistic synapse that includes time-dependent changes in release probability based on the Dittman, Kreitzer and Regehr (J Neurosci. 2000 Feb 15;20(4):1374-85) kinetic scheme. Although detailed, this model is computationally expensive and likely not suitable for large scale network simulations. Other simpler models of synapses are also included.

Network connectivity may be defined programmatically, or based on a table of connectivity patterns. A table with estimates derived from the literature is included in the source. 

Included in this package is a set of test suites for different components. An overriding set of unit tests is available to confirm performance of the base models against a set of reference runs, several of which are in turn directly traceable to the original manuscripts. The test suites are useful in verifying performance of the model after modifications of the code or changes in the installation (upgrades of Python or Matlab, for example). 

A manuscript describing this package has been published:
--------------------------------------------------------

    Paul B. Manis, Luke Campagnola,
    A biophysical modelling platform of the cochlear nucleus and other auditory circuits: 
    From channels to networks,
    Hearing Research,
    Volume 360,
    2018,
    Pages 76-91,
    ISSN 0378-5955,
    https://doi.org/10.1016/j.heares.2017.12.017.
    Open Access: http://www.sciencedirect.com/science/article/pii/S037859551730360X

If you use this package, we would appreciate it if you cite our work in any publications or abstracts.

Issues
=========
Install `cochlea`_ from its github repo. The pip version is obsolete and will throw error related the numpy's fft function.

.. _`cochlea`: https://github.com/mrkrd/cochlea

Testing
==========
It is better to regenerate the test results rather than use the ones in the repo with which Pickle has some parse issues::

  $ python test.py --audit



Changes in this branch
========================
