# http3/Dockerfile
# HTTP/3をサポートするNginxのカスタムイメージを使用
FROM nginx-quic
COPY ./html /usr/share/nginx/html
COPY ./conf/nginx-quic.conf /etc/nginx/nginx.conf
COPY ../../openssl /etc/nginx/ssl
