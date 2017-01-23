#!/bin/bash

echo "Primero dry-run:"

rsync -avz -n --delete --no-perms --no-owner --no-group --exclude "data/media/*" --exclude "data/static/*" --exclude "*/.DS_Store"  --exclude "__pycache__"  --exclude ".vagrant/" --exclude "conf/local_*.py" --exclude "src/" --exclude "*.pyc" ./ root@facturas.openmultimedia.biz:/vagrant

echo "CUALQUIER TECLA PARA EJECUTAR"
read

rsync -avz --delete --no-perms --no-owner --no-group  --exclude "data/media/*" --exclude "data/static/*" --exclude "*/.DS_Store" --exclude "__pycache__" --exclude ".vagrant/" --exclude "conf/local_*.py" --exclude "src/" --exclude "*.pyc" --exclude "data/db.sqlite3" ./ root@facturas.openmultimedia.biz:/vagrant
