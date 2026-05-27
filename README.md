# hello

A small Python test project.

## Setup

Requires [uv](https://github.com/astral-sh/uv) (`brew install uv`).

```bash
uv venv
uv pip install -r requirements.txt
```

This creates a `.venv/` in the project root and installs dependencies into it.

## Running

From the terminal:

```bash
uv run hello.py
```

Or activate the venv first and run with plain `python`:

```bash
source .venv/bin/activate
python hello.py
```

## Debugging in VS Code

1. Open this folder in VS Code.
2. Install the recommended **Python** extension when prompted (see `.vscode/extensions.json`).
3. VS Code should auto-select `.venv/bin/python` as the interpreter. If not, run `Python: Select Interpreter` from the command palette and pick the one in `.venv`.
4. Set breakpoints by clicking in the gutter next to any line.
5. Press **F5** and choose a launch config:
   - **Python: Current File** — debugs whichever file is open.
   - **Python: hello.py** — always debugs `hello.py`.

Both configs use the integrated terminal so `input()` prompts work.

## Managing dependencies

```bash
# Add a package
uv pip install <package>

# Update requirements.txt after adding/removing packages
uv pip freeze > requirements.txt

# Reinstall everything from requirements.txt
uv pip install -r requirements.txt
```
