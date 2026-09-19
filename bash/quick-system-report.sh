#!/usr/bin/env bash
set -u
printf 'Hostname: '; hostname
printf 'Kernel: '; uname -r
printf 'Uptime: '; uptime -p
printf '\nMemory:\n'; free -h
printf '\nDisk:\n'; df -h /
printf '\nFailed services:\n'; systemctl --failed --no-legend 2>/dev/null || true
printf '\nListening ports:\n'; ss -lnt 2>/dev/null || true
