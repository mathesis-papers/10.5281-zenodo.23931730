# 精确陈述与证明

记 $G_k=\mathbb Z/2\mathbb Z\times\mathbb Z/(2k)\mathbb Z$，$k\ge1$。$s$-生成对是不同的 $a,b$，使每个 $g$ 都可写成 $xa+yb$，其中 $x,y\in\mathbb Z$ 且 $|x|+|y|\le s$。除非另有更强限制，下文均取 $s\ge1$。以下十一条结果保留原稿中定理、引理、推论共用的原编号。证明依据 Haobo Ma 与 Wenlin Zhang 的第 2 版论文，[DOI:10.5281/zenodo.23931731](https://doi.org/10.5281/zenodo.23931731)。

对一个 $s$-生成对，定义加法满射 $f:\mathbb Z^2\to G_k$ 为 $f(x,y)=xa+yb$，并记 $K=\ker f$，$T(u,v)=(u+v,u-v)$，$M=T^{-1}K$。模 $2G_k$ 约化后，$(\mathbb Z/2\mathbb Z)^2$ 到 $G_k/2G_k$ 的满射两边都含四个元素，因而为双射，故 $K\subseteq2\mathbb Z^2$。选取 $f(z)=(1,0)$，则 $2z\in K$；若 $K\subseteq4\mathbb Z^2$，便有 $z\in2\mathbb Z^2$，与 $f(z)$ 的第一坐标矛盾。因此 $K\not\subseteq4\mathbb Z^2$。$T$ 的像由坐标同奇偶的整数向量组成，指数为 $2$，且包含 $K$，所以 $T(M)=K$，$[\mathbb Z^2:M]=2k$。$M$ 中每个向量的坐标和为偶数。这些事实是下面引理的共同准备，而非对动作额外施加的假设。

## 定理 1：猜想 4.1 的分类

::: {.theorem #thm-classification title="猜想 4.1 的分类" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s1" lean="D5/S3/FiniteGroups/BajnokBeattyAllRegimes.result"}
对正整数 $k,s$，$G_k$ 存在 $s$-生成对，当且仅当下列条件之一成立：

1. $s$ 为奇数且 $2k\le s^2-1$。
2. $s$ 为偶数且 $2k\le s^2-s$。
3. $s\equiv0\pmod4$，$k$ 为偶数，且 $s^2-s<2k\le s^2$。
4. $s\equiv2\pmod4$，$k\equiv2\pmod4$，且 $s^2-s<2k\le s^2$。
:::

::: {.proof #pf-thm-classification}
由 [@lem-square]，总有 $2k\le s^2$。若 $s$ 为奇数，$2k$ 为偶数，故 $2k\le s^2-1$；反向由 [@lem-lower]。若 $s=2t$ 为偶数，较低范围也由 [@lem-lower] 处理。在剩余区间设 $r=2t^2-k$，则 $0\le r<t$。[@lem-congruences] 给出 $r$ 为偶数，且当 $t$ 为奇数时 $4\mid r$。$t$ 为偶数时，这等价于 $k$ 为偶数；$t$ 为奇数时，这等价于 $k\equiv2\pmod4$。反之，这些同余条件使 $r=2j$，其中 $0\le2j<t$，且 $t$ 或 $j$ 为偶数。于是 $k=2(t^2-j)$，由 [@lem-family] 得到所需生成对。
:::

## 引理 2：正方形覆盖

::: {.lemma #lem-square title="正方形覆盖" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s2" status="written-proof" proof="pf-lem-square" doi="10.5281/zenodo.23931731" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/131"}
若 $f$ 将整数菱形 $|x|+|y|\le s$ 映满 $G_k$，则 $M$ 的每个陪集都在 $\{0,\ldots,s-1\}^2$ 内有代表。特别地，$2k\le s^2$。
:::

::: {.proof #pf-lem-square}
先设 $s=2t$。给定 $z\in\mathbb Z^2$，令 $v=T(z-(t,t))+(1,0)$，并选择 $f(w)=f(v)$ 且 $\lVert w\rVert_1\le2t$ 的 $w$。因为 $w-v\in K\subseteq2\mathbb Z^2$，$w_1+w_2$ 与 $w_1-w_2$ 都为奇数，其绝对值至多 $2t-1$。因此

$$
q=\left(\frac{w_1+w_2-1}{2},\frac{w_1-w_2-1}{2}\right)
$$

属于 $\{-t,\ldots,t-1\}^2$。由 $w=T(q)+(1,0)$，有 $z-(q+(t,t))\in M$，所以 $q+(t,t)$ 就是所需代表。

若 $s=2t+1$，改取 $v=T(z-(t,t))$。此时 $w_1+w_2,w_1-w_2$ 都为偶数，绝对值至多 $2t$。令 $q=((w_1+w_2)/2,(w_1-w_2)/2)$，则 $q\in\{-t,\ldots,t\}^2$，同样相减得到代表。正方形有 $s^2$ 个点，而陪集数为 $2k$，故得上界。
:::

## 引理 3：近正方形刚性

::: {.lemma #lem-rigidity title="近正方形刚性" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s3" lean="D5/S3/FiniteGroups/NearSquareLatticeRigidity.near_square_rigidity"}
设 $n\ge2$，$0\le\delta<n$，且 $[\mathbb Z^2:L]=n^2-\delta$。若 $L$ 的每个陪集都与 $\{0,\ldots,n-1\}^2$ 相交，则存在 $0\le A,B<n$ 及 $\epsilon\in\{1,-1\}$，使得

$$
AB=\delta,
$$
$$
L=\mathbb Z(n,-\epsilon B)+\mathbb Z(-A,\epsilon n).
$$
:::

::: {.proof #pf-lem-rigidity}
令 $d=n^2-\delta$，则 $d>n(n-1)$ 且 $2d>n^2$。对每个 $0\le y<n$，覆盖 $(n,y)$ 得到某个 $(p,q)\in L$，满足

$$
1\le p\le n,\quad -(n-1)\le q\le n-1,
$$
$$
0\le y-q<n.
$$

若存在 $(p,0)\in L$，其中 $1\le p\le n$，覆盖 $(0,n)$ 又得到 $(-x,n-z)\in L$，$0\le x,z<n$。行列式 $p(n-z)$ 是 $d$ 的正整数倍，且不超过 $n^2<2d$，故等于 $d$。若 $p<n$ 或 $z>0$，其值至多 $n(n-1)$，矛盾。因此 $p=n,z=0,\delta=0$。取 $(n,0),(-x,n)$ 就得到结论，此时 $A=x,B=0,\epsilon=1$。

否则不存在上述水平向量。取最小的正整数 $b,c$，使得存在 $(p,-b),(r,c)\in L$，其中 $1\le p,r\le n$。将前面的列覆盖分别用于 $y=0,n-1$，可知二者存在且 $b,c<n$。任意 $y$ 对应的 $q$ 必满足 $q\le-b$ 或 $q\ge c$，所以必须有 $y\le n-1-b$ 或 $y\ge c$。这些整数区间不能留下空缺，故 $b+c\le n$。现在

$$
0<pc+rb\le n(b+c)\le n^2<2d.
$$

它是 $d$ 的倍数，因此等于 $d$。若 $b+c<n$，或 $p,r$ 都小于 $n$，则至多为 $n(n-1)$，矛盾。故 $b+c=n$，且 $p=n$ 或 $r=n$。

若 $p=n$，取 $(n,-b)$ 与 $(r,c)-(n,-b)=(-(n-r),n)$，令 $A=n-r,B=b,\epsilon=1$。若 $r=n$，取 $(n,c)$ 与 $(p,-b)-(n,c)=(-(n-p),-n)$，令 $A=n-p,B=c,\epsilon=-1$。两种情形的行列式绝对值均为 $d=n^2-AB$，故 $AB=\delta$。两向量属于 $L$ 且生成子格的指数等于 $L$ 的指数，所以生成整个 $L$。
:::

## 引理 4：必要同余条件

::: {.lemma #lem-congruences title="必要同余条件" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s4" lean="D5/S3/FiniteGroups/BajnokBeattyCayleyNecessity.top_strip_necessity"}
若 $s=2t$、$k=2t^2-r$ 且 $0\le r<t$，则 $G_k$ 中任何 $s$-生成对都满足 $2\mid r$；当 $t$ 为奇数时，还满足 $4\mid r$。
:::

::: {.proof #pf-lem-congruences}
将 [@lem-square] 与 [@lem-rigidity] 用于 $M$，取 $n=2t,\delta=2r$；因 $2r<2t$，假设满足。得到基 $(2t,-\epsilon B),(-A,\epsilon2t)$ 且 $AB=2r$。$M$ 内向量的坐标和为偶数，所以 $A=2u,B=2v$，其中 $u,v\ge0$，从而 $r=2uv$ 为偶数。

若 $t$ 为奇数且 $4\nmid r$，则 $u,v$ 都为奇数。对两基向量应用 $T$，分别得到

$$
2(t-\epsilon v,t+\epsilon v),
$$
$$
2(-u+\epsilon t,-u-\epsilon t).
$$

它们都在 $4\mathbb Z^2$ 中，又生成 $T(M)=K$，与 $K\not\subseteq4\mathbb Z^2$ 矛盾。
:::

## 引理 5：一个充分构造族

::: {.lemma #lem-family title="一个充分构造族" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s5" lean="D5/S3/FiniteGroups/BajnokBeattyCayleySufficiency.result"}
设 $t\ge1$，$0\le j<t$。若 $t$ 为偶数或 $j$ 为偶数，则群 $\mathbb Z/2\mathbb Z\times\mathbb Z/(4(t^2-j))\mathbb Z$ 存在 $2t$-生成对。
:::

::: {.proof #pf-lem-family}
令 $L$ 由

$$
V=(2(t-j),-2(t+j)),
$$
$$
W=(2(t-1),2(t+1))
$$

生成。行列式绝对值为 $8(t^2-j)$，四个坐标的最大公因数为 $2$：除以 $2$ 后的公因数整除 $t-1,t+1$，故整除 $2$；而 $t$ 为偶数时已有奇数坐标，$t$ 为奇数且 $j$ 为偶数时 $t-j$ 为奇数。因此 Smith 标准形的第一不变因子为 $2$，第二个为行列式除以 $2$，所以

$$
\mathbb Z^2/L\simeq\mathbb Z/2\mathbb Z\times\mathbb Z/(4(t^2-j))\mathbb Z.
$$

还需证明覆盖。变换后 $T(W)=(4t,-4)=U$，$T(V)=(-4j,4t)=V'$。当 $t>1$ 时，$U+V'$ 的两个坐标都为正。因此对任意 $z\in\mathbb Z^2$，$T(z)+(2t,2t)$ 模 $\mathbb ZU+\mathbb ZV'$ 的陪集存在非负代表。选取坐标和最小的非负代表 $(X,Y)$。若 $X\ge4t$，减去 $U$ 仍非负，且坐标和减少 $4(t-1)>0$；若 $Y\ge4t$，减去 $V'$ 同样使坐标和减少 $4(t-j)>0$。所以 $0\le X,Y<4t$。当 $t=1$ 时必有 $j=0$，先用 $U=(4,-4)$ 再用 $V'=(0,4)$ 作整数除法，也得到同一个范围。

减去 $(2t,2t)$ 后得到某个 $T(w)$，其中 $w\in z+L$，而 $T(w)$ 的两个坐标都在 $[-2t,2t-1]$。由

$$
|w_1|+|w_2|=\max\{|w_1+w_2|,|w_1-w_2|\}
$$

得系数范数至多 $2t$。最后 $L\subseteq2\mathbb Z^2$，故 $(1,0),(0,1)$ 的像不同；将它们沿上述同构送到目标群便得到生成对。
:::

## 引理 6：较低范围

::: {.lemma #lem-lower title="较低范围" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s6" status="written-proof" proof="pf-lem-lower" doi="10.5281/zenodo.23931731" source="Lemma 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/132"}
若 $s$ 为奇数且 $2k\le s^2-1$，或 $s$ 为偶数且 $2k\le s^2-s$，则 $G_k$ 存在 $s$-生成对。
:::

::: {.proof #pf-lem-lower}
先证明一个整数表示：对 $t\ge0$，$\mathbb Z/2\mathbb Z\times\mathbb Z$ 中的 $(1,t),(1,t+1)$ 能用系数范数至多 $2t+1$ 表示所有 $|z|\le2t(t+1)$ 的 $(\eta,z)$。

当 $\eta=0$，写

$$
z=(2t+1)q+w,\quad -t\le w\le t,
$$
$$
q=\left\lfloor\frac{z+t}{2t+1}\right\rfloor.
$$

由 $z$ 的界有 $-t\le q\le t$。取 $x=q-w,y=q+w$，则 $x+y$ 为偶数，$tx+(t+1)y=z$，且 $|x|+|y|=2\max(|q|,|w|)\le2t$。

当 $\eta=1$，写 $z=(2t+1)q+u$，$0\le u\le2t$，于是 $-t-1\le q\le t$。取

$$
x=q+1-u+t,\qquad y=q+u-t.
$$

此时 $x+y=2q+1$ 为奇数，$tx+(t+1)y=z$，且 $x-y=2t+1-2u$。由和差范数恒等式，$|x|+|y|\le2t+1$。当 $s=2t+1$，选取第二坐标的整数代表 $|z|\le k\le2t(t+1)$，再模 $2k$ 约化即得结论。两个动作的第二坐标相差 $1$，因此不同。

当 $s=2t$，取 $(1,t-1),(1,t)$。上面的构造用参数 $t-1$ 可在至多 $2t-1$ 步内覆盖 $|z|\le B=2t(t-1)$ 的两种第一坐标。三个区间 $ct+[-B,B]$，$c=-1,0,1$，覆盖 $[-B-t,B+t]$，因为 $t\le2B+1$；该不等式在 $t=1$ 成立，$t>1$ 时由 $(t-1)(4t-1)\ge0$ 得到。选择 $c$ 使 $|z-ct|\le B$，先表示 $(\eta-c,z-ct)$，再加上 $c(1,t)$，总步数至多 $2t$。因 $k\le B+t=2t^2-t$，模 $2k$ 约化完成证明。两个动作仍然不同。
:::

## 推论 7：固定群族中的最大阶

::: {.corollary #cor-family-max title="固定群族中的最大阶" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s7" status="written-proof" proof="pf-cor-family-max" doi="10.5281/zenodo.23931731" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/133"}
在存在 $s$-生成对的群 $G_k$ 中，偶数 $s\ge2$ 时的最大阶为 $2s^2$，奇数 $s\ge3$ 时为 $2s^2-2$。$s=1$ 时没有这样的群。
:::

::: {.proof #pf-cor-family-max}
群的阶为 $4k$。奇数 $s\ge3$ 时取 $2k=s^2-1$。偶数 $s$ 时取 $k=s^2/2$：若 $s\equiv0\pmod4$ 则 $k$ 为偶数；若 $s\equiv2\pmod4$ 则 $k\equiv2\pmod4$。这些值由 [@thm-classification] 实现；上界及 $s=1$ 的不可能性也由同一定理得到。
:::

## 推论 8：偶数第一不变因子

::: {.corollary #cor-even title="偶数第一不变因子" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s8" status="written-proof" proof="pf-cor-even" doi="10.5281/zenodo.23931731" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/134"}
设 $c\ge2$ 为偶数，$k,s\ge1$。若 $G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$ 存在 $s$-生成对，则 $|G|\le2s^2$。等号成立必须有 $c\mid s$。特别地，当 $s$ 为奇数时，$|G|\le2s^2-2$。
:::

::: {.proof #pf-cor-even}
令 $f:\mathbb Z^2\to G$ 为生成对诱导的满射，$K=\ker f$。诱导满射 $(\mathbb Z/c\mathbb Z)^2\to G/cG$ 的两边都有 $c^2$ 个元素，因此为双射，故 $K\subseteq c\mathbb Z^2\subseteq2\mathbb Z^2$。令 $M=T^{-1}K$，则 $T(M)=K$ 且 $[\mathbb Z^2:M]=|G|/2$。[@lem-square] 的覆盖论证只用到 $K\subseteq2\mathbb Z^2$，所以仍给出 $|G|/2\le s^2$。

若等号成立，因 $|G|\ge c^2\ge4$，有 $s\ge2$。在 [@lem-rigidity] 中取 $n=s,\delta=0$，得到 $AB=0$。若 $B=0$，第一基向量经 $T$ 变为 $(s,s)\in K$；若 $A=0$，第二基向量经 $T$ 变为 $(\epsilon s,-\epsilon s)\in K$。因 $K\subseteq c\mathbb Z^2$，两者都强制 $c\mid s$。奇数 $s$ 不可能满足等号；又 $4\mid|G|$，故上界可降为 $2s^2-2$。
:::

## 引理 9：奇数第一不变因子

::: {.lemma #lem-odd title="奇数第一不变因子" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s9" status="written-proof" proof="pf-lem-odd" doi="10.5281/zenodo.23931731" source="Lemma 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/135"}
设 $c\ge3$ 为奇数，写 $s=ct+r$，其中 $0\le r<c$。若 $G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$ 存在 $s$-生成对，则 $k\le F_c(s)$。令 $h=(c-1)/2$，定义

$$
F_c(s)=\begin{cases}
2t^2,&0\le r<h,\\
2t(t+1),&h\le r<c-1,\\
2t(t+1)+1,&r=c-1.
\end{cases}
$$

不要求生成对具有特殊形式。
:::

::: {.proof #pf-lem-odd}
同上设 $K=\ker f$，则 $K\subseteq c\mathbb Z^2$。同一群元素的所有代表都有相同的模 $c$ 系数余数。$c^2$ 个系数余数类分别对应 $cG$ 的陪集，每个有 $k$ 个元素，所以菱形内每个系数余数类至少有 $k$ 个点。

令 $U=x+y,V=x-y$。$c$ 为奇数，故该变换模 $c$ 可逆；在整数上，它把菱形对应到 $|U|,|V|\le s$ 且 $U\equiv V\pmod2$ 的点。记 $E_i,O_i$ 为余数 $i$ 在 $[-s,s]$ 内的偶数、奇数代表数。指定 $U,V$ 的余数为 $i,j$ 后，点数为 $E_iE_j+O_iO_j$。

取 $i=s+1\pmod c$，代表为 $s+1-\ell c$，其中 $1\le\ell\le\lfloor(2s+1)/c\rfloor$，奇偶交替。若 $r<(c-1)/2$，共有 $2t$ 个代表，故 $E_i=O_i=t$。取 $j=i$，得到 $2t^2$ 个点。

若 $(c-1)/2\le r<c-1$，$i=s+1$ 与 $j=s+2$ 各有 $2t+1$ 个代表；后者的数目为 $\lfloor(2s+2)/c\rfloor=2t+1$。首个代表的奇偶性相反，故计数分别为 $(t,t+1),(t+1,t)$，得到 $2t(t+1)$ 个点。

若 $r=c-1$，再次取 $j=i$。共有 $2t+1$ 个代表，得到 $t^2+(t+1)^2=2t(t+1)+1$ 个点。每种情形的 $k$ 都不超过选定类别的点数。论证包含 $t=0$，没有对生成对形状增加假设。
:::

## 推论 10：非循环群的最大阶

::: {.corollary #cor-global title="非循环群的最大阶" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s10" lean="D5/S3/FiniteGroups/BajnokBeattySharpMaximum.sharp_maximum"}
对 $s\ge3$，存在 $s$-生成对的非循环有限交换群的最大阶 $N(s)$ 满足：

$$
N(s)=2s^2\quad\text{若 }2s+1\text{ 为素数};
$$
若 $2s+1$ 为合数，则

$$
N(s)=2s^2+2s-\frac{p^2-1}{2}.
$$

其中第二种情形的 $p$ 是 $2s+1$ 的最小素因子。
:::

::: {.proof #pf-cor-global}
由有限交换群结构定理，二生成元非循环群可写成 $G=\mathbb Z/c\mathbb Z\times\mathbb Z/(ck)\mathbb Z$，$c\ge2$。偶数 $c$ 由 [@cor-even] 给出 $|G|\le2s^2$。奇数 $c$ 用 [@lem-odd]。第一段有 $c^2F_c(s)=2c^2t^2\le2s^2$。中间一段有

$$
c^2F_c(s)-2s^2=2ct(c-2r)-2r^2.
$$

若 $r>(c-1)/2$，此式为负；若 $r=(c-1)/2$，则

$$
|G|\le2s^2+2s-\frac{c^2-1}{2},\qquad c\mid2s+1.
$$

最后一段的差为

$$
-2ct(c-2)-c^2+4c-2<0.
$$

$c\ge5$ 时常数项已为负；$c=3,r=2$ 时因 $s\ge3$ 而 $t\ge1$，差为 $1-6t<0$。

若 $2s+1$ 为素数，特殊中间情形的唯一可能因子 $c\ge3$ 是 $c=2s+1$；此时 $t=0,F_c(s)=0$，与 $k\ge1$ 矛盾。所以阶至多 $2s^2$。若为合数，特殊情形的每个 $c\ge p$，故得到所述上界。这个上界严格大于 $2s^2$：写 $2s+1=pq$，$q\ge p$，超出量为

$$
pq-1-\frac{p^2-1}{2}\ge\frac{p^2-1}{2}>0.
$$

达到上界的构造来自 Bajnok–Beatty 的[定理 1.7、命题 2.3、推论 2.5](https://arxiv.org/abs/2406.04045v1)：$\mathbb Z/s\mathbb Z\times\mathbb Z/(2s)\mathbb Z$ 达到 $2s^2$。合数情形令 $q=(2s+1)/p$，$t=(q-1)/2\ge1$。由他们的定理 2.4，群 $\mathbb Z/p\mathbb Z\times\mathbb Z/(2pt(t+1))\mathbb Z$ 中的 $(1,t),(1,t+1)$ 为 $s$-生成对，阶恰为 $2s^2+2s-(p^2-1)/2$。这些群均非循环，且所选动作不同。
:::

## 推论 11：统一上界及等号情形

::: {.corollary #cor-universal title="统一上界及等号情形" mathesis="collected:bajnok-beatty-original-conjecture-4-1:2:s11" status="written-proof" proof="pf-cor-universal" doi="10.5281/zenodo.23931731" source="Corollary 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/136"}
对 $s\ge3$，任何存在 $s$-生成对的非循环有限交换群的阶都不超过 $2s^2+2s-4$。等号成立当且仅当 $s\equiv1\pmod3$，且群同构于

$$
\mathbb Z/3\mathbb Z\times\mathbb Z/((2s^2+2s-4)/3)\mathbb Z.
$$
:::

::: {.proof #pf-cor-universal}
前面所有非特殊情形的上界均至多 $2s^2<2s^2+2s-4$。特殊上界为 $2s^2+2s-(c^2-1)/2$；要达到 $2s^2+2s-4$，必须有 $c=3$，从而 $s\equiv1\pmod3$。群的不变因子于是被阶唯一确定为所述形式。反之，在这个同余类内，[@cor-global] 的构造取 $p=3$ 就达到该阶。论证不要求生成对为 $(1,u),(1,v)$ 的形式，因此给出了 Bajnok–Beatty 定理 3.3 去掉这一限制后的结果。
:::
