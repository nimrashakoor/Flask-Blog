#!/bin/bash

echo "Testing main page"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing Projects page"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/projects')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing Blog page"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/blog')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing Contact page"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/contact')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing health"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/health')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing login"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/login')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing register"
code=$(curl -s -o /dev/null -w "%{http_code}" 'http://mlh-blog-nimrashakoor.duckdns.org/register')
if (( $code >= 300 && $code <= 599 )); then
    echo "Fail: Error code $code"
else echo "Success"
fi
echo "Testing Complete"