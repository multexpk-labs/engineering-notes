# Command Notebook

## Linux

```bash
uname -a
uptime
free -h
df -h
ss -lntup
systemctl --failed
journalctl -p err -b
```

## Networking

```bash
dig example.com
curl -I https://example.com
curl -sS https://example.com/health
```

## Git

```bash
git status
git log --oneline -20
git diff
git branch -a
```

## PHP / Laravel

```bash
php -v
composer --version
php artisan about
php artisan migrate:status
```

Commands should be adapted to the actual environment. Do not execute destructive commands copied from a note without understanding their effect.
