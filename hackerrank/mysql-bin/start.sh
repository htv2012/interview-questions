# https://infotechys.com/deploying-mysql-using-podman/
podman run                                       \
    --name mysql-container                       \
    -e MYSQL_ROOT_PASSWORD='LacLeoMeDongLo2025/' \
    -d                                           \
    -p 3306:3306                                 \
    -v /var/tmp/mysql:/var/lib/mysql             \
    mysql:latest
