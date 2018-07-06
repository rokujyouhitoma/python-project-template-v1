# 目的

Pythonのプロジェクトテンプレートを整備する。

# Requirements

 - Python3.6.5

# 開発ツール

## 暫定採用

 - isort
 - yapf
 - flake8
 - mypy
 - pytest

## 選定

TODO: 選定した際の理由を整理。

 - 静的型チェッカー
   - 目的：mypyの存在ありき。型チェクに頼りたい
   - 選定：mypy
   - 候補：mypy
 - コーディングスタイルチェッカー
   - 目的：コーディングスタイルのチェックを人手のレビューで行いたくないため
   - 選定：flake8
   - 候補：flake8、pycodestyle
 - ソースコードフォーマッター
   - 目的：ソースコードの整形を人任せにせず、機械任せにしたいため
   - 選定：yapf、isort
   - 候補：yapf、black、autopep8、isort
 - テストフレームワーク
   - 目的：標準のunittestより簡単にテストを書きたい
   - 選定：pytest
   - 候補：pytest
