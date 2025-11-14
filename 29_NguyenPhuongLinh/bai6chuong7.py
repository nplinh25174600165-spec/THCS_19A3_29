nam = int(input("Nhập năm: "))
if nam % 400 == 0:
    print("Năm nhuận")
elif nam % 4 == 0 and nam % 100 != 0:
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")