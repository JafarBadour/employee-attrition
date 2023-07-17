FROM python:3.9.13
ARG RUN_ID
ARG MODEL_NAME
ENV SERVER_PORT 5000
ENV SERVER_HOST 0.0.0.0
ENV FILE_STORE /opt/mlflow/fileStore/
ENV ARTIFACT_STORE /opt/mlflow/artifactStore
ENV PYTHONPATH /opt/mlflow/utils
RUN mkdir -p /opt/mlflow/scripts \
&& mkdir -p ${FILE_STORE} \
&& mkdir -p ${ARTIFACT_STORE}

COPY ./temp/SVCmodel ${ARTIFACT_STORE}/SVCmodel
COPY ./temp/cpu-requirements.txt ${ARTIFACT_STORE}/cpu-requirements.txt

RUN pip install -r ${ARTIFACT_STORE}/cpu-requirements.txt \
&& apt-get update \
&& apt-get install -y git
# Copy over artifact and code
COPY run.sh /opt/mlflow/scripts/

RUN chmod +x /opt/mlflow/scripts/run.sh 
ENTRYPOINT ["/usr/bin/env"]
COPY ./temp/ ${FILE_STORE}/

WORKDIR $FILE_STORE
CMD ["bash", "/opt/mlflow/scripts/run.sh"]
#CMD ["tail", "-f", "/dev/null"]