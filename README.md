# Conditional FIFO Profiles for Coordinated Repair in Time-Dependent Inventory Routing

Python code and experiment data for *Conditional FIFO Profiles for Coordinated
Repair in Time-Dependent Inventory Routing* by Gia Phong Ngo.

## Start here

Use Python 3.11–3.13 in a fresh virtual environment. Run from this folder:

    python -m pip install -r requirements.txt
    python main.py tests
    python main.py tables

The table command generates tables for the principal comparisons, robustness results,
sensitivity results and directed-probe counts from retained records. Output
goes to tables/ by default. Use --output to choose another destination.

With OpenSSL available on PATH, verify the 120 directed probes and 66
improving joint moves:

    python main.py probes

Use python main.py all to run all three checks. The runner unpacks the
source and retained records into a temporary directory and preserves the
historical paths required by the signed evidence. The pinned commit and the
instructions for a fresh coordination run are inside source.zip.

## Appendix inputs and results

The appendix-linux/ directory contains the saved Appendix cell results, plans,
summaries and environment records. Use compact-arc-linux-verified.json for
the merged compact-arc result. For the original Lyon-derived data, see the
[pinned benchmark repository](https://github.com/faycalt/TDIRP/tree/a65e097e652c046b27ac64f75cea0c1c7836eb74).
The original HGS distribution and benchmark archive are obtained separately.
See THIRD_PARTY.md.

## Additional material

Full historical logs, journals, native binaries and the complete Appendix run
bundles are outside this compact copy. For additional retained execution records
or experimental material, contact the corresponding author,
Gia Phong Ngo ([giaphong.ngo@outlook.com.vn](mailto:giaphong.ngo@outlook.com.vn)).
