## Dataset name

PAUS

## Contact

David Navarro Gironés (david.navarro.girones@gmail.com)

## Input data used to make these measurements

PAUS master catalogue (https://cosmohub.pic.es/catalogs/319) to define the positions and the physical properties. Shapes from the CFHTLenS and KiDS catalogues.

## Reference publications and conditions of use

https://arxiv.org/abs/2505.15470

## Availability of input catalogues and measurement software

Include links where possible

## Sample selection

There are 20 subsamples with i_AB < 22. 10 correspond to red galaxies and 10 to blue galaxies. Inside each of them, the IA measurements are provided for:
- color-only split
- color and redshift (3 equip. bins) split
- color and luminosity (3 equip. bins) split
- color and stellar mass (3 equip. bins) split

The angular PAUS mask is applied to all the catalogues. The redshift range is 0.1 < zb < 1.0. A description of the different splits, with several defining properties can be found in Table 2 of https://arxiv.org/abs/2505.15470

If you can provide full distributions rather than just means, please add these to the repo as ancillatory data and briefly describe here.

## Shape information

Shape measurement in the r-band using the KSB algorithm, with corrections from Hoekstra et al. (1998). A description of the shape calibration is found in Section 2.3 of https://arxiv.org/abs/2505.15470


## Redshift information

Photometric redshifts using the BB (from CFHTLenS or KiDS, depending on the field) and the NB from PAUS. The paper describing the photo-z estimation used for this sample can be found in https://arxiv.org/abs/2312.07581


## Measurement details

- type of IA/clustering estimator: w\_gp, with Pi\_max = 233 Mpc/h
- binning details: 12 logarithmically-space angular bins (rp) between 0.1-18 Mpc/h and Pi binning following a Fibonacci sequence up to 233 Mpc/h.
- fiducial cosmology: Omega_c=0.25-0.044, Omega_b=0.044, h=0.69, sigma8 = 0.8, n_s=0.95
- H_0 convention: Mpc/h
- comoving coordinates
- random catalogues: Random sampling in the angular space, taking into account the mask. Smoothing in the radial distribution with a top-hat filter of 420Mpc/h.

## Covariances

Jacknife covariances with different number of patches depending on the case under study. The number of patches can be found in Table 2 of https://arxiv.org/abs/2505.15470

## Notes

The notation used to name the measurements is the following:
- color-only split -> 2pt_paus_{field}_{mag_lim}_{color}
- color and redshift (3 equip. bins) split -> 2pt_paus_{field}_{mag_lim}_{color}_zb_equip_3_bins_{bin_number}
- color and luminosity (3 equip. bins) split -> 2pt_paus_{field}_{mag_lim}_{color}_lum_r_bcnz_equip_3_bins_{bin_number}
- color and stellar mass (3 equip. bins) split -> 2pt_paus_{field}_{mag_lim}_{color}_stellar_mass_equip_3_bins_{bin_number}

where field = 'all_fields' (W1, G09 and W3), mag_lim = 'bright' (i_AB < 22), bin_number can be [0, 1, 2] depending on the equipopulated bin one choses (with 0 the bin within the lower part of the range and 2 the bin within the higher) and color is either 'red' or 'blue'.

**Add anything that might be relevant to the user**

Consider the following:
- missing data/information, caveats
- parts of the data that should not be (fully) trusted, e.g. covariance on large scales, or clustering on small scales
- independence/shared volume with other IA measurements
- ancillatory data useful for modelling the data, e.g. luminosity function slopes for magnification bias
- recommendations for use, e.g. scale cuts or signals to include
