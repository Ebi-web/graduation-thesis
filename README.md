# graduation-thesis

## 環境構築

前提としてDockerとDocker Composeがインストールされている必要があります。
graduation-thesis以下の各ディレクトリで以下のコマンドを実行してください。

```bash
docker compose up -d
```

例えば静的ページのロードに関する性能比較を行う場合は以下のコマンドで環境構築ができます。

```bash
cd loading-static-page && docker compose up -d
```

また、HTTP/2とHTTP/3ではHTTPSを使用するため自己署名証明書の導入が必要です。
graduation-thesisで使用する証明書は以下のコマンドで生成できます。

```bash
mkdir openssl && cd openssl # certificates must be placed in the openssl directory
openssl genrsa 2048 > server.key
openssl req -new -key server.key > server.csr
openssl x509 -days 3650 -req -sha256 -signkey server.key < server.csr > server.crt
```

## docker versionの確認

```text     
Client:
 Cloud integration: v1.0.22
 Version:           20.10.12
 API version:       1.41
 Go version:        go1.16.12
 Git commit:        e91ed57
 Built:             Mon Dec 13 11:46:56 2021
 OS/Arch:           darwin/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.12
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.12
  Git commit:       459d0df
  Built:            Mon Dec 13 11:43:56 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.12
  GitCommit:        7b11cfaabd73bb80907dd23182b9347b4245eb5d
 runc:
  Version:          1.0.2
  GitCommit:        v1.0.2-0-g52b36a2
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## docker compose versionの確認

```text
Docker Compose version v2.2.3
```

## python versionの確認

```text
tools/html_generator配下にてPython 3.9を使用。
```

## Chrome versionの確認

```text
バージョン: 120.0.6099.129（Official Build） （x86_64）
```

## 著者のマシン

以下の画像は著者のマシンにおける「このMacについて」のスクリーンショットである。
<img width="475" alt="スクリーンショット 2024-01-20 14 03 21" src="https://github.com/Ebi-web/graduation-thesis/assets/74973675/377634ac-6e0c-4630-b61f-a5b326ece71c">
