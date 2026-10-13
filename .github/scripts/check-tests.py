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
    # GitHub truncates annotation messages; put assertion failures before logs.
    failure = result.stdout.split("\nfailures:\n", 1)
    tail = failure[1][:3000] if len(failure) == 2 else result.stdout[-3000:]
    escaped = tail.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error title=Rust test failure::{escaped}")
sys.exit(result.returncode)
