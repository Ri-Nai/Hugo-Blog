# 使用 Hugo 构建静态站点
FROM hugomods/hugo:std-exts-0.128.0 AS builder
WORKDIR /src
# 复制整个项目
COPY . .
# 构建静态文件（生成在 public 目录）
RUN hugo --minify --baseURL "https://ri-nai.github.io/Hugo-Blog/"

# 使用 Nginx 来托管静态文件
FROM nginx:stable-alpine
# 将构建产物复制到 Nginx 的 web 目录
COPY --from=builder /src/public /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
