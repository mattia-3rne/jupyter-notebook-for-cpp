from __future__ import annotations

import os
import subprocess
import sys
import tempfile


def run_cpp_source(source: str, std: str = "c++17", extra_flags: str = "") -> int:
    flags = ["-Wall", "-Wextra", f"-std={std}"]
    if extra_flags:
        flags.extend(extra_flags.split())

    with tempfile.TemporaryDirectory() as tmp:
        cpp_path = os.path.join(tmp, "main.cpp")
        exe_path = os.path.join(tmp, "main")
        with open(cpp_path, "w", encoding="utf-8") as handle:
            handle.write(source)

        compile_proc = subprocess.run(
            ["g++", *flags, cpp_path, "-o", exe_path],
            capture_output=True,
            text=True,
        )
        if compile_proc.returncode != 0:
            print(compile_proc.stderr or compile_proc.stdout, file=sys.stderr)
            return compile_proc.returncode

        run_proc = subprocess.run([exe_path], capture_output=True, text=True)
        if run_proc.stdout:
            print(run_proc.stdout, end="")
        if run_proc.stderr:
            print(run_proc.stderr, end="", file=sys.stderr)
        return run_proc.returncode


def cpp(line: str, cell: str) -> None:
    std = "c++17"
    extra = ""
    if line.strip():
        parts = line.strip().split()
        index = 0
        while index < len(parts):
            if parts[index] == "-std" and index + 1 < len(parts):
                std = parts[index + 1]
                index += 2
            else:
                extra += parts[index] + " "
                index += 1

    run_cpp_source(cell, std=std, extra_flags=extra.strip())


def load_cpp_magic() -> None:
    from IPython import get_ipython

    ip = get_ipython()
    if ip is None:
        raise RuntimeError("load_cpp_magic() must be called from Jupyter or IPython.")
    ip.register_magic_function(cpp, "cell", "cpp")
