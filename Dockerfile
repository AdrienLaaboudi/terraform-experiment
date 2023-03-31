#Multi-staged Dockerfile

#Installing node and building the conda environment
FROM continuumio/miniconda3 AS node-conda
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install curl -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && apt-get install -y nodejs

RUN mkdir -p /backend
RUN mkdir -p /scripts
RUN mkdir -p /static-files
RUN mkdir -p /media-files
RUN mkdir -p /frontend

COPY ./scripts /scripts
RUN chmod +x ./scripts

COPY ./backend/requirements.yml /backend/requirements.yml
RUN /opt/conda/bin/conda env create -f /backend/requirements.yml

#Building the frontend
FROM node-conda AS frontend

WORKDIR /frontend
COPY ./frontend/package.json /frontend/
COPY ./frontend/package-lock.json /frontend/
RUN npm install
COPY ./frontend /frontend
RUN npm run build

Building the backend, activating the conda environment and
FROM node-conda AS final

COPY --from=node-conda /opt/conda/envs/DRF-batch-23 /opt/conda/envs/DRF-batch-23

COPY ./backend /backend

ENV PATH /opt/conda/envs/DRF-batch-23/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
RUN echo "source activate DRF-batch-23">~/.bashrc

COPY --from=frontend /frontend/build /frontend/build
WORKDIR /backend