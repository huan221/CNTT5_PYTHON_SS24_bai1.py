# ===== PHÂN TÍCH LỖI =====

# 1. total_amount là thuộc tính public
# => Có thể bị sửa trực tiếp từ bên ngoài
# => Vi phạm tính đóng gói (Encapsulation)

# 2. Cần đổi total_amount thành __total_amount
# => Kích hoạt Name Mangling để bảo vệ dữ liệu

# 3. Dùng @property để cho phép đọc tổng tiền
# => Không cho phép gán trực tiếp

# 4. self.vat_rate = new_rate
# => Tạo instance attribute mới cho object hiện tại
# => Không thay đổi class attribute vat_rate

# 5. Cần dùng @classmethod và tham số cls
# => Cập nhật VAT cho toàn bộ đối tượng trong hệ thống

# fix code

class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate
            

# check output

order_table1 = CoffeeOrder('Bàn 1')
order_table2 = CoffeeOrder('Bàn 2')

order_table1.add_item(50000)
order_table2.add_item(30000)

try:
    order_table1.total_amount = 0
except AttributeError:
    print('Không thể sửa trực tiếp tổng tiền!')

CoffeeOrder.update_vat_rate(0.08)

print(order_table1.total_amount)
print(order_table2.total_amount)

print(order_table1.vat_rate)
print(order_table2.vat_rate)

print(order_table1.calculate_final_bill())
print(order_table2.calculate_final_bill())