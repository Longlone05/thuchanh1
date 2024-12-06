def max_profit(stock_prices):
    if not stock_prices or len(stock_prices) < 2:
        return 0  # Không thể có lợi nhuận nếu không đủ giá

    min_price = stock_prices[0]  # Giá mua thấp nhất ban đầu
    max_profit = 0  # Lợi nhuận tối đa ban đầu

    for price in stock_prices[1:]:
        profit = price - min_price  # Tính lợi nhuận nếu bán tại giá hiện tại
        max_profit = max(max_profit, profit)  # Cập nhật lợi nhuận tối đa nếu cần
        min_price = min(min_price, price)  # Cập nhật giá mua thấp nhất

    return max_profit

# Nhập giá cổ phiếu từ người dùng
n = list(map(int, input("Nhập giá cổ phiếu (cách nhau bởi dấu cách): ").split()))

# Hiển thị lợi nhuận tối đa
print("Lợi nhuận tối đa có thể đạt được:", max_profit(n))
