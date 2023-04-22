# Docker image 打包與相關說明
分成兩個Container，Nginx與flask。分別為Proxy與AP的角色。相關Dockerfile如下

Nginx --> Docker-nginx/Dockerfile

flask --> Docker-flask/Dockerfile

主程式名稱為  app.py

如果需要在本機測試該程式執行是否可以正常運行可以使用下列六行指令

該指令需要安裝Docker CE

[下載鏈接](https://www.docker.com/products/docker-desktop) 需要註冊docker.com才能下載

```
docker build -t docker_nginx -f docker-nginx/Dockerfile . --no-cache
docker build -t docker_flask -f docker-flask/Dockerfile . --no-cache
```

docker run --name docker_nginx -p 80:80 -idt docker_nginx
docker run --net=container:docker_nginx --name docker_flask -idt docker_flask
執行之後即可使用本機 http://localhost/ 進行瀏覽