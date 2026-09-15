# Terminal cheat sheet — keep this on your second screen

Setup, once, before you start talking:

```bash
cd cs499-ci-demo
clear
export PS1="$ "          # short prompt, no username on the projector
```

---

## Part 1 — the testing half (replaces slides 11–17)

**Show the code, then the tests.**

```bash
cat prime.py
cat test_prime.py
```

**Run them.**

```bash
python -m unittest discover -v
```

Ten tests, all pass. Now break it and let the suite tell you.

**Break it.**

```bash
./break.sh
git diff prime.py
```

One character. Ask them which test will fail before you run it.

**Run again.**

```bash
python -m unittest discover
```

`AssertionError: True is not false` — `test_is_one_not_prime`, the edge case
they added themselves. Point at that: the known cases all still pass. Only the
edge case noticed.

**Fix it.**

```bash
./fix.sh
python -m unittest discover
```

Back to green. That whole loop is about four minutes.

**The hand-off line to Part 2:** "I ran that. What happens when someone else
changes this code and doesn't?"

---

## Part 2 — the CI half

**Show that the config is just a file in the repo.**

```bash
cat .github/workflows/ci.yml
```

Same command as slide 27, same command you just ran by hand.

**Break it on a branch and push.**

```bash
git switch -c break-prime
./break.sh
git commit -am "Simplify the guard in is_prime"
git push -u origin break-prime
```

Then open the PR in the browser. Watch the yellow dot before you say anything.

**Fix on the same branch.**

```bash
./fix.sh
git commit -am "Restore the <= 1 guard"
git push
```

Same PR, second run, green. No new PR needed — say that out loud, it is the
thing students get wrong.

**Clean up after class.**

```bash
git switch main
git branch -D break-prime
git push origin --delete break-prime
```

---

## If something goes sideways

- **Runner queues:** switch to your screenshots, keep talking, come back at the end.
- **No network at all:** Part 1 works entirely offline. Do it, then describe
  Part 2 over the deck.
- **You forgot to push before class:** push `main` first and wait for one green
  run before opening any PR. A workflow will not run until it exists on the
  default branch.
- **Font too small:** `Ctrl/Cmd +` in the terminal, and run `clear` between steps.
