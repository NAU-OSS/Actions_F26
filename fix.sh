#!/usr/bin/env bash
# Demo: put it back.
set -e
sed -i.bak 's/if number < 1:/if number <= 1:/' prime.py && rm -f prime.py.bak
grep -n "if number" prime.py
