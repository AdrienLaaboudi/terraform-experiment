FROM continuumio/miniconda3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN mkdir -p /backend
RUN mkdir -p /scripts

COPY ./backend /backend
COPY ./scripts /scripts

RUN chmod +x ./scripts


RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/DRF-batch-23/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
RUN echo "source activate DRF-batch-23">~/.bashrc

WORKDIR /backend