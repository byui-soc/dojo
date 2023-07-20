# Challenge 9

## Belt Granted: Red Belt
## Skills Used: Enumeration, Privilege Escalation 

You were able to pop a shell on a box during a pentest. Your job now is to enumerate the system, escalate your privileges to the root user, and grab the root.txt flag.

## Setup
This challenge is designed to be run locally with docker.<br>
To install docker, run:
```
sudo apt update && sudo apt install docker.io
```
Ensure docker is working with:
```
docker --version
```
Then, download the linux.tar image file [here](linux.tar), and start it by running:
```
docker load -i linux.tar
docker run -t -i linux /bin/bash
```

## Help
If you're having trouble, I suggest completing the [Linux Privilege Escalation Room](https://tryhackme.com/room/linprivesc) on TryHackMe.
