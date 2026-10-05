#!/usr/bin/env python3
"""Genera la carta pública (index.html, sin bebidas) a partir de la carta completa del QR de mesa.
La carta completa es la única que se edita: <carpeta mesa-*>/index.html. Después: python3 build.py"""
import glob,re
src=glob.glob("mesa-*/index.html"); assert len(src)==1, src
s=open(src[0],encoding="utf-8").read()
s=re.sub(r"/\*BEBIDAS\*/.*?/\*FIN-BEBIDAS\*/","",s,flags=re.S)
s=s.replace('<meta name="robots" content="noindex,nofollow">\n',"")
s=s.replace("../","")
assert "s:\"vinos\"" not in s and "Moët" not in s and "Larios" not in s
open("index.html","w",encoding="utf-8").write(s)
print("index.html generado desde",src[0])
