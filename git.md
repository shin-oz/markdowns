# 第１回
なし


# 第２回
大まかな流れ
ファイルを作る・修正
ある程度のまとまりになったら履歴をデータベースに保存

- 作業ディレクトリ：ファイルの作成・修正
- ステージングエリア（インデックス）：ある程度のまとまりを保存前にまとめる
- リポジトリ：ローカルリポジトリ（作業はこっちでやる）・リモートリポジトリ（他の人とネットにて情報を管理）


# 第３回
今いるディレクトリでgitを利用する
git init

ステージングエリアにあげる
git add ~~

状況を確認
git status

リポジトリに追加
git Commit
（変更内容を記入）

コミット履歴を確認
git log

# 第４回・第５回
一行でコミット履歴を確認
git log --oneline

変更内容も確認
git log -p

どのファイルに変更が加えられたか九人
git log --stat


# 第６回
先ほどの情報を削除
git checkout -- index.html

# 第7回
どこが変更されているか確認→ステージングエリアに上がっていない情報を確認
git diff

どこが変更されているか確認→ステージングエリアに上がった情報を確認
git diff --cached


# 第８回
gitの管理下のファイルを管理下から外す→これをしないで削除すると、おかしくなっちゃう
git rm ~~


# 第９回
gitの管理下から外す
vim .gitignore
.gitignoreに記入

※置いているディレクトリ以下の管理下へ影響

# 第１０回
エディタを開かないでコミット
git commit -m "メッセージ"

直前のコミットを修正（直前コミットを上書きし、新たなコミットを作らないなし）
git commit --amend


# 第１１回
コミット状況を戻す
git reset --hard HEAD (HEADは直前)

# 第１２回
前回の情報を適用する
git reset --hard ORIG_HEAD (前回の内容だけはORIG_HEADに含まれている)

# 第１３回
※別々のバージョンで同時に修正するとき使用
ブランチ一覧をみる
git branch
新しいブランチを作成
git branch ~~
ブランチを移動
git branch checkout ~~


# 第１４回
別のブランチの内容を混ぜる
git merge ~~~
(※マージ先のブランチから、マージする内容を指定)
ブランチを削除
git branch -d ~~~

# 第１５回
ブランチを作成し、そのブランチへcheckout
git branch -b ~~~


# 第１６回
同じ箇所を別のブランチで変更し、マージすることで衝突が発生した場合
→自動で追加されコンフリクト場所の修正を実施


# 第１７回
タグつけ（git log時のIDをわかりやすくする）
直近のコミットにタグを追加
git tag ~~
直近より前にタグつけ
git tag 名前 ID(git log時のid)
タグを削除
git tag -d 名前


# 第１８回
エイリアス
checkut を　coでできるようにする
git config --global alias.co checkut
設定を確認
git config -l


# 第１９回
共有リポジトリを作成する
git init --bare
（※ここではコミット等は行わない）
共有リポジトリとして指定
git remote add origin ~~~
（~~~を共有リポジトリoriginとして登録）

# 第２０回
共有リポジトリへpush
git push origin master
（masterの内容をoriginへpush）


# 第２１回
Users/...をmyweb2としてcloneする
git clone /Users/shin-oz/2020_2021/ourweb.git myweb2

作成した内容をpush
git push origin master

remoteの内容をpull
git pull origin master


# 第２２回


