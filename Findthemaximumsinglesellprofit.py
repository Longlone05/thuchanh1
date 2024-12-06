n = list(map(int, input("Nhập giá cổ phiếu: ").split()))

def max_profit(stock_price):
    max_profit = 0  # Khởi tạo giá trị lợi nhuận tối đa ban đầu là rất nhỏ
    for i in range(1, len(stock_price)):
        profit = stock_price[i] - stock_price[i-1]  # Tính sự chênh lệch giữa số bên phải và số bên trái
        max_profit = max(max_profit, profit)  # Cập nhật lợi nhuận tối đa
    
    return max_profit

print("Lợi nhuận tối đa có thể đạt được:", max_profit(n))
