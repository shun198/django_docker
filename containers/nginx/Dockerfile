# FROM nginx

# COPY containers/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY containers/nginx/nginx.conf /etc/nginx/conf.d
