#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA de los decks de la Sesion 2 con el qa.py de la Sesion 1.  Uso: python3 qa2.py [deck.html] [--shot 3 5]"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "sesion-1", "build")))
import qa  # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, ".."))
args = sys.argv[1:]
decks = [a for a in args if a.endswith(".html")] or sorted(f for f in os.listdir(OUT) if re.match(r"\d\d_.*\.html$", f))
shots = args[args.index("--shot") + 1:] if "--shot" in args else []
mal = False
for d in decks:
    print("=" * 12, d)
    mal |= qa.qa_deck(os.path.join(OUT, d), shots)
sys.exit(1 if mal else 0)
