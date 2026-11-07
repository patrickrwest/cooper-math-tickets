# Wraps the artifact source (../cooper-math-tickets.html) into a full standalone index.html with home-screen icon tags.
import sys
src = open(sys.argv[1]).read().replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="docs/icon-192.png">
<link rel="manifest" href="manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Tickets">
<meta name="theme-color" content="#d94f3d">
'''
i = src.index('<div class="wrap">')
open('index.html', 'w').write(head + src[:i] + '</head>\n<body>\n' + src[i:] + '</body>\n</html>\n')
