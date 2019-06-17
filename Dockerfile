FROM rothgar/mpsyt:latest

COPY MANIFEST.in MANIFEST.in
COPY tapeterm tapeterm
COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY README.md README.md

ENV LANG=en

RUN python setup.py install

CMD tapeterm --"$LANG"
