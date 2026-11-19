# 范围、证据与文献

## 已证明什么，边界在哪里？

[分类定理](statements.md#thm-classification)对所有正整数 $k,s$ 解决猜想 4.1。[最大阶公式](statements.md#cor-global)对 $s\ge3$ 解决猜想 1.6，上界适用于任意生成对。[统一上界](statements.md#cor-universal)还包含等号群的同构类型，从而去掉 Bajnok–Beatty 定理 3.3 原来的特殊形式假设。

小半径不能直接代入最大阶公式。$s=1$ 时，偶数 $c$ 的上界要求 $c^2\le2$，奇数 $c$ 的余数界则要求 $k=0$，都不可能给出非循环群。$s=2$ 时偶数 $c$ 的阶至多为 $8$，奇数 $c$ 只允许 $c=3,k=1$；标准生成对 $(1,0),(0,1)$ 在两步内覆盖 $\mathbb Z_3^2$，故 $N(2)=9$。

若菱形中每个系数点恰好对应一个不同群元素，就称为**完美**生成对，群的阶必为 $2s^2+2s+1$。$s\ge3$ 时这超过非循环群上界，因此群必为循环群。$s=2$ 时阶为 $13>9$，$s=1$ 时阶为素数 $5$，也都必须循环。

原稿还纠正了印刷版猜想 1.10 的一个定义域。$s=2$ 时，$\mathbb Z/13\mathbb Z$ 中的 $\{2,10\}$ 是完美的：

$$
0,\quad\pm2,\quad\pm10,\quad\pm4,
$$
$$
\pm20,\quad\pm12,\quad\pm8
$$

恰好给出十三个不同余数。它等于 $5\{2,3\}$，但乘数 $d=0,1,2,3,4$ 分别给出 $\{0\},\{2,3\},\{4,6\},\{6,9\},\{8,12\}$，没有一个是 $\{2,10\}$。因此乘数应在模 $2s^2+2s+1$ 的可逆元中取值，而非模 $2s+1$ 的余数中取值。**本文没有证明纠正后的完整二生成元形状断言**。循环性、这个明确反例与纠正后的形状断言是不同命题。

原稿也说明单生成元及半径一的初等完美生成集边界。三个及更多生成元的问题，以及原稿引用的高维 Lee 球文献，不属于这里的二维证明。受限无符号基使用的系数集合也不同。

## 精确形式化证据与贡献入口

以下链接直接指向本书所选提交的 Lean 源码。对应关系以具体数学命题为单位，不把整篇论文作为一个验证单位。

| 原稿结果 | 对应形式化源码 |
|---|---|
| 定理 1：四种情形的完整分类 | [全部范围](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyAllRegimes.lean#L339) |
| 引理 3：格子基及亏损乘积 | [近正方形刚性](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/NearSquareLatticeRigidity.lean#L231) |
| 引理 4：任意生成对的必要同余 | [较高区间的必要性](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyCayleyNecessity.lean#L305) |
| 引理 5：含端点的充分构造族 | [统一构造](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattyCayleySufficiency.lean#L265) |
| 推论 10：全体非循环群的上界及达到 | [精确最大值](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/FiniteGroups/BajnokBeattySharpMaximum.lean#L390) |

其余六条编号命题的原稿证明已在前章完整给出。共享请求区分已有形式证明的直接推论与仍需补充形式推理的更细结论：

- [所有正半径的正方形覆盖：合并已有覆盖与计数证明](https://github.com/the-omega-institute/trureturing-requests/issues/131)。
- [较低范围：抽取已有分类的推论](https://github.com/the-omega-institute/trureturing-requests/issues/132)。
- [固定群族的最大阶：由分类导出极值结论](https://github.com/the-omega-institute/trureturing-requests/issues/133)。
- [偶数第一不变因子：保留小半径及等号整除条件](https://github.com/the-omega-institute/trureturing-requests/issues/134)。
- [奇数第一不变因子：保留完整三段余数界](https://github.com/the-omega-institute/trureturing-requests/issues/135)。
- [统一上界：补齐等号同构类型分类](https://github.com/the-omega-institute/trureturing-requests/issues/136)。

贡献者可在这些规范请求下协调，从自己的 fork 向[上游 `dev`](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)提交聚焦的 PR。应复用已有分类及精确最大值。请求提供贡献入口，不把已有书面证明的问题改称数学开放问题，也不构成验证凭据。

## 文献与归属

- Haobo Ma 与 Wenlin Zhang，*Bajnok–Beatty Conjectures 4.1 and 1.6 (arXiv:2406.04045v1, Section 4, p. 10; Section 1, p. 3): classification and extremal noncyclic order*，第 2 版。[版本 DOI:10.5281/zenodo.23931731](https://doi.org/10.5281/zenodo.23931731)。[概念 DOI:10.5281/zenodo.23931730](https://doi.org/10.5281/zenodo.23931730) 标识跨版本作品。Haobo Ma 的机构为 Chrono AI，新加坡；Wenlin Zhang 的机构为新加坡国立大学及 Chrono AI，新加坡。原论文许可为 CC BY 4.0。
- B. Bajnok 与 W. K. Beatty，*On the Diameter of Undirected Cayley Graphs of Finite Abelian Groups*，[arXiv:2406.04045v1](https://arxiv.org/abs/2406.04045v1)，2024；发表于 *Combinatorics and Number Theory* **14** (2025)，1–12，[DOI:10.2140/cnt.2025.14.1](https://doi.org/10.2140/cnt.2025.14.1)。原始 v1 定位：猜想 4.1，§4，第 10 页；猜想 1.6，§1，第 3 页；猜想 1.10，§1，第 4 页。定理 4.2–4.4 提供已知范围；定理 1.7 及 §2 构造给出达到上界的例子。
- R. Dougherty 与 V. Faber，*The degree-diameter problem for several varieties of Cayley graphs, I: The Abelian case*，*SIAM Journal on Discrete Mathematics* **17** (2004)，478–519，[DOI:10.1137/S0895480100372899](https://doi.org/10.1137/S0895480100372899)。商格子表述见 [arXiv:math/9412223v2](https://arxiv.org/abs/math/9412223v2) 第 6 页命题 2。

几何主步骤采用商格子观点；精确最大值则把本文的余数计数上界与 Bajnok、Beatty 已有的达到构造结合。原始完整参考文献及高维结果的归属见[公开版本 PDF](https://zenodo.org/records/23931731/files/note-v2.pdf)，它们不是以上二维论证的额外前提。
