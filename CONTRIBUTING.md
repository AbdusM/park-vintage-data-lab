# Contributing to Park Vintage Data Lab

Welcome! This project is intentionally simple and learner-first.

## How to contribute

- Open an issue first for larger changes.
- Keep new changes beginner-friendly.
- Update README when you change setup steps.
- Prefer small, clear changes over broad refactors.
- Add comments when code behavior is not obvious.
- Include sample outputs only when they help learners.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Code quality

- Keep scripts readable.
- Use short functions where useful.
- Avoid one-file all-in-one scripts when a small helper is clearer.

## Before submitting a pull request

- Make sure notebooks still have readable markdown instructions.
- Keep data in `data/raw/` immutable.
- Keep `data/processed/` results reproducible by script.
