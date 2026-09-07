"""Run the remaining scene experiments, at most two model requests at once."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--scenes", nargs="+", type=int, default=[1, 2, 3, 5])
    parser.add_argument("--prompt-version", choices=["v1", "v2"], default="v1")
    parser.add_argument("--reasoning-effort", choices=["medium", "high"], default="medium")
    args = parser.parse_args()
    if len(set(args.scenes)) != len(args.scenes) or any(s not in range(1, 6) for s in args.scenes):
        parser.error("provide distinct scene numbers between 1 and 5")
    root = Path(__file__).resolve().parent

    def run(scene):
        command = [sys.executable, "-B", str(root / "run_experiment.py"), "--scene", str(scene), "--prompt-version", args.prompt_version, "--reasoning-effort", args.reasoning_effort]
        if args.render:
            command.append("--render")
        print(f"Scene {scene}: {'rendering' if args.render else 'preparing'}", flush=True)
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"Scene {scene}: {'complete' if result.returncode == 0 else 'FAILED'}", flush=True)
        if result.returncode:
            print((result.stderr or result.stdout)[-3000:], flush=True)
        return result.returncode

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = [future.result() for future in as_completed([pool.submit(run, s) for s in args.scenes])]
    return int(any(results))


if __name__ == "__main__":
    sys.exit(main())
