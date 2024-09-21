# テストサーバを起動
# python -m http.server --cgi

import cgi
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# HTML文字列
html = '''
<!DOCTYPE html>
<html>
<head>
<title>CGI</title>
<meta charset="UTF-8">
</head>
<body>
{}
<hr>
{}
<hr>
{}
</body>
</html>
'''

# フォームから値を取得
name = "未入力"
email = "未入力"
errors = []

form = cgi.FieldStorage()

if "name" in form:
    name = form["name"].value
else:
    errors.append("お名前の入力がありません")

if "email" in form:
    email = form["email"].value
else:
    errors.append("メールアドレスの入力がありません")

result = "お名前：{}<br />".format(name)
result += "メールアドレス: {}".format(email)

# 結果を表示
print(html.format(
    "リクエストは {} です。".format(os.environ['REQUEST_METHOD']),
    result,
    "<br />".join(errors))
)
