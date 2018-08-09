#!/bin/sh


sudo su && ssh root@35.237.233.134 <<EOF
  cd Iaculus
  git pull
  source /home/sharpthunder/Iaculus/.venv/bin/activate
  pip install -r requirements.txt
  python ./Iaculus/manage.py migrate
  sudo supervisorctl restart iaculus
  exit

