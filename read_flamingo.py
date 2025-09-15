import numpy as np
import pandas as pd
import h5py
from astropy.cosmology import FlatLambdaCDM
import pylevin as levin

import pylab as plt
# import emcee
from nautilus import Sampler, Prior  # <<< moved Prior import here
from multiprocessing import Pool
import argparse
import pyccl as ccl
import pyccl.nl_pt as pt
import scipy
import re
from scipy.interpolate import interp1d



min_rp_scale_Mpc_h_wgg = args.min_rp_scale_Mpc_h
min_rp_scale_Mpc_h_wgp = args.min_rp_scale_Mpc_h
max_rp_scale_Mpc_h_wgg = args.max_rp_scale_Mpc_h
max_rp_scale_Mpc_h_wgp = args.max_rp_scale_Mpc_h

# print(max_rp_scale_Mpc_h_wgg)

run = 'L2800N5040'  # or 'L1000N1800'

wgg_measured = pd.read_hdf(f'/disks/shear16/herle/correlations1/correlations_galaxy_{run}_HYDRO_FIDUCIAL_0.0.h5')[['wgg_rp', 'wgg_xip']]
wgp_measured = pd.read_hdf(f'/disks/shear16/herle/correlations1/correlations_galaxy_{run}_HYDRO_FIDUCIAL_0.0.h5')[['wgp_rp', 'wgp_xip']]


wgg_JK_measured = np.load(f'/disks/shear16/herle/correlations1/wgg_xip_jk_galaxy_{run}_HYDRO_FIDUCIAL_0.0.npy')
wgp_JK_measured = np.load(f'/disks/shear16/herle/correlations1/wgp_xip_jk_galaxy_{run}_HYDRO_FIDUCIAL_0.0.npy')

min_rp_scale_wgg = min_rp_scale_Mpc_h_wgg / y3fid.h
min_rp_scale_wgp = min_rp_scale_Mpc_h_wgp / y3fid.h
max_rp_scale_wgg = max_rp_scale_Mpc_h_wgg / y3fid.h
max_rp_scale_wgp = max_rp_scale_Mpc_h_wgp / y3fid.h

wgg_rp = wgg_measured["wgg_rp"].values / y3fid.h
wgp_rp = wgp_measured["wgp_rp"].values / y3fid.h

mask_wgg = (wgg_rp >= min_rp_scale_wgg) & (wgg_rp <= max_rp_scale_wgg)
mask_wgp = (wgp_rp >= min_rp_scale_wgp) & (wgp_rp <= max_rp_scale_wgp)

wgg_measured = wgg_measured[mask_wgg].reset_index(drop=True)
wgp_measured = wgp_measured[mask_wgp].reset_index(drop=True)

wgg_rp_cut = wgg_rp[mask_wgg]
wgp_rp_cut = wgp_rp[mask_wgp]

wgg_JK_measured = wgg_JK_measured[:, mask_wgg]
wgp_JK_measured = wgp_JK_measured[:, mask_wgp]

wgg_mean = np.mean(wgg_JK_measured, axis=0)
wgp_mean = np.mean(wgp_JK_measured, axis=0)

wgg_diff = pd.DataFrame(wgg_JK_measured - wgg_mean, columns=wgg_rp_cut)
wgp_diff = pd.DataFrame(wgp_JK_measured - wgp_mean, columns=wgp_rp_cut)

corr_diff = pd.concat([wgg_diff, wgp_diff], axis=1)
cov_mat = ((NPatches - 1) / NPatches) * np.sum(np.einsum('ij,ik->ijk', corr_diff, corr_diff), axis=0)
cov_mat = pd.DataFrame(data=cov_mat, columns=np.concatenate([wgg_rp_cut, wgp_rp_cut]))
cov_mat.set_index(np.concatenate([wgg_rp_cut, wgp_rp_cut]), inplace=True)


# Put back into a DataFrame with the same structure
cov_mat = pd.DataFrame(cov_mat, index=cov_mat.index, columns=cov_mat.columns)

cov_mat = cov_mat / (y3fid.h ** 2)
cov_arr = cov_mat.values  # <<< cache numeric array
inv_cov = np.linalg.pinv(cov_arr)  # <<< cache inverse once


wgg_measured["wgg_xip"] /= y3fid.h
wgp_measured["wgp_xip"] /= y3fid.h

corr = pd.concat([wgg_measured.wgg_xip, wgp_measured.wgp_xip]).to_numpy()  # <<< ensure ndarray
