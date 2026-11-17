# External material and provenance

## Benchmark data

The benchmark archive comes from the [TDIRP repository](https://github.com/faycalt/TDIRP/blob/a65e097e652c046b27ac64f75cea0c1c7836eb74/Benchmark.zip). The archived benchmark SHA-256 is:

`90f4b2e5705f43d1a1b2a574ea2f2ac35c443c04fedff8ebf77ac6fecb0e093c`

The benchmark archive is distributed separately. This repository does not grant rights to external benchmark data.

## Optional HGS integration

The upstream [HGS-IRP implementation](https://github.com/vidalt/HGS-IRP) was inspected at commit `61af0f43166719322f41916c36967bdeef01990c`. Its source header restricts use without explicit permission from its authors; a repository-wide redistribution license was not identified in the inspected version. Consequently, this package does not vendor upstream C++ source, patches containing upstream source, or native executables. Optional integration requires an independently obtained and appropriately authorized external installation.

The retained HGS comparison concerns a source-adapted static planning pipeline followed by evaluation/repair under the original FIFO model. It must be described with that scope, rather than as a reproduction of a published time-dependent HGS result. The optional runner must fail explicitly when its required external installation is unavailable.


## Python dependencies

NumPy and SciPy are installed through the root requirements.txt. Their licenses and the licenses of their bundled numerical components remain applicable.
