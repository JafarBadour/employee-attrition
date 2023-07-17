#!/bin/sh
# run.sh
source ${FILE_STORE}/.env
nohup python $FILE_STORE/src/monitor/sqlpusher.py &

mlflow models serve -m $ARTIFACT_STORE/SVCmodel -h $SERVER_HOST -p $SERVER_PORT --no-conda