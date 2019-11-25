#!/bin/sh
cd ~/Desktop/Projects_Github/Mini-Sql-Engine
git init
git add .
git commit -m "first"
git config --global user.email "9412470@gmail.com"
git config --global user.name "aman-agrawal"
git remote add origin https://github.com/aman-agrawal/Mini-Sql-Engine.git
git push -u origin master
git config credential.helper store
git push https://github.com/aman-agrawal/Mini-Sql-Engine.git
