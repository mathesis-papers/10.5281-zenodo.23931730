/* Deterministic scenes for the installed film engine. The animation illustrates
   coefficients and exact examples; theorem badges cite film.json's declarations. */
'use strict';
function sceneTitle(en, zh) {
  txt(en, 960, 212, {size:44, fam:F.disp, w:700, align:'center', c:C.white});
  txt(zh, 960, 266, {size:28, fam:F.zh, align:'center', c:C.dim});
}
function mathLabel(s,x,y,size=38,col=C.white) {
  txt(s,x,y,{size,fam:F.math,align:'center',c:col});
}
function coefficientPoints(cx,cy,unit,transform=0,alpha=1) {
  for(let x=-4;x<=4;x++) for(let y=-4;y<=4;y++) {
    if(Math.abs(x)+Math.abs(y)>4) continue;
    const u=(1-transform)*x+transform*(x+y);
    const v=(1-transform)*y+transform*(x-y);
    dot(cx+unit*u,cy-unit*v,7,'c',alpha);
  }
}
function axes(cx,cy,unit=57) {
  line(cx-4.6*unit,cy,cx+4.6*unit,cy,C.dim,0.45);
  line(cx,cy-4.6*unit,cx,cy+4.6*unit,C.dim,0.45);
}
SCENES.moves=S=>{
  badgeQ(S,[[0,null,'computed']]);
  sceneTitle('TWO MOVES, AT MOST TWO STEPS','两个动作，至多两步');
  panel(200,330,1520,490,1,C.cyan);
  const expressions=[['0','b','2b','−b'],['a − b','a','a + b','−a']];
  const costs=[[0,1,2,1],[2,1,2,1]];
  const budget=Math.min(2,Math.floor(3*at(S,1,3.5)));
  for(let row=0;row<2;row++) for(let col=0;col<4;col++) {
    const x=475+col*320,y=495+row*205;
    const visible=costs[row][col]<=budget;
    chip(x,y,260,120,expressions[row][col],visible?C.cyan:C.dim,visible?1:0.2,38,F.math);
    mathLabel(`(${row}, ${col})`,x,y+92,25,C.dim);
  }
  mathLabel('a = (1, 1)       b = (0, 1)       Z/2 × Z/4',960,365,29);
};
SCENES.diamond=S=>{
  badgeQ(S,[[0,null,'computed']]);
  sceneTitle('THE COEFFICIENT DIAMOND','系数菱形：先数走法，再识别重合');
  panel(150,320,780,510,1,C.cyan);
  axes(540,575,54);
  const radius=4*at(S,1,2.8);
  for(let x=-4;x<=4;x++) for(let y=-4;y<=4;y++) {
    const cost=Math.abs(x)+Math.abs(y);
    if(cost>4)continue;
    dot(540+x*54,575-y*54,7,'c',cost<=radius?1:0.16);
  }
  panel(990,320,780,510,1,C.cyan);
  mathLabel('|x| + |y| ≤ 4',1380,440,48);
  mathLabel('1 + 4(1 + 2 + 3 + 4) = 41',1380,540,32);
  const a=at(S,2,1.5);
  mathLabel('f(x, y) = xa + yb',1380,645,35);
  txt('SAME ENDPOINT = LATTICE RELATION',1380,735,{size:22,fam:F.disp,align:'center',c:C.cyan,a});
};
SCENES.transform=S=>{
  badgeQ(S,[[0,null,'computed']]);
  sceneTitle('ADD AND SUBTRACT THE COORDINATES','和差坐标：图形改变，奇偶性保留');
  panel(150,320,780,510,1,C.cyan);
  const q=at(S,0,4.5);
  axes(540,575,54);coefficientPoints(540,575,54,q);
  panel(990,320,780,510,1,C.cyan);
  mathLabel('U = x + y',1380,415,42);
  mathLabel('V = x − y',1380,475,42);
  mathLabel('|x| + |y| = max(|U|, |V|)',1380,555,32);
  mathLabel('U ≡ V (mod 2)',1380,625,36);
  txt('PARITY + TRANSLATION',1380,703,{size:25,fam:F.disp,align:'center',c:C.cyan,a:at(S,2,1)});
  mathLabel('2k classes ≤ 4² = 16',1380,765,34);
};
SCENES.rigidity=S=>{
  badgeQ(S,[[0,null,'lean']]);
  sceneTitle('ALMOST FULL SQUARES ARE RIGID','近乎装满的正方形，亏损必须是乘积');
  panel(150,320,780,510,1,C.cyan);
  for(let x=0;x<4;x++)for(let y=0;y<4;y++)dot(350+x*120,390+y*120,11,'c',1);
  txt('16 AVAILABLE REPRESENTATIVES',540,800,{size:23,fam:F.disp,align:'center',c:C.dim});
  panel(990,320,780,510,1,C.lean);
  mathLabel('index = n² − AB',1380,420,42);
  mathLabel('n = 4,  k = 7:   AB = 16 − 14 = 2',1380,510,30);
  mathLabel('A = 2u,   B = 2v',1380,610,38);
  mathLabel('AB = 4uv ≠ 2',1380,705,48,C.lean);
  txt('CONDITIONAL COVER ⇒ CONTRADICTION',1380,785,{size:21,fam:F.disp,align:'center',c:C.dim});
};
SCENES.construction=S=>{
  badgeQ(S,[[0,null,'lean']]);
  sceneTitle('ZERO DEFICIT, AND AN ACTUAL CONSTRUCTION','亏损为零之后，还需要真正的覆盖构造');
  panel(150,320,780,510,1,C.cyan);axes(540,575,40);
  coefficientPoints(540,575,40,0,0.6);
  const a=at(S,1,1.8);
  arrow(540,575,540+4*40,575+4*40,C.cyan,a,4);
  arrow(540,575,540+2*40,575-6*40,C.mag,a,4);
  mathLabel('V',760,770,32,C.cyan);mathLabel('W',650,340,32,C.mag);
  panel(990,320,780,510,1,C.lean);
  mathLabel('t = 2,   j = 0,   k = 8',1380,415,34);
  mathLabel('V = (4, −4)',1380,500,40);
  mathLabel('W = (2, 6)',1380,565,40);
  mathLabel('|det(V, W)| = 32',1380,650,36);
  mathLabel('Z² / ⟨V, W⟩ ≅ Z/2 × Z/16',1380,750,32);
};
SCENES.maximum=S=>{
  badgeQ(S,[[0,null,'lean']]);
  sceneTitle('OTHER GROUPS CHANGE THE MAXIMUM','改变群的形状，最大阶也会改变');
  panel(150,320,780,510,1,C.cyan);
  mathLabel('s = 3:   2s + 1 = 7',540,420,34);
  mathLabel('N(3) = 18',540,500,52);
  mathLabel('s = 4:   2s + 1 = 9,  p = 3',540,620,30);
  mathLabel('N(4) = 36',540,710,52);
  panel(990,320,780,510,1,C.lean);
  mathLabel('N(s) = 2s²   (2s + 1 prime)',1380,420,30);
  mathLabel('N(s) = 2s² + 2s − (p² − 1)/2',1380,505,28);
  txt('COMPOSITE CASE · s ≥ 3',1380,555,{size:23,fam:F.disp,align:'center',c:C.dim});
  txt('ATTAINING CONSTRUCTIONS',1380,650,{size:24,fam:F.disp,align:'center',c:C.cyan});
  txt('B. Bajnok · W. K. Beatty',1380,695,{size:28,fam:F.disp,align:'center',c:C.white});
  txt('Paper: Haobo Ma · Wenlin Zhang',1380,770,{size:25,fam:F.disp,align:'center',c:C.dim});
};
FILM.poster=()=>{
  ctx.fillStyle=C.bg; ctx.fillRect(0,0,W,H);
  sceneTitle('WHY 28 FAILS AND 32 WORKS','从菱形到正方形');
  panel(150,320,780,510,1,C.cyan);axes(540,575,54);coefficientPoints(540,575,54,0,1);
  panel(990,320,780,510,1,C.cyan);
  mathLabel('s = 4',1380,430,58);
  mathLabel('k = 7:  AB = 2',1380,535,44);
  mathLabel('A, B even  ⇒  impossible',1380,600,30);
  mathLabel('k = 8:  constructed',1380,710,42);
  txt('Haobo Ma · Wenlin Zhang',960,900,{size:28,fam:F.disp,align:'center',c:C.dim});
};
