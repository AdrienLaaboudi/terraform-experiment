FROM continuumio/miniconda3

RUN mkdir -p /backend
COPY ./backend /backend

RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/DRF-batch-23/bin:$PATH
RUN echo "source activate DRF-batch-23">~/.bashrc

WORKDIR /backend