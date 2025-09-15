# IAmeasurementsStore

This repository stores intrinsic alignment (IA) measurements in units of **Mpc/h**.  
It also contains utilities for reading and processing the data.

---

## Dataset Details

- **Units**: Mpc/h  
- **π<sub>max</sub>**: 100 Mpc/h  
- **Redshift**: 0  
- **Cosmology**: D3A cosmology (see [FLAMINGO simulations](https://flamingo.strw.leidenuniv.nl/simulations.html))  

The corresponding power spectrum can be downloaded from the FLAMINGO project:  
➡️ [Power spectra (L2p8_m9)](https://flamingo.strw.leidenuniv.nl/power_spectra.html)

---

## Code

### `read_flamingo.py`
This script demonstrates how to:

- Read **w<sub>gg</sub>** and **w<sub>gp</sub>** along with their **r<sub>p</sub>** values.  
- Extract **ξ<sub>+</sub>** (*xip*) for each jackknife region.  
- Compute the **joint covariance matrix** from jackknife samples.  

---

## Usage

1. Clone this repository:
   ```bash
   git clone git@github.com:echo-IA/IAmeasurementsStore.git
   cd IAmeasurementsStore
