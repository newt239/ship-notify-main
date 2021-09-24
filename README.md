# ship-notify-main

Dockerをベースに``ship-notify-public``リポジトリを一から作り直すリポジトリ。ライブラリ``py-cord``のv2.0リリース後対応し、順次以降予定

## setup
```
docker build -t "ship-notify" .
docker run -it "ship-notify"
```
## deploy
```
git add .
git commit -m "commit message"
git push heroku master
```
## todo

- 環境変数の設定(dockerだから普通と違いそう)
- dynoの管理など(とりあえず停止→ ``heroku ps:scale web=0`` )
- py-cord 2.0のリリース待ち
- https://devcenter.heroku.com/ja/articles/build-docker-images-heroku-yml