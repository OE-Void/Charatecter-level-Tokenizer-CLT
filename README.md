CLT — Character-Level Tokenizer

Summary

CLT is a minimal character-level tokenizer utility. It reads a local `token.txt` file to build a character vocabulary and provides simple helper functions to encode strings into token indices and decode indices back to strings. The project is intentionally small and dependency-free so it can be used as a lightweight starter tokenizer or for testing and learning purposes.

Notes on purpose

This implementation operates at the character level (one symbol per token). Modern tokenizers often use subword or byte-pair encodings to reduce the number of tokens required for common words; character-level tokenizers are simpler but produce longer sequences. CLT is useful when you need a tiny, deterministic tokenizer and don't want to rely on external libraries.

Requirements

- Python 3.8 or newer
- No third-party packages are required for the current code

Installation

1. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (none required now):

```bash
pip install -r requirements.txt
```

Preparing `token.txt`

The code expects a file named `token.txt` in the repository root. This repository currently includes `token.txt` (it contains the project's character vocabulary). If you prefer to keep the vocabulary file tracked, no action is needed. If you would rather stop tracking `token.txt` (for privacy or to avoid committing changes), remove it from the index and keep it ignored with these commands:

```bash
# remove token.txt from the repository but keep the local file
git rm --cached token.txt
git commit -m "remove token.txt from repository (keep locally)"
# ensure .gitignore contains token.txt so it won't be re-added
```

If you need to create a simple test `token.txt`, you can still generate one locally with:

```bash
echo "abcdefghijklmnopqrstuvwxyz\n" > token.txt
```

Usage

Import and use the `encode` and `decode` helpers from the `clt.clt` module. Example (run from the repository root):

```bash
python -c "from clt.clt import encode, decode; s='hello'; i=encode(s); print('encoded:', i); print('decoded:', decode(i))"
```

Or in a Python script or REPL:

```python
from clt.clt import encode, decode

encoded = encode('hello')
print('encoded:', encoded)
print('decoded:', decode(encoded))
```

Files

- `clt/clt.py` — module that reads `token.txt`, constructs `char_to_idx` and `idx_to_char`, and defines `encode` and `decode`.
- `requirements.txt` — project requirements (currently no third-party packages).
- `.gitignore` — recommended ignores for the repository. Note: `token.txt` is currently tracked in this repository; `.gitignore` will prevent new untracked copies from being added but will not untrack files that are already committed.
- `token.txt` — currently included in the repository (contains the character vocabulary).

Developer notes

- The module reads `token.txt` at import time. For larger vocabularies or production use, consider adding an explicit loader function and avoiding heavy I/O during import.
- If you add third-party packages, list them and pin versions in `requirements.txt`.

Contributing

Contributions are welcome. Open an issue or a pull request with a short description of the change.

License

MIT
