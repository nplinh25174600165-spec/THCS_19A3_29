n = int(input("Nhập số cần kiểm tra: "))
    i = 0
    while i * i <= n:
        if i * i == n:
            print(n, "là số chính phương")
            return
        i += 1
    print(n, "không phải số chính phương")