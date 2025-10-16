#!/usr/bin/env python3

import glob
import os
import shutil
import subprocess
import sys


def package() -> str:
    shutil.rmtree("dist", ignore_errors=True)
    subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"], check=True)
    wheels = glob.glob("dist/*.whl")
    if len(wheels) != 1:
        sys.exit(f"Expected to find 1 wheel generated under dist/ but found {len(wheels)}")
    return wheels[0]


def repair(wheel: str) -> None:
    auditwheel_cmd = ["auditwheel", "repair", "-w", "dist", wheel]
    docker = shutil.which("docker")
    if docker:
        subprocess.run(
            [
                docker,
                "run",
                "-u",
                f"{os.getuid()}:{os.getgid()}",
                "-v",
                f"{os.getcwd()}:/io",
                "-w",
                "/io",
                "quay.io/pypa/manylinux1_x86_64",
                *auditwheel_cmd
            ],
            check=True
        )
    else:
        subprocess.run([sys.executable, "-m", *auditwheel_cmd], check=True)
    os.unlink(wheel)


def main() -> None:
    wheel = package()
    if sys.platform == "linux":
        repair(wheel)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

