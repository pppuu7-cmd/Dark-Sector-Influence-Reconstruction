# Exp073EN attempts 1-2 — network SSL BLOCKED before resource/science stage

Date: 2026-09-06 Europe/Stockholm(+03 observed WSL clock).

Run `33993889263` used the prospectively preregistered Exp073EN file-backed WW_S0_S0 path. Hosted preflight succeeded. Home jobs `101380820499` and `101381512953` both terminated before disk gate, local stock-vs-patched qualifier, NaMaster build, R1 validation, or any full-resolution science arithmetic.

Both home attempts failed in the live-exclusivity infrastructure check because system Python 3.14 `urllib.request.urlopen()` received `ssl.SSLEOFError: UNEXPECTED_EOF_WHILE_READING` while contacting the GitHub Actions API. Attempt 2 additionally showed the GitHub runner itself transiently failing to resolve action download info because an SSL connection could not be established, after which the runner's own retry succeeded. These outcomes are network/infrastructure `+0/+0`; they are not resource failures, storage-qualification failures, numerical failures, or dark-sector science failures.

No Exp073EN evidence artifact was produced because failure occurred before any persistent evidence payload existed. No WW_S0_S0 authority was created.

Infrastructure repair v0.2 preserves the exact science contract and all frozen scientific component identities. It changes only the live-exclusivity transport: `ci/exp073en_live_exclusivity_curl_retry_v0_2.sh` uses `curl --retry 8 --retry-all-errors` to fetch Actions run/job JSON, then parses the downloaded JSON locally with Python. `ci/exp073en_home_filebacked_fullres_v0_2.sh` generates a temporary copy of the original v0.1 home script and replaces only the marker-delimited live-exclusivity block with the retry-safe helper. All code after `# Exact 8-CPU execution contract.` and all code before the original live-exclusivity block are inherited byte-for-byte from v0.1 at runtime.

Helper SHA256: `18da216f85d6a51eb08a4ef9e0ae18bc5e8d44995c3859d3162e59d611afeb8c`; Git blob `3bc8faf4bbb861961ce4cb27c25959100e82c501`.
Wrapper SHA256: `2f07add883c1a5b9ebe7becf5b18d61000e1d37cf662e3d40bfbb175ebed4351`; Git blob `ac4689c4b9b52451fd8eac3387b14029e67c1cdc`.

Next action: activate a new Exp073EN infrastructure attempt using the v0.2 wrapper. This remains the same preregistered science candidate; network retry does not change acceptance criteria or science accounting.
