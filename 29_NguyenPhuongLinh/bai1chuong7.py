gia = float(input("Nhập giá sản phẩm: "))
sl = int(input("Nhập số lượng: "))
tong = gia * sl
vat = tong * 0.10
tong_phai_tra = tong + vat
print("Tổng phải trả:", round(tong_phai_tra, 2))