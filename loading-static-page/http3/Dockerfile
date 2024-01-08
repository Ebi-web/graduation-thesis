# http3/Dockerfile
# HTTP/3をサポートするNginxのカスタムイメージを使用
FROM nginx-quic
COPY ./assets/html /usr/share/nginx/html
COPY ./assets/photos /usr/share/nginx/html/photos
COPY ./conf/nginx-quic.conf /etc/nginx/nginx.conf
COPY ./openssl /etc/nginx/ssl
