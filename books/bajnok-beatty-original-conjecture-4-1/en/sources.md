# Scope, evidence and sources

## What has been proved, and what remains?

The [classification](statements.md#thm-classification) settles Conjecture 4.1 for every positive $k,s$. The [maximum-order formula](statements.md#cor-global) settles Conjecture 1.6 for $s\ge3$, with upper bounds valid for arbitrary spanning pairs. The [universal bound](statements.md#cor-universal) includes the equality group type, removing the earlier special-form assumption in Bajnok–Beatty's Theorem 3.3.

Small radii do not follow by substituting into the maximum formula. At $s=1$, the even-$c$ bound would require $c^2\le2$, while the odd-$c$ residue bound gives $k=0$; neither permits a noncyclic group. At $s=2$, even $c$ permits order at most $8$, and odd $c$ permits only $c=3,k=1$. The standard pair $(1,0),(0,1)$ covers $\mathbb Z_3^2$ in two steps, so $N(2)=9$.

A **perfect** spanning pair represents every group element exactly once using the diamond. It would have order $2s^2+2s+1$. For $s\ge3$ that exceeds the noncyclic bound, so the group must be cyclic. For $s=2$ the order is $13>9$, and for $s=1$ it is the prime $5$; cyclicity holds in these cases too.

The manuscript also corrects a domain in the printed Conjecture 1.10. At $s=2$, the set $\{2,10\}$ in $\mathbb Z/13\mathbb Z$ is perfect: the residues of

$$
0,\quad\pm2,\quad\pm10,\quad\pm4,
$$
$$
\pm20,\quad\pm12,\quad\pm8
$$

are all thirteen residues. It equals $5\{2,3\}$, whereas the multipliers $d=0,1,2,3,4$ give respectively $\{0\},\{2,3\},\{4,6\},\{6,9\},\{8,12\}$, none equal to $\{2,10\}$. The multiplier must range over units modulo $2s^2+2s+1$, rather than residues modulo $2s+1$. The corrected two-generator shape assertion is **not proved in this paper**. Cyclicity, this explicit counterexample to the printed domain, and the corrected shape assertion are distinct statements.

The elementary one-generator and radius-one perfect-set cases are described in the manuscript. Results for three or more generators and the cited higher-dimensional Lee-ball literature are outside this two-dimensional proof. Restricted unsigned bases also use a different coefficient set.

## Exact formal evidence and focused contributions

The following links point directly to Lean source at the book's selected revision. The mathematical statements, rather than an entire paper, are the units of correspondence.

| Manuscript result | Corresponding formal source |
|---|---|
| Theorem 1: all four classification clauses | [All regimes](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyAllRegimes.lean#L339) |
| Lemma 3: actual lattice basis and deficit product | [Near-square rigidity](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/NearSquareLatticeRigidity.lean#L231) |
| Lemma 4: necessary congruences for arbitrary pairs | [Top-strip necessity](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyCayleyNecessity.lean#L305) |
| Lemma 5: sufficient family, including its endpoint | [Uniform construction](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyCayleySufficiency.lean#L265) |
| Corollary 10: global upper bound and attainment | [Sharp maximum](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattySharpMaximum.lean#L390) |

The other six numbered statements have manuscript proofs reproduced in the preceding chapter. Shared requests distinguish short consequences of existing formal proofs from stronger statements requiring additional formal reasoning:

- [Square covering at every positive radius: combine existing covering/counting proofs](https://github.com/the-omega-institute/trureturing-requests/issues/131).
- [Lower ranges: expose a consequence of the existing classification](https://github.com/the-omega-institute/trureturing-requests/issues/132).
- [Maximum within the family: deduce the extremal corollary from that classification](https://github.com/the-omega-institute/trureturing-requests/issues/133).
- [Even first invariant factor: include small radii and the equality divisibility condition](https://github.com/the-omega-institute/trureturing-requests/issues/134).
- [Odd first invariant factor: retain the full three-part residue bound](https://github.com/the-omega-institute/trureturing-requests/issues/135).
- [Universal bound: complete the equality isomorphism classification](https://github.com/the-omega-institute/trureturing-requests/issues/136).

Contributors can coordinate on these canonical requests and submit focused PRs from their own forks directly to [upstream `dev`](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). In particular, the classification and sharp maximum should be reused. A request is a contribution route, not a mathematical open problem or a verification receipt.

## Sources and attribution

- Haobo Ma and Wenlin Zhang, *Bajnok–Beatty Conjectures 4.1 and 1.6 (arXiv:2406.04045v1, Section 4, p. 10; Section 1, p. 3): classification and extremal noncyclic order*, version 2. [Version DOI:10.5281/zenodo.23931731](https://doi.org/10.5281/zenodo.23931731). The [concept DOI:10.5281/zenodo.23931730](https://doi.org/10.5281/zenodo.23931730) identifies the work across versions. Haobo Ma: Chrono AI, Singapore. Wenlin Zhang: National University of Singapore and Chrono AI, Singapore. The recorded paper is licensed CC BY 4.0.
- B. Bajnok and W. K. Beatty, *On the Diameter of Undirected Cayley Graphs of Finite Abelian Groups*, [arXiv:2406.04045v1](https://arxiv.org/abs/2406.04045v1), 2024; published in *Combinatorics and Number Theory* **14** (2025), 1–12, [DOI:10.2140/cnt.2025.14.1](https://doi.org/10.2140/cnt.2025.14.1). Original v1 locators: Conjecture 4.1, §4, p. 10; Conjecture 1.6, §1, p. 3; Conjecture 1.10, §1, p. 4. Theorems 4.2–4.4 supply the earlier ranges; Theorem 1.7 and the §2 constructions supply attainment.
- R. Dougherty and V. Faber, *The degree-diameter problem for several varieties of Cayley graphs, I: The Abelian case*, *SIAM Journal on Discrete Mathematics* **17** (2004), 478–519, [DOI:10.1137/S0895480100372899](https://doi.org/10.1137/S0895480100372899). The quotient-lattice formulation is Proposition 2 in [arXiv:math/9412223v2](https://arxiv.org/abs/math/9412223v2), p. 6.

The central geometric step uses the quotient-lattice viewpoint, while the sharp maximum combines the paper's residue upper bound with Bajnok and Beatty's existing attaining constructions. The complete original bibliography and higher-dimensional attributions are available in the [public version PDF](https://zenodo.org/records/23931731/files/note-v2.pdf); they are not needed as premises of the two-dimensional proofs above.
