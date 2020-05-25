# ・F - Silver Fox vs Monster
#前回と同じ問題、前回は累積和で解いたので今回はBIT(BinaryIndexedTree)で解いた
#TLEがあるがWAはないのでコード自体はおそらく正しい
from collections import deque
import bisect
 
class BIT:
    def __init__(self, n, d = None):
        self.n = n
        self.bit = [0] * (n + 1)
        if d == None:
            return
        for i in range(n):
            self.update(i, d[i])
 
    #値更新
    def update(self, i, x = 1):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)
 
    #区間合計値を出力            
    def query(self, i):
        i += 1
        res_sum = 0
        while i > 0:
            res_sum += self.bit[i]
            i -= i & -i
        return res_sum
    
N, D, A = list(map(int, input().split()))
pair_xh = [[-1, -1] for _ in range(N)] # 1回ずつしか使わないけどソートするから必要
for i in range(N):
    pair_xh[i][0], pair_xh[i][1] = list(map(int, input().split()))
pair_xh.sort(key = lambda x: x[0]) #座標でソート
 
# q_lim_d = deque() # 累積和に含まれる攻撃範囲とダメージを保存する場所
# total = 0 # 喰らいダメージの累積和
count = 0 # 攻撃回数
bit = BIT(N + 1)
 
for i in range(N):
    x = pair_xh[i][0]
    h = pair_xh[i][1]
    
    # while len(q_lim_d) and q_lim_d[-1][0] < x: # 範囲外になったら喰らわないから累積和から外す
    #     total -= q_lim_d[-1][1]
    #     q_lim_d.pop()
    # h -= total
    h -= bit.query(i)
    if h > 0: # 見てる敵の体力が0になる攻撃回数を求めその分を累積和に足す
        times = (h + A - 1) // A # 0にするのに必要な回数(切り上げ)
        count += times
        damage = A * times
        # total += damage
        # q_lim_d.appendleft([x + 2 * D, damage])
        bit.update(i, damage)
        rx = x + D * 2
        j = bisect.bisect_right(pair_xh, [rx + 1, -1])
        bit.update(j, -damage)
print(count)

