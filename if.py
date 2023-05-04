# 条件分岐
music = "Spring of Life"
print("春の曲といえば" + music + " 派\n")

if music == "Spring of Life":
    print("サプライズを待っていてもしょうがないから〜")
else:
    print("ワンルーム・ディスコ派ですか？")
print("ドライブはFAKE IT派です")

likePerfume = "気になる姫"
if likePerfume == "こどものっち":  # ここは一致を確かめるので==
    PerfumeLocks = "こどものっち"  # ここは代入なので=
elif likePerfume == "かしゆかおじさん":
    PerfumeLocks = "かしゆかおじさん"
else:
    PerfumeLocks = "気になる姫"
print("Perfume Locksといえば" + PerfumeLocks + "!!!\n")
# 比較演算子
msgA = int(len("マワルカガミ"))  # 6
msgB = int(len("コミュニケーション"))  # 9
print(bool(msgA == msgB))  # false
print(bool(msgA != msgB))  # true
print(bool(msgA <= msgB))  # true
print('\n')
# unicodeのコードポイント
print(ord("a"))  # 97
print(ord("B"))  # 66
# 要素が含まれる
array1 = ["レーザービーム", "スパイス", "いじわるなハロー"]
print(bool("スパイス" in array1))  # true
print(bool("ビーム" in array1))  # false
# 論理和・論理積・否定
print(bool(5 < msgA or 20 < msgA))  # true,一方がtrueならtrueを返す
print(bool(5 < msgA and 20 < msgA))  # false,一方がfalseならfalseを返す
print(bool(not 5 < msgA))  # 逆を返す
print("\n")
# オブジェクトが同一かどうか比較
array2 = ["レーザービーム", "スパイス", "いじわるなハロー"]
array3 = array2
print(array1 == array2)  # true
print(array1 is array2)  # オブジェクトが別々なのでfalse
print(array2 is array3)  # 同じオブジェクトを示しているのでtrue
print("\n")

# 固有のidを取得
print(id(array1))  # 4515128768
print(id(array2))  # 4515723456 → array1とは異なる
print(id(array3))  # 4515723456 → array2と同様
