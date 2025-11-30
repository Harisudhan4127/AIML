x = input()
h = int(x[:2])
m = x[2:]
if h > 12:
    if h > 21:
        print(f"{h-12}:{m} PM")
    else:
        print(f"0{h-12}:{m} PM")
else:
    if h == 0:
        print(f"{abs(h-12)}:{m} AM")
    else:
        print(f"{x[:2]}:{m} AM")