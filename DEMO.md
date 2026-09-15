# Live demo runbook (instructor)

Delete this file before handing the repo to students, or leave it — it gives
away the punchline but nothing else.

## Before class

1. Create a **public** repo on GitHub and push everything in this folder to `main`.
   Public matters: Actions minutes are free on public repos, and the fork
   discussion later only makes sense on a public repo.
2. Open the **Actions** tab once and confirm the CI and Lint runs are green.
   A workflow only runs once it exists on the default branch, so this first
   push is what registers it.
3. Fork the repo to a second account if you want to demo the fork case. Even
   without that, you can talk over the green check on your own PR.
4. Screenshot four things now, in case the runners queue mid-lecture:
   - the Actions tab with a green run
   - a PR with both checks pending (yellow)
   - a PR with a failed check (red X)
   - the expanded log showing the assertion error
5. Set branch protection on `main` requiring the `test` check, then take a
   screenshot of the greyed-out Merge button. Turn it off again if it gets in
   your way during the demo.

## The break (slide 33)

On a branch, change one character in `prime.py`:

```python
    if number <= 1:    # before
    if number < 1:     # after
```

Now `is_prime(1)` returns `True`. The suite fails in well under a second:

```
FAIL: test_is_one_not_prime (test_prime.PrimesEdgeCaseTestCase.test_is_one_not_prime)
AssertionError: True is not false
```

One failing test, one obvious line, and the edge case they added themselves on
slide 14 is the one that catches it. That is the argument for edge cases, made
by the repository instead of by you.

### Do not use the slide-10 break here

The tempting break is the original bug from slides 10–12:

```python
    for element in range(1, number):
```

It makes `is_prime()` return `False` for every number — which means
`print_next_prime()` never finds a prime and **loops forever**. The unit tests
never finish, the job hangs instead of failing, and you get a spinning yellow
dot rather than a red X.

That is a genuinely good five-second aside if you want it: a hanging job is
worse than a failing one, it burns minutes until the runner gives up, and it is
why every job in this repo sets `timeout-minutes: 5`. But do not make it the
demo — you need the red X.

## Sequence in class (about 15 minutes)

| Time | What you do | What to say |
| --- | --- | --- |
| 0:00 | Show the repo, open `.github/workflows/ci.yml` | The config is in the repo, not in a web dashboard |
| 0:02 | `git switch -c break-prime`, make the edit, push | |
| 0:03 | Open the PR on GitHub | Watch the yellow dot appear before you have said anything |
| 0:05 | Checks go red. Click **Details** | The bot answered before any human looked at this |
| 0:07 | Read the log down to the assertion | Ask them which edge case caught this |
| 0:09 | Fix on the same branch, push again | Same PR, new run — no new PR needed |
| 0:12 | Green check, then merge | |
| 0:14 | Point at the Lint check | Two checks, only one of them is a test |

## If the runner queues

Switch to the screenshots and keep talking. Then come back to the tab at the
end of the session — the run will have finished by then, and finishing the arc
live is worth the interruption.

## Fallback: no network

`python -m unittest discover -v` in the terminal shows the same failure. The
whole point of CI is that it runs this for you on someone else's machine, on
every pull request, without being asked — say that while the local run scrolls.
