#!/bin/bash
echo INICIANDO TRABAJO
set -e
LOGDIR=/var/log/gunicorn/
test -d $LOGDIR || mkdir -p $LOGDIR
LOGFILE=/var/log/gunicorn/hello.log
touch $LOGFILE
NUM_WORKERS=3
TIME_OUT=120
# user/group to run as
USER=root
GROUP=root
cd /srv/www/app/
echo Current Conf: -b 0.0.0.0:8000 PsicoBack.wsgi:application -w $NUM_WORKERS --timeout $TIME_OUT \
    --user=$USER --group=$GROUP --log-level=info \
    --log-file=$LOGFILE 2>>$LOGFILE
#exec python3 manage.py runserver --settings=PsicoBack.development_docker

exec gunicorn -b 0.0.0.0:8000 PsicoBack.wsgi:application -w $NUM_WORKERS --timeout $TIME_OUT \
    --user=$USER --group=$GROUP --log-level=info \
    --log-file=$LOGFILE 2>>$LOGFILE