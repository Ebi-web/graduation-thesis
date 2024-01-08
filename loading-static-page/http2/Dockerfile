FROM nginx:alpine
COPY ./http2/html /usr/share/nginx/html
COPY ./assets/photos /usr/share/nginx/html/photos
COPY ./http2/conf/nginx.conf /etc/nginx/nginx.conf
COPY ./openssl /etc/nginx/ssl