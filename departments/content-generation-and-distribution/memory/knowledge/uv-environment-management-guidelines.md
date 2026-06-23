---
title: Manage Python virtual environments with uv using precise environment targeting to avoid execution and installation failures
confidence: H
tag: self
created: 2026-06-16
source: 2026-06-16 session: installation errors due to unexpected '--venv' argument in uv pip install, and missing bin/pip under uv-managed virtual environment
---

When managing dependencies and python virtual environments using `uv` on macOS, standard pip patterns and virtual environment assumptions can break. Follow these guidelines to avoid installer and shell execution failures.

### Installation & Packaging Rules with `uv`
1. **No `--venv` in `uv pip install`**:
   - `uv pip install` does not accept a `--venv` argument. Attempting to run `uv pip install --venv <env> <package>` will fail with: `error: unexpected argument '--venv' found`.
2. **Missing `bin/pip` in Virtual Environments**:
   - Virtual environments created by `uv` may not contain `bin/pip` under their environment root (e.g., `tts_env/bin/pip` does not exist). Do not assume `pip` is available inside the venv's binary path.
3. **Correct Target Specification**:
   - To install a package into a specific virtual environment from outside, explicitly specify the python interpreter using the `--python` flag:
     ```bash
     uv pip install <package> --python <path_to_venv_python_binary>
     ```
     For example:
     ```bash
     uv pip install kokoro-onnx soundfile edge-tts faster-whisper --python tts_env/bin/python
     ```
   - Alternatively, activate the virtual environment first, then run `uv pip install`:
     ```bash
     source tts_env/bin/activate && uv pip install <package>
     ```

### Execution Rules
- Always execute python scripts using the exact virtualenv interpreter path rather than a global `python` command:
  ```bash
  ./tts_env/bin/python script.py
  ```
- This ensures clean execution and avoids library contamination from other environments or system Python.

<!-- backlinks:auto -->
## Backlinks

- [[local-audio-pipeline-on-apple-silicon]]
<!-- /backlinks:auto -->
