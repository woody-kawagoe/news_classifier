# Usage

(domain)/naive\_bayesにアクセスするとフォーム画面が表示される。
フォームにGunosyのニュースのURLを入力すると分類結果画面に遷移する。

# Packages

+ python 3.5.0
+ django 1.10.2
+ mecab 0.996
+ mecab-ipadic-neologd
+ python-mecab3 0.7

# View

## form フォーム画面
フォームにURLを入力で送信ボタンを押すと、URLをPOSTで送信する。
## result 結果画面
classifierから送信された分類結果を表示する。
## classifier 分類器
入力はformから送信されたURL。分類結果をresultに送る。

現在分類機能は未実装で、入力URLをそのままresultに送っている。
今後はclassifierを改良する。
