n = list(map(int, input("Nhập giá cổ phiếu: ").split()))

def max_profit(stock_price):
    maxP = 0 
    for i in range(len(stock_price)):
        for j in range(i + 1, len(stock_price)):
            profit = stock_price[j] - stock_price[i]  # Tính lợi nhuận
            if profit > maxP:
                maxP = profit
    return maxP
print("Lợi nhuận tối đa có thể đạt được:", max_profit(n))
