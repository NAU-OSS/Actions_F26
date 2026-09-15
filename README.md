# CS499 — Tests and CI demo

A deliberately tiny Python project used in the Tests and Continuous Integration
lecture. The point is not the code; it is watching GitHub Actions react to it.

## The code

- `prime.py` — `is_prime()` and `print_next_prime()`
- `test_prime.py` — the `unittest` suite we grew one case at a time

## Run the tests locally

```bash
python -m unittest discover -v
```

All tests should pass.

## The workflows

| File | What it does |
| --- | --- |
| `.github/workflows/ci.yml` | Runs the test suite on every push to `main` and on every pull request |
| `.github/workflows/lint.yml` | Runs `flake8` — a check that is not a test |
| `.github/workflows/ci-matrix.yml` | The same tests on 3 operating systems × 3 Python versions |

`ci-matrix.yml` is set to `workflow_dispatch` only, so it runs when you press the
button in the Actions tab rather than on every push. Uncomment the `push` and
`pull_request` triggers when you want it on every change.

## Things worth noticing

- A workflow has to exist on the **default branch** before GitHub will run it.
- The workflow files are in the repository, so they get reviewed like any other code.
- A pull request from a **fork** does not get access to repository secrets, and a
  first-time contributor's run may need a maintainer to approve it.

## Your turn

1. Break something on a branch, open a pull request, and read the failing log.
2. Make the CI check **required** under Settings → Branches → branch protection,
   and watch the Merge button go grey.
3. Add a job that runs `flake8` only on files changed in the pull request.
