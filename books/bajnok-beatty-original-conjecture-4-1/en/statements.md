# Exact statements and proofs

Write $G_k=\mathbb Z/2\mathbb Z\times\mathbb Z/(2k)\mathbb Z$, with $k\ge1$. An $s$-spanning pair consists of distinct $a,b$ for which every $g$ equals $xa+yb$ with integers $x,y$ satisfying $|x|+|y|\le s$. Throughout, $s\ge1$ unless a statement specifies a stronger bound. The eleven results below retain the original manuscript's shared theorem/lemma/corollary numbering. Their proofs follow Haobo Ma and Wenlin Zhang, version 2, [DOI:10.5281/zenodo.23931731](https://doi.org/10.5281/zenodo.23931731).

For an $s$-spanning pair, define the additive surjection $f:\mathbb Z^2\to G_k$ by $f(x,y)=xa+yb$, and put $K=\ker f$, $T(u,v)=(u+v,u-v)$ and $M=T^{-1}K$. Reduction modulo $2G_k$ gives a bijection from $(\mathbb Z/2\mathbb Z)^2$ to $G_k/2G_k$, so $K\subseteq2\mathbb Z^2$. Choose $z$ with $f(z)=(1,0)$. Then $2z\in K$, but if $K\subseteq4\mathbb Z^2$, we would have $z\in2\mathbb Z^2$, contradicting the first coordinate of $f(z)$. Thus $K\not\subseteq4\mathbb Z^2$. The image of $T$ consists of pairs with equal coordinate parity, has index $2$, and contains $K$. Consequently $T(M)=K$ and $[\mathbb Z^2:M]=2k$. Every $(u,v)\in M$ has even coordinate sum. These facts are the setup for Lemmas 2–4, not extra hypotheses on the generators.

## Theorem 1: Classification of Conjecture 4.1

::: {.theorem #thm-classification title="Classification of Conjecture 4.1" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s1" lean="D5/S3/FiniteGroups/BajnokBeattyAllRegimes.result"}
For positive integers $k,s$, the group $G_k$ has an $s$-spanning pair
if and only if one of the following conditions holds:

1. $s$ is odd and $2k\le s^2-1$.
2. $s$ is even and $2k\le s^2-s$.
3. $s\equiv0\pmod4$, $k$ is even, and $s^2-s<2k\le s^2$.
4. $s\equiv2\pmod4$, $k\equiv2\pmod4$, and $s^2-s<2k\le s^2$.
:::

::: {.proof #pf-thm-classification}
[@lem-square] gives $2k\le s^2$ for every spanning pair.
For odd $s$, the even integer $2k$ is at most $s^2-1$, and
[@lem-lower] gives the converse.
For even $s=2t$, [@lem-lower] treats $2k\le s^2-s$.
In the remaining interval put $r=2t^2-k$; then $0\le r<t$.
[@lem-congruences] says that $r$ is even, and that
$4\mid r$ when $t$ is odd. If $t$ is even this is exactly the
condition that $k$ is even. If $t$ is odd it is exactly
$k\equiv2\pmod4$.
Conversely these congruences give $r=2j$ with $0\le2j<t$ and
$t$ even or $j$ even. Then $k=2(t^2-j)$, and
[@lem-family] supplies a $2t$-spanning pair.
:::

## Lemma 2: Square covering

::: {.lemma #lem-square title="Square covering" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s2" status="written-proof" proof="pf-lem-square" doi="10.5281/zenodo.23931731" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/131"}
If $f$ maps the integer diamond $|x|+|y|\le s$ onto $G_k$, every
coset of $M$ has a representative in $\{0,\ldots,s-1\}^2$.
In particular, $2k\le s^2$.
:::

::: {.proof #pf-lem-square}
First let $s=2t$. Given $z\in\mathbb Z^2$, put
$v=T(z-(t,t))+(1,0)$ and choose $w$ with $f(w)=f(v)$ and
$\lVert w\rVert_1\le2t$. Since $w-v\in K\subseteq2\mathbb Z^2$, the integers
$w_1+w_2$ and $w_1-w_2$ are odd. Their absolute values are at most
$2t-1$. Hence
$$
q=\big((w_1+w_2-1)/2,(w_1-w_2-1)/2\big),
$$

$$
q\in\{-t,\ldots,t-1\}^2.
$$
As $w=T(q)+(1,0)$, we have $z-(q+(t,t))\in M$, as required.

If $s=2t+1$, instead take $v=T(z-(t,t))$. Now $w_1+w_2$ and
$w_1-w_2$ are even, with absolute values at most $2t$.
Take $q=((w_1+w_2)/2,(w_1-w_2)/2)\in\{-t,\ldots,t\}^2$.
The same subtraction gives the required representative. The square has
$s^2$ points, so $[\mathbb Z^2:M]=2k$ proves the bound.
:::

## Lemma 3: Near-square rigidity

::: {.lemma #lem-rigidity title="Near-square rigidity" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s3" lean="D5/S3/FiniteGroups/NearSquareLatticeRigidity.near_square_rigidity"}
Let $n\ge2$, $0\le\delta<n$, and $[\mathbb Z^2:L]=n^2-\delta$.
Suppose every coset of $L$ meets $\{0,\ldots,n-1\}^2$.
Then for some $0\le A,B<n$ and $\epsilon\in\{1,-1\}$,
$$
AB=\delta,
$$

$$
L=\mathbb Z(n,-\epsilon B)+\mathbb Z(-A,\epsilon n).
$$
:::

::: {.proof #pf-lem-rigidity}
Write $d=n^2-\delta$. Then $d>n(n-1)$ and $2d>n^2$.
For each $0\le y<n$, applying the covering assumption to $(n,y)$
produces a vector $(p,q)\in L$ with
$$
1\le p\le n,\qquad -(n-1)\le q\le n-1,
$$

$$
0\le y-q<n.
$$
First suppose $(p,0)\in L$ for some $1\le p\le n$.
Covering $(0,n)$ produces $(-x,n-z)\in L$ with $0\le x,z<n$.
Their determinant $p(n-z)$ is a positive multiple of $d$ at most $n^2$,
so it equals $d$. If either $p<n$ or $z>0$, this determinant is at most
$n(n-1)$, a contradiction. Thus $p=n$, $z=0$, $\delta=0$, and the
two vectors $(n,0),(-x,n)$ give the desired basis.

Otherwise no vector $(p,0)$ with $1\le p\le n$ belongs to $L$.
Let $b$ be the least positive integer such that $(p,-b)\in L$ for
some $1\le p\le n$, and let $c$ be the least positive integer such
that $(r,c)\in L$ for some $1\le r\le n$. Such integers exist by
the displayed column inequalities with $y=0,n-1$, and $b,c<n$.
For any $0\le y<n$, the vector in the displayed column inequalities has either
$q\le-b$, giving $y\le n-1-b$, or $q\ge c$, giving $y\ge c$.
There can be no missing integer between these intervals, so $b+c\le n$.
The determinant of $(p,-b),(r,c)$ is
$$
0<pc+rb\le n(b+c)\le n^2.
$$
It is a multiple of $d$, and therefore equals $d$.
If $b+c<n$, or if both $p<n$ and $r<n$, it is at most $n(n-1)$,
again impossible. Hence $b+c=n$, and either $p=n$ or $r=n$.
If $p=n$, use $(n,-b)$ and $(r,c)-(n,-b)=(-(n-r),n)$.
Here $A=n-r$, $B=b$, and $AB=\delta$.
If $r=n$, use $(n,c)$ and $(p,-b)-(n,c)=(-(n-p),-n)$,
with $A=n-p$, $B=c$, and $\epsilon=-1$.
In each case the two vectors lie in $L$ and their absolute determinant
is $d$, so their span equals $L$.
:::

## Lemma 4: Necessary congruences

::: {.lemma #lem-congruences title="Necessary congruences" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s4" lean="D5/S3/FiniteGroups/BajnokBeattyCayleyNecessity.top_strip_necessity"}
If $s=2t$, $k=2t^2-r$, and $0\le r<t$, any $s$-spanning pair in
$G_k$ satisfies $2\mid r$; if $t$ is odd, it also satisfies $4\mid r$.
:::

::: {.proof #pf-lem-congruences}
Apply [@lem-rigidity] to $M$, using [@lem-square],
with $n=2t$ and $\delta=2r$. It gives the basis
$(2t,-\epsilon B),(-A,\epsilon2t)$ with $AB=2r$.
Every vector of $M$ has even coordinate sum. Thus $A=2u$ and $B=2v$
for nonnegative integers $u,v$, and $r=2uv$ is even.
If $t$ is odd and $4\nmid r$, both $u,v$ are odd. Applying $T$ to
the two basis vectors gives
$$
2(t-\epsilon v,t+\epsilon v),
$$

$$
2(-u+\epsilon t,-u-\epsilon t).
$$
Both belong to $4\mathbb Z^2$. Since they generate $T(M)=K$, this contradicts
$K\subseteq2\mathbb Z^2$, $K\not\subseteq4\mathbb Z^2$.
:::

## Lemma 5: A sufficient family

::: {.lemma #lem-family title="A sufficient family" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s5" lean="D5/S3/FiniteGroups/BajnokBeattyCayleySufficiency.result"}
Let $t\ge1$ and $0\le j<t$. If $t$ is even or $j$ is even, the group
$\mathbb Z/2\mathbb Z\times\mathbb Z/(4(t^2-j))\mathbb Z$ has a $2t$-spanning pair.
:::

::: {.proof #pf-lem-family}
Let $L$ be generated by
$$
V=(2(t-j),-2(t+j)),
$$
$$
W=(2(t-1),2(t+1)).
$$
The absolute determinant is $8(t^2-j)$. The greatest common divisor of
the four entries is $2$: after division by $2$ any common divisor
divides both $t-1$ and $t+1$, hence divides $2$; an odd entry occurs
when $t$ is even, or when $t$ is odd and $j$ is even.
The elementary integer row and column reductions for a rank-two matrix
therefore give
$$
\mathbb Z^2/L\simeq\mathbb Z/2\mathbb Z\times\mathbb Z/(4(t^2-j))\mathbb Z.
$$
Here we use the Smith normal form rule: its first invariant is the
greatest common divisor of the entries and its second is the absolute
determinant divided by the first.

We show that every coset has a representative of $\ell^1$-norm at most
$2t$. Under $T$, the two relation vectors are
$$
T(W)=(4t,-4)=U,
$$

$$
T(V)=(-4j,4t)=V'.
$$
Assume first $t>1$. Their sum has both coordinates positive, since
$j<t$. For a given $z\in\mathbb Z^2$, the coset of $T(z)+(2t,2t)$
modulo $\mathbb Z U+\mathbb Z V'$ therefore has a nonnegative representative.
Choose one, $(X,Y)$, with least coordinate sum.
If $X\ge4t$, subtraction of $U$ preserves nonnegativity and reduces
the sum by $4(t-1)>0$. If $Y\ge4t$, subtraction of $V'$ preserves
nonnegativity and reduces the sum by $4(t-j)>0$.
Consequently $0\le X,Y<4t$.
For $t=1$ necessarily $j=0$; reduction first by $U=(4,-4)$ and then
by $V'=(0,4)$ gives the same square by integer division.

Subtracting $(2t,2t)$ yields a vector $T(w)$ with $w\in z+L$ and
both coordinates in $[-2t,2t-1]$. The identity
$$
|w_1|+|w_2|=\max\{|w_1+w_2|,|w_1-w_2|\}
$$
gives the required norm bound. Finally, $L\subseteq2\mathbb Z^2$, so the
images of $(1,0)$ and $(0,1)$ in $\mathbb Z^2/L$ are distinct.
Their images under the displayed isomorphism are the desired pair.
:::

## Lemma 6: Lower ranges

::: {.lemma #lem-lower title="Lower ranges" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s6" status="written-proof" proof="pf-lem-lower" doi="10.5281/zenodo.23931731" source="Lemma 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/132"}
If $s$ is odd and $2k\le s^2-1$, or if $s$ is even and
$2k\le s^2-s$, the group $G_k$ has an $s$-spanning pair.
:::

::: {.proof #pf-lem-lower}
For $t\ge0$, the two vectors $(1,t),(1,t+1)$ in $\mathbb Z/2\mathbb Z\times\mathbb Z$
represent every $(\eta,z)$ with $|z|\le2t(t+1)$ using coefficient
norm at most $2t+1$. Here is an explicit verification.
For $\eta=0$, write
$$
z=(2t+1)q+w,\quad -t\le w\le t,
$$

$$
q=\left\lfloor\frac{z+t}{2t+1}\right\rfloor.
$$
The bound on $z$ gives $-t\le q\le t$.
Take $x=q-w$, $y=q+w$. Then $x+y$ is even,
$tx+(t+1)y=z$, and $|x|+|y|=2\max(|q|,|w|)\le2t$.
For $\eta=1$, write $z=(2t+1)q+u$, $0\le u\le2t$.
Now $-t-1\le q\le t$. Set
$$
x=q+1-u+t,\qquad y=q+u-t.
$$
Then $x+y=2q+1$ is odd and $tx+(t+1)y=z$.
Also $x-y=2t+1-2u$; thus the same norm identity gives
$|x|+|y|\le2t+1$.
For odd $s=2t+1$, choose an integer representative $z$ of the second
coordinate with $|z|\le k\le2t(t+1)$, and reduce this construction
modulo $2k$. The pair is distinct since its second coordinates differ
by $1$ modulo $2k$.

For even $s=2t$, use $(1,t-1),(1,t)$. The preceding construction
with parameter $t-1$ covers both first coordinates for
$|z|\le B=2t(t-1)$ with coefficient norm at most $2t-1$.
The three integer intervals $ct+[-B,B]$, $c=-1,0,1$, cover
$[-B-t,B+t]$: their endpoints are adjacent or overlap because
$t\le2B+1$. This last inequality holds at $t=1$, and for $t>1$ it
follows from $(t-1)(4t-1)\ge0$.
Choose $c$ with $|z-ct|\le B$, represent $(\eta-c,z-ct)$ in the
smaller range, and add $c(1,t)$. The coefficient norm is at most
$2t$. As $k\le B+t=2t^2-t$, reduction modulo $2k$ gives the claim,
again with distinct elements.
:::

## Corollary 7: Maximum within the family

::: {.corollary #cor-family-max title="Maximum within the family" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s7" status="written-proof" proof="pf-cor-family-max" doi="10.5281/zenodo.23931731" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/133"}
Among groups $G_k$ with an $s$-spanning pair, the largest order is
$2s^2$ for even $s\ge2$, and $2s^2-2$ for odd $s\ge3$.
There is no such group for $s=1$.
:::

::: {.proof #pf-cor-family-max}
The order is $4k$. For odd $s\ge3$, take $2k=s^2-1$.
For even $s$, take $k=s^2/2$: it is even if $s\equiv0\pmod4$,
and it is $2$ modulo $4$ if $s\equiv2\pmod4$.
The upper bounds and the assertion for $s=1$ follow from
[@thm-classification].
:::

## Corollary 8: Even first invariant factor

::: {.corollary #cor-even title="Even first invariant factor" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s8" status="written-proof" proof="pf-cor-even" doi="10.5281/zenodo.23931731" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/134"}
Let $c\ge2$ be even and $k,s\ge1$. If
$G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$ has an $s$-spanning pair, then
$|G|\le2s^2$. Equality requires $c\mid s$.
In particular, if $s$ is odd then $|G|\le2s^2-2$.
:::

::: {.proof #pf-cor-even}
Let $f:\mathbb Z^2\to G$ be the surjection induced by the pair, and put
$K=\ker f$. The induced surjection $(\mathbb Z/c\mathbb Z)^2\to G/cG$ is bijective,
since both groups have order $c^2$. Thus $K\subseteq c\mathbb Z^2\subseteq2\mathbb Z^2$.
For $M=T^{-1}K$ we have $T(M)=K$ and $[\mathbb Z^2:M]=|G|/2$.
The proof of [@lem-square], which uses only $K\subseteq2\mathbb Z^2$,
therefore gives $|G|/2\le s^2$.
If equality holds, $s\ge2$ and [@lem-rigidity] applies with
$n=s$, $\delta=0$. Its basis has $AB=0$. If $B=0$, applying $T$ to
the first basis vector gives $(s,s)\in K$. If $A=0$, applying $T$ to
the second gives $(\epsilon s,-\epsilon s)\in K$.
In either case $K\subseteq c\mathbb Z^2$ implies $c\mid s$.
For odd $s$ equality is impossible; since $4\mid|G|$,
the inequality sharpens to $|G|\le2s^2-2$.
:::

## Lemma 9: Odd first invariant factor

::: {.lemma #lem-odd title="Odd first invariant factor" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s9" status="written-proof" proof="pf-lem-odd" doi="10.5281/zenodo.23931731" source="Lemma 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/135"}
Let $c\ge3$ be odd, and write $s=ct+r$ with $0\le r<c$.
If $G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$ has an $s$-spanning pair, then $k\le F_c(s)$. Put $h=(c-1)/2$ and define

$$
F_c(s)=\begin{cases}
2t^2,&0\le r<h,\\
2t(t+1),&h\le r<c-1,\\
2t(t+1)+1,&r=c-1.
\end{cases}
$$
No regularity hypothesis on the pair is required.
:::

::: {.proof #pf-lem-odd}
For the surjection $f:\mathbb Z^2\to G$ induced by the pair, put $K=\ker f$.
As in [@cor-even], $K\subseteq c\mathbb Z^2$.
Consequently all representatives of any one element of $G$ have the
same coefficient residue modulo $c$. Each of the $c^2$ coefficient
residues corresponds to one coset of $cG$, with $k$ elements.
Each residue class in the diamond $|x|+|y|\le s$ must therefore
contain at least $k$ points.

Put $U=x+y$ and $V=x-y$. Since $c$ is odd, this is an invertible
change of coordinates modulo $c$. Over the integers it identifies
the diamond with $|U|,|V|\le s$, $U\equiv V\pmod2$.
For a residue $i$ modulo $c$, let $E_i,O_i$ count its even and odd
representatives in $[-s,s]$. A prescribed pair of residues for $U,V$
therefore contains $E_iE_j+O_iO_j$ diamond points.

Choose $i=s+1\pmod c$. Its representatives are $s+1-\ell c$,
$1\le\ell\le\lfloor(2s+1)/c\rfloor$, with alternating parity.
If $r<(c-1)/2$, there are $2t$ representatives, so $E_i=O_i=t$.
Taking $j=i$ gives $2t^2$ points.
If $(c-1)/2\le r<c-1$, both $i=s+1$ and $j=s+2$ have $2t+1$
representatives: for the latter the number is
$\lfloor(2s+2)/c\rfloor=2t+1$.
Their first representatives have opposite parity. Thus their counts
are $(t,t+1)$ and $(t+1,t)$, giving $2t(t+1)$ points.
If $r=c-1$, take $j=i$ again. There are $2t+1$ representatives, giving
$t^2+(t+1)^2=2t(t+1)+1$ points. In each case $k$ is at most this count.
:::

## Corollary 10: Maximum noncyclic order

::: {.corollary #cor-global title="Maximum noncyclic order" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s10" lean="D5/S3/FiniteGroups/BajnokBeattySharpMaximum.sharp_maximum"}
For $s\ge3$, the largest order $N(s)$ of a noncyclic finite abelian
group with an $s$-spanning pair is
$$
N(s)=2s^2\quad\text{if }2s+1\text{ is prime};
$$

If $2s+1$ is composite,

$$
N(s)=2s^2+2s-\frac{p^2-1}{2}.
$$
where $p$ is the smallest prime divisor of $2s+1$ in the second case.
:::

::: {.proof #pf-cor-global}
By the structure theorem for finite abelian groups generated by two elements, such a noncyclic group has the form $G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$ with $c\ge2$.
Even $c$ gives $|G|\le2s^2$ by [@cor-even].
For odd $c$, apply [@lem-odd].
In its first case, $c^2F_c(s)=2c^2t^2\le2s^2$.
In its middle case,
$$
c^2F_c(s)-2s^2=2ct(c-2r)-2r^2.
$$
This is negative for $r>(c-1)/2$. At $r=(c-1)/2$ it gives exactly
$$
|G|\le2s^2+2s-(c^2-1)/2,
$$

$$
c\mid 2s+1.
$$
In the last case the difference is
$$
\begin{aligned}
c^2F_c(s)-2s^2&=-2ct(c-2)\\
&\quad-c^2+4c-2<0.
\end{aligned}
$$
For $c\ge5$ the constant term is already negative; for $c=3$, $s\ge3$
and $r=2$ imply $t\ge1$, giving $1-6t<0$.

If $2s+1$ is prime, its only possible divisor $c\ge3$ in the exceptional
middle case is $c=2s+1$. Then $t=0$ and $F_c(s)=0$, incompatible with
$k\ge1$. Hence $|G|\le2s^2$.
If $2s+1$ is composite, every exceptional $c$ satisfies $c\ge p$;
its bound is at most $2s^2+2s-(p^2-1)/2$.
This exceeds $2s^2$: writing $2s+1=pq$ with $q\ge p$ gives excess
$pq-1-(p^2-1)/2\ge(p^2-1)/2>0$.

The matching constructions are those of Bajnok–Beatty [Theorem 1.7, Proposition 2.3 and Corollary 2.5](https://arxiv.org/abs/2406.04045v1):
$\mathbb Z/s\mathbb Z\times\mathbb Z/(2s)\mathbb Z$ attains $2s^2$.
In the composite case, put $q=(2s+1)/p$ and $t=(q-1)/2\ge1$.
The pair $\{(1,t),(1,t+1)\}$ in
$\mathbb Z/p\mathbb Z\times\mathbb Z/(2pt(t+1))\mathbb Z$ is $s$-spanning by
Bajnok–Beatty [Theorem 2.4](https://arxiv.org/abs/2406.04045v1), with order $2s^2+2s-(p^2-1)/2$.
All these groups are noncyclic and the indicated pairs are distinct.
:::

## Corollary 11: Universal bound and equality

::: {.corollary #cor-universal title="Universal bound and equality" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s11" status="written-proof" proof="pf-cor-universal" doi="10.5281/zenodo.23931731" source="Corollary 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/136"}
For $s\ge3$, every noncyclic finite abelian group with an $s$-spanning
pair has order at most $2s^2+2s-4$.
Equality holds precisely for the isomorphism type
$\mathbb Z/3\mathbb Z\times\mathbb Z/((2s^2+2s-4)/3)\mathbb Z$, with $s\equiv1\pmod3$.
:::

::: {.proof #pf-cor-universal}
The nonexceptional bounds above are at most $2s^2<2s^2+2s-4$.
In the exceptional bound equality requires $c=3$, hence
$s\equiv1\pmod3$. Fixing $c=3$ and the order forces the displayed
invariant factors, so it also fixes the isomorphism type. Conversely,
the construction in [@cor-global] with $p=3$ attains that order. This also extends Theorem 1.8 to arbitrary pairs:
the odd-$c$ residue bounds imply all its stated upper bounds, while
[@cor-even] treats even $c$.
:::
