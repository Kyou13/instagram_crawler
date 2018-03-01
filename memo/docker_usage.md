# Dockerコマンド
- コンテナ起動
```
$ docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]
```
- コンテナのスタート、ストップ
```
$ docker container start [OPTIONS] CONTAINER [CONTAINER...]
$ docker container stop [OPTIONS] CONTAINER [CONTAINER...]
```
- コンテナのリストを表示・取得
```
$ docker container ls [OPTIONS]
```
- コンテナのログ確認
```
$ docker container logs [OPTIONS] CONTAINER
```
- コンテナの破棄
```
$ docker container rm [OPTIONS] CONTAINER [CONTAINER...]
```

### コンテナイメージの作成
- dockerイメージ一覧を取得
```
$ docker image ls ($ docker imagesと同義)
```

- コンテナんの一括削除
```
$ docker rm `docker ps -a -q`
```
