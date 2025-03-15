
# python password.py
# https://withcation.com/2020/10/20/post-1491
# パスワード設定の数について

with open("sample.txt", mode = "w") as f:
    for i in range(5): # 最上桁
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        for n in range(5): # 最下桁
                            f.write(f"{i}{j}{k}{l}{m}{n}\n")
