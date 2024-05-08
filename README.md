# IAmeasurementsStore
Repo for IA measurements

This is a collection of summary statistics of past direct intrinsic
alignment measurements, generally using position-shape
correlation. Whenever possible these measurements will come with
accompanying clusterign measurements, covariances, and redshift
distributions, which will allow you to fit your favourite IA model to
the datasets.

When using a dataset, please cite the corresponding publications. If
this repo and its tools contributed to your work, please also
acknowledge the echoIA Collaboration. In the code/ directory you will
find an example notebook to read the fits format in which the data is stored.

When adding a new dataset (great!), please do the following:
1. create a new folder with an informative title describing your
   dataset;
2. use the Python notebooks in the code/ directory to convert your data
   into the standard fits format;
3. copy the template readme into your folder, replace 'template' by
   the name of you dataset folder, and enter as much metadata as
   possible, addressing all the prompts in the template.

