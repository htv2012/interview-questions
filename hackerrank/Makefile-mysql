### Create a new directory
new:
	copier copy .template .

shell:
	bin/shell.sh

conn:
	@podman exec -it mysql-container mysql -u root sandbox

install:
	podman pull docker.io/library/mysql:latest

start:
	# https://infotechys.com/deploying-mysql-using-podman/
	mkdir -p /var/tmp/mysql
	podman run                                       \
		--name mysql-container                       \
		-e MYSQL_ROOT_PASSWORD=$(pw)                 \
		-d                                           \
		-p 3306:3306                                 \
		-v /var/tmp/mysql:/var/lib/mysql             \
		mysql:latest


