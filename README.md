# django-web-app

This repository hosts the web app developed for the course Cyber Security Project I at the University of Helsinki.

## Default account
There is a default account that you can use to login into the web app.
username: admin
password: admin

## Overview of the Flaws (OWASP 2021)

1. ~~Cryptographic failure <br/>~~
 -> Deprecated hash function used (MD5).
2. ~~Identification and Authentication Failures <br/>~~
 -> Permits brute force or other automated attacks.
3. ~~Security logging and Monitoring failures <br/>~~
 -> Auditable events, such as logins, failed logins, and high-value transactions, are not logged.
4. ~~Security misconfiguration <br/>~~
 -> Error handling reveals informative error messages to users
5. ~~Broken Access Control <br/>~~
->  Browsing to authenticated pages as an unauthenticated user
