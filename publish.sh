#! /bin/bash

cd ~/Trove
\cp -ur ../RPG/Trove .
python publish.py
git add .
git commit -am "updating"
git push
