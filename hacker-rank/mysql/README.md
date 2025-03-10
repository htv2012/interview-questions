# Sandbox MySQL For Mac

https://dev.to/manikbajaj/how-to-install-mysql-8-on-macos-using-homebrew-399d

## Setup Passwordless

Create `~/my.cnf` with the following content

```
[mysql]
user=root
password=<Password here>
```

Make sure to change permission:

```bash
chmod 600 ~/.my.cnf
```


# For Ubuntu

```bash
apt update
apt upgrade -y
apt install -y mysql-server
```

We should be able to start the mysql shell without any password:

```bash
sudo mysql
```

After that, set the password. Issue the follow commands inside the mysql shell:

```
alter user 'root'@'localhost' identified with caching_sha2_password by 'new-password';
flush privileges;
```

After that, follow the *Setup Passwordless* steps.

