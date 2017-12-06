# Sites Monitoring Utility

**The module check sites health**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart
**Ways to use:**
- Have to use  module `check_sites_health.py` after `python3` with `url.txt`.
  - You get 30 days before expiration  by default.
  - You may get other amount days, if use `-d`.


Example of script launch on Linux, Python 3.5:


```bash
$ python3 check_sites_health.py url.txt -d 50
Domain:http://linux.org is OK!
Domain:https://pythonworld.ru is OK!
Domain:https://habrahabr.ru is OK!
Domain:http://stackoverflow.com is OK!
Domain:https://toster.ru is OK!
Domain:http://vk.ru is OK!
Domain:http://yandex.ru is OK!
Domain:http://djbook.ru is OK!
Domain:http://mail.ru is OK!

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
