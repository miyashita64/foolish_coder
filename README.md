# foolish_coder
テストコードからソースコードを生成するツールのプロトタイプ。

## 実行環境
- Python3

## 必要パッケージ
- antlr4 (`$ pip3 install antlr4-python3-runtime`)
- numpy (`$ pip3 install numpy`)

## 使用手順
1. テストケースを追加する
1. `$ make generate` でソースコードを生成する
1. `$ make test` でテストにパスできないことを確認する
1. 生成されたソースコードをレビュー・リファクタリングする
1. `$ make approve` で自動生成&リファクタリングしたソースコードを保存する