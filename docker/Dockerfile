# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/pgwall_test
COPY ./ /tmp/pgwall_test/
RUN pip install /tmp/pgwall_test

RUN rm -rf /tmp/pgwall_test

ENTRYPOINT ["/opt/conda/bin/pgwall_testcmd.py"]

CMD ["--help"]
