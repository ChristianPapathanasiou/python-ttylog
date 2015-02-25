# python tty-log

A python tty keylogger C. Papathanasiou 2015

A simple strace based python tty keylogger. With a bit of additional work (and its intended purpose for me) is to be used for heuristic analysis of user sessions to detect user behaviour that lies outside of normal and take action to block  user/assist with policy enforcement.

Example usage: 

```
[root@localhost /]# python tty-log.py <pid of tty>
clear
id
uname -a
w
ls

^C
KeyboardInterrupt
[root@localhost /]
```
