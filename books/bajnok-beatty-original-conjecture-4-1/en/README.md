# How far can two moves take you?

Choose two moves on a board that wraps around. You may repeat either move forwards or backwards. Can you reach every position from the origin in at most $s$ steps? This paper by Haobo Ma and Wenlin Zhang answers two questions of B. Bajnok and W. K. Beatty: exactly when one family of boards works, and how many positions any noncyclic finite abelian group can have if two moves suffice. The answers depend on more than area: parity controls the first, and the smallest prime divisor of $2s+1$ controls the second.

Here is the surprise. Write a position as $(\eta,z)$, with the first coordinate taken modulo $2$ and the second modulo $2k$. There are $4k$ positions. At radius $s=4$, no two distinct moves cover all $28$ positions when $k=7$, yet a suitable pair covers all $32$ positions when $k=8$. The obstruction is the shape of the integer relations between the moves. The [complete classification](statements.md#thm-classification) describes it exactly.

## What counts as a move?

Arithmetic modulo $n$ works like a clock: after $n$ comes $0$ again. On $G_2=\mathbb Z/2\mathbb Z\times\mathbb Z/4\mathbb Z$, choose $a=(1,1)$ and $b=(0,1)$. The four positions with first coordinate $0$ are reached by $0,b,2b,-b$. Those with first coordinate $1$ are reached by $a-b,a,a+b,-a$. Each expression uses at most two moves.

The choice of moves matters, as well as the size of the group. In general, integers $x,y$ record the net numbers of uses of $a,b$; a negative coefficient means going backwards. The cost is $|x|+|y|$. We call $\{a,b\}$ an **$s$-spanning pair** when every position has an expression

$$
g=xa+yb,\qquad |x|+|y|\le s.
$$

The moves are distinct, repetition is allowed, and the bound is “at most”. The group is abelian: changing the order of the moves does not change the endpoint. A group is noncyclic if no single move visits all its positions by repetition. For example, each element of $G_k$ has order at most $2k$, less than the group's order $4k$.

## The answer: size first, then congruences near the limit

For all positive integers $k,s$, the board $G_k$ works exactly in these four cases:

| Radius | Complete condition on $k$ |
|---|---|
| $s$ odd | $2k\le s^2-1$ |
| $s$ even, lower range | $2k\le s^2-s$ |
| $s\equiv0\pmod4$, upper range | $s^2-s<2k\le s^2$, and $k$ even |
| $s\equiv2\pmod4$, upper range | $s^2-s<2k\le s^2$, and $k\equiv2\pmod4$ |

The notation $k\equiv2\pmod4$ means remainder $2$ on division by $4$. At $s=4$, every $k\le6$ works. The upper range contains $7,8$, and only $8$ is even. At $s=6$, every $k\le15$ works, while only $18$ among $16,17,18$ has remainder $2$ modulo $4$. At $s=1$ no positive $k$ works. Remember that $2k$ is half the group's order, not its order.

Bajnok and Beatty had proved the size bound, odd-radius classification and lower even range. The new step completes the narrow upper interval; this paper also supplies the lower-range arguments. Their conjecture numbers refer to arXiv:2406.04045v1, not to the chapters of this explanation.

## Why draw a diamond?

Plot each coefficient pair $(x,y)$ on the integer plane. The allowed pairs $|x|+|y|\le s$ form a diamond: every extra horizontal step uses one step that could have been vertical. It contains $2s^2+2s+1$ integer points, since the ring at distance $j>0$ contains $4j$ points.

Different coefficient pairs can reach the same position. If $ua+vb=0$, adding $(u,v)$ to a coefficient pair leaves its endpoint unchanged. All these integer relations form a lattice $K$. The question becomes: does every equivalence class modulo $K$ meet the diamond? These classes correspond exactly to board positions.

For $G_k$, reduction modulo $2$ proves $K\subseteq2\mathbb Z^2$, while $K$ is not contained in $4\mathbb Z^2$. Every relation has two even coordinates, but they cannot all be divisible by four. These facts will force the congruence obstruction.

Set $T(u,v)=(u+v,u-v)$ and $M=T^{-1}K$. The identity

$$
|x|+|y|=\max\{|x+y|,|x-y|\}
$$

relates the diamond to a square. Integer parity requires a suitable translation; a picture of a rotated diamond alone does not justify the count. The [square-covering lemma](statements.md#lem-square) proves that each class modulo $M$ has a representative in an $s$ by $s$ integer square. There are $2k$ classes, so $2k\le s^2$.

## Why is an almost full square rigid?

Suppose an $n$ by $n$ square covers $n^2-\delta$ lattice classes with $0\le\delta<n$. So few repetitions are available that the lattice must have a basis

$$
(n,-\epsilon B),\qquad(-A,\epsilon n),
$$

where $0\le A,B<n$, $\epsilon=\pm1$ and $AB=\delta$. The product appears because the parallelogram formed by these vectors has area $n^2-AB$, exactly the number of classes. To prove it, cover the column just outside the right edge. This supplies relation vectors going upwards and downwards. Their determinant must be a positive multiple of the index, but the available area is less than twice that index. It therefore equals the index. The resulting inequalities force vectors to reach the full side length. The [complete proof](statements.md#lem-rigidity) includes $\delta=0$.

In the upper range for $s=2t$, write $k=2t^2-r$, where $0\le r<t$. The lemma gives $AB=2r$. Every vector of $M$ has even coordinate sum, forcing $A=2u,B=2v$. Hence $r=2uv$ is even. If $t$ is odd and $4$ does not divide $r$, both $u,v$ are odd. Applying $T$ then puts both basis vectors in $4\mathbb Z^2$, contradicting the earlier fact about $K$. Thus odd $t$ requires $4\mid r$ too. These are exactly the two upper-range congruences.

Necessity still needs a matching construction. The paper uses the relation vectors

$$
V=(2(t-j),-2(t+j)),
$$
$$
W=(2(t-1),2(t+1)).
$$

For $0\le j<t$, with $t$ or $j$ even, the quotient is exactly $\mathbb Z/2\mathbb Z\times\mathbb Z/(4(t^2-j))\mathbb Z$. Subtracting suitable relations moves any coefficient pair back into a bounded square; the norm identity then gives at most $2t$ steps. Every admissible upper-range value has $r=2j$ and is obtained this way. The [sufficiency proof](statements.md#lem-family) treats the endpoint $t=1,j=0$ separately.

The short film follows the mechanism from moves to the diamond, the square, and the congruence obstruction.

::: {.film src="001-diamond-square"}
From a diamond to a square: why $28$ positions can fail while $32$ succeed.
:::

## If we allow other boards, how large can they be?

Every noncyclic finite abelian group generated by two elements has the form
$\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$, with $c\ge2$, $k\ge1$ and order $c^2k$. Let $N(s)$ be the largest order admitting an $s$-spanning pair. For $s\ge3$,

$$
N(s)=2s^2\quad\text{if }2s+1\text{ is prime};
$$
If $2s+1$ is composite,

$$
N(s)=2s^2+2s-\frac{p^2-1}{2}.
$$

where $p$ is the smallest prime divisor of $2s+1$. For $s=3$, the number $7$ is prime and $N(3)=18$. For $s=4$, the smallest prime divisor of $9$ is $3$, so $N(4)=36$. The latter value is attained by $(1,1),(1,2)$ in $\mathbb Z/3\mathbb Z\times\mathbb Z/12\mathbb Z$, exceeding the maximum $32$ with first factor fixed at $2$.

The key is to sort coefficients by their residues modulo $c$. All relation vectors belong to $c\mathbb Z^2$, so all representations of one group element have the same coefficient residues. Each residue class must reach $k$ group elements. The sparsest residue class in the diamond therefore limits $k$. For odd $c$, the sum-and-difference transformation is invertible modulo $c$. Let $E_i,O_i$ count the even and odd representatives of residue $i$ in $[-s,s]$. A prescribed pair of residues contains exactly $E_iE_j+O_iO_j$ diamond points.

For $s=4,c=3$, residue $2$ has representatives $-4,-1,2$: two even and one odd. Residue $0$ has representatives $-3,0,3$: one even and two odd. This gives $2\cdot1+1\cdot2=4$ points, forcing $k\le4$ and order at most $36$. The [precise chapter](statements.md#lem-odd) gives the general three-part count. Exceeding $2s^2$ is possible only if $c\mid2s+1$. The penalty $(c^2-1)/2$ grows with $c$, so the smallest prime factor wins. Bajnok and Beatty supplied the attaining constructions. This paper supplies the matching upper bound for arbitrary pairs, removing the earlier special-form assumption.

The academic presentation follows this proof route and puts the detailed count in an appendix.

::: {.slides src="seminar"}
Aligned Chinese and English Beamer editions with speaker notes.
:::

## Where to go next

[Exact statements and proofs](statements.md) retains all eleven numbered results and their dependencies. [Scope, evidence and sources](sources.md) explains which statements have corresponding Lean theorems, which written proofs still need formalization, and the precise boundary of the perfect-spanning-set discussion. Small radii are separate: no noncyclic group works at radius $1$, and the maximum at radius $2$ is $9$, attained by $\mathbb Z_3^2$.
