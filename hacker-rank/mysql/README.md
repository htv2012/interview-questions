# Sandbox MySQL


For Mac

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


