"""Keep Cargo's exit status and surface test failures in the Actions summary."""
import subprocess
import sys

result = subprocess.run(
    ["cargo", "test", "--locked", "--all-targets"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
print(result.stdout, end="")
if result.returncode:
    tail = result.stdout[-12000:]
    escaped = tail.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error title=Rust test failure::{escaped}")
sys.exit(result.returncode)
