keo = int(input("Nhập tổng số kẹo: "))
hocsinh = int(input("Nhập số học sinh: "))
moi_hs = keo // hocsinh
thua = keo % hocsinh
print("Mỗi học sinh nhận:", moi_hs)
print("Số kẹo thừa:", thua)