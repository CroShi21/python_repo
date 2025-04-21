print("電子レンジの加熱時間計算！")
print("電子レンジの加熱時間（秒）= 記載されたW / 電子レンジのW * 記載された加熱時間（秒）")

print("記載されたワット:")
kisai_w = input()
print("電子レンジのワット:")
renzi_w = input()
print("記載された加熱時間（秒）:")
kisai_sec = input()

kekka = int(kisai_w) / int(renzi_w) * int(kisai_sec)
kekka_minu = kekka - 60
print(f"電子レンジの加熱時間（秒）:{round(kekka)}秒")
print(f"電子レンジの加熱時間（分,秒）:1分{round(kekka_minu)}秒")