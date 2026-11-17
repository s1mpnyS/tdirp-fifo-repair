"""Check the implementation, generate result tables, or verify directed probes."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", choices=("tests", "tables", "probes", "all"))
    parser.add_argument("--output", type=Path, default=ROOT / "tables",
                        help="destination for regenerated tables")
    args = parser.parse_args()

    with TemporaryDirectory(prefix="tdirp-reproduction-") as directory:
        work = Path(directory)
        with ZipFile(ROOT / "source.zip") as source:
            source.extractall(work)
        snapshot = work / "frozen_snapshot"
        if args.task in ("tests", "all"):
            subprocess.run([sys.executable, "-B", "-m", "unittest", "discover",
                            "-s", "code/tests", "-p", "test_v11_fifo_control.py"],
                           cwd=snapshot, check=True)
        if args.task in ("tables", "all"):
            replay = work / "table-replay"
            display = replay / "display"
            display.mkdir()
            for script in ("rebuild_main_comparisons.py",
                           "rebuild_robustness_and_sensitivity.py"):
                subprocess.run([sys.executable, "-B", script], cwd=replay, check=True)
            shutil.copytree(display, args.output, dirs_exist_ok=True)
            print(f"Regenerated tables: {args.output.resolve()}", flush=True)
        if args.task in ("probes", "all"):
            subprocess.run([sys.executable, "-B", "code/reviewer_probe_evidence.py",
                            "verify", str(ROOT / "directed-probe-evidence.zip")],
                           cwd=snapshot, check=True)


if __name__ == "__main__":
    main()
