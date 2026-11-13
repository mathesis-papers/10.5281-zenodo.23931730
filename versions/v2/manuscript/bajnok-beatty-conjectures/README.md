# Bajnok–Beatty Conjectures 4.1 and 1.6 (arXiv:2406.04045v1)

The note proves the complete signed two-generator classification for
`Z/2Z × Z/(2k)Z`, for every positive `k,s`. It includes the near-square lattice
lemma, both congruence restrictions, the sufficient lattice construction,
and explicit integer representations for the lower ranges.
It also proves the order bound `|G| ≤ 2s²`, with equality requiring `c | s`,
for arbitrary pairs in `G = Z/cZ × Z/(ck)Z` when `c` is even, removing the
regularity assumption in the source's Theorem 3.2(1).
The posing locators are Section 4, p. 10 (Conjecture 4.1) and Section 1,
p. 3 (Conjecture 1.6).

For every `s ≥ 3`, the largest noncyclic finite abelian group admitting an
`s`-spanning pair has order `2s²` when `2s+1` is prime, and
`2s²+2s−(p²−1)/2` otherwise, where `p` is the smallest prime divisor of
`2s+1`. Coefficient-residue counts prove the upper bound for arbitrary
generating pairs; the attaining constructions are those of Bajnok and
Beatty, Theorem 1.7, Proposition 2.3, and Corollary 2.5.
The same argument removes regularity from Theorems 1.8, 3.2, and 3.3.
For Conjecture 1.10 (Section 1, p. 4), the note proves cyclicity for two
generators, corrects the printed multiplier domain with an explicit perfect
set in `Z/13Z`, and separates the remaining shape assertion from the
higher-dimensional theorem statement cited from Chen–Huang–Luo.
The note also records `N(2)=9` and the absence of a noncyclic group with
a radius-one spanning pair, correcting the literal radius-one claims
in the source's Theorems 1.7 and 1.9.

## Files and reproduction

- `note.tex`: complete LaTeX source, including its bibliography.
- `note.pdf` (distributed separately): the readable note.
- `metadata.json`: title, creators, license, problem identifier, and formal-source link.
- `verify.py`: Python 3 standard-library finite checker.
- `checks.json`: finite-check results for the default bounds.

Build using Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively use a standard TeX installation:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded; BibTeX and external figures are unnecessary.
Reproduce the finite checks with:

```sh
python3 verify.py > checks-reproduced.json
```

The checker exhausts all distinct pairs for `1 ≤ k ≤ 40`, compares radii
`1 ≤ s ≤ 12`, and checks the sufficient families and integer formulas through
`t=12`. Its bounded computations supplement the written unbounded proofs.
The even-first-invariant-factor consequence is checked over all distinct pairs
for `c ∈ {4,6}` and `1 ≤ k ≤ 4`.
The checker also compares 600 odd-invariant-factor residue counts for
`1 ≤ s ≤ 40`, odd `3 ≤ c ≤ 31`; compares the global upper formula with
attaining pairs for `2 ≤ s ≤ 100`; and verifies the perfect-set domain
counterexample in `Z/13Z`.
An exhaustive comparison of all noncyclic two-generator abelian groups of
order at most 61 recovers the global maxima for `2 ≤ s ≤ 5` independently
of the residue formulas.
The note's final section identifies the exact statements of the four linked
Lean declarations at commit `50f2a97bb5e704842f2c32c6095f68a0dc62c779`.
The odd-invariant-factor bound and the conclusions about Conjectures 1.6
and 1.10 are written arguments, separate from those declarations.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`).
