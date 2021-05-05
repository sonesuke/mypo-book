FROM amd64/python:3.7.10-slim-buster

RUN apt update && \
    apt install -y make fonts-ipafont-gothic npm && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install sphinx sphinx-book-theme seaborn docutils-ast-writer

RUN npm config set unsafe-perm true
RUN npm install --global textlint textlint-plugin-rst textlint-rule-preset-japanese

RUN pip install mypo