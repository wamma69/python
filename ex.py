# 한국돈을 입력하면 외국화폐로 환전계산.
import pickle

f = open("ttt.pic", "rb")
d = pickle.load(f)

# print(d)

x = float(input("바꿀 한국돈은 얼마인가요?"))

for a, b  in d.items():
    r = x / b
    print(a, r)
