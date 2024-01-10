def knapsack(bids, m):
    """
    動的計画法を用いてナップサック問題を解く関数
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
    VCGメカニズムによる支払い額を計算する関数
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



bids = list(map(int, input().split()))
m = int(input())

# ナップサック問題の解法とVCGメカニズムによる支払い額の計算
total_value, allocation = knapsack(bids, m)
payments = calculate_payments(bids, m, allocation)

# 結果の表示
print(f"入札額: {bids}")
print(f"出品数: {m}")
print(f"最大入札額の総和: {total_value}")
print(f"割当て: {allocation}")
print(f"支払額: {payments}")