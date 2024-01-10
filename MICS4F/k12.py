import random
import time

def knapsack(bids, m):
    """
    動的計画法を用いてナップサック問題を解く関数。
    bids: 入札額のリスト
    m: 出品数

    戻り値: 最大の入札額の総和とそれに対応する割当て
    """
    n = len(bids)
    # V[k][l]は、最初のk人の入札者とl個の財に対する最大入札額の総和を表す
    V = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # 動的計画法による表の計算
    for k in range(1, n + 1):
        for l in range(1, m + 1):
            V[k][l] = V[k - 1][l]
            for z in range(1, l + 1):
                V[k][l] = max(V[k][l], V[k - 1][l - z] + bids[k - 1] * z)

    # 割当ての復元
    allocation = [0] * n
    remaining = m
    for k in range(n, 0, -1):
        if V[k][remaining] != V[k - 1][remaining]:
            # 入札者kに財が割り当てられている場合
            for z in range(1, remaining + 1):
                if V[k][remaining] == V[k - 1][remaining - z] + bids[k - 1] * z:
                    allocation[k - 1] = z
                    remaining -= z
                    break

    return V[n][m], allocation

def calculate_payments(bids, m, allocation):
    """
    VCGメカニズムによる支払い額を計算する関数。
    bids: 入札額のリスト
    m: 出品数
    allocation: 全員が参加した場合の割当て

    戻り値: 各買い手の支払い額のリスト
    """
    n = len(bids)
    payments = [0] * n

    for j in range(n):
        # 買い手jを除いた場合のナップサック問題の解を求める
        total_value_without_j, allocation_without_j = knapsack(bids[:j] + bids[j + 1:], m)

        # 買い手jの支払い額を計算
        payment_j = total_value_without_j
        for i in range(n):
            if i != j:
                payment_j -= bids[i] * allocation[i]
        payments[j] = payment_j

    return payments

def generate_problem(num_bidders, num_goods):
    """
    与えられた入札者数と財の個数に基づいて問題を生成する関数。
    入札額は10から100の間でランダムに選ばれる。

    num_bidders: 入札者数
    num_goods: 財の個数
    """
    return [random.randint(10, 100) for _ in range(num_bidders)], num_goods

def measure_performance(num_bidders, num_goods, num_trials=10):
    """
    指定された入札者数と財の個数に対して、問題を生成し、割当てと支払い額の計算の平均計算時間と支払い額の総和の平均を測定する関数。

    num_bidders: 入札者数
    num_goods: 財の個数
    num_trials: 試行回数（デフォルトは10）
    """
    total_time = 0
    total_payment_sum = 0

    for _ in range(num_trials):
        bids, m = generate_problem(num_bidders, num_goods)

        start_time = time.time()
        total_value, allocation = knapsack(bids, m)
        payments = calculate_payments(bids, m, allocation)
        end_time = time.time()

        total_time += end_time - start_time
        total_payment_sum += sum(payments)

    average_time = total_time / num_trials
    average_payment_sum = total_payment_sum / num_trials

    return average_time, average_payment_sum

# 入札者数と財の個数の組み合わせを設定
combinations = [(50, 30), (50, 50), (100, 30), (100, 50), (200, 30), (200, 50)]

# 各組み合わせに対する平均計算時間と支払い額の総和の平均を測定
results = {}
for num_bidders, num_goods in combinations:
    avg_time, avg_payment_sum = measure_performance(num_bidders, num_goods)
    print(f"入札者数:{num_bidders}", f" 財の個数:{num_goods}", f" 平均計算時間:{avg_time}", f" 支払額総和平均:{avg_payment_sum}")
    results[(num_bidders, num_goods)] = (avg_time, avg_payment_sum)

print(results)