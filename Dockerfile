FROM rothgar/mpsyt:latest

ADD MANIFEST.in MANIFEST.in
ADD tapeterm tapeterm
ADD requirements.txt requirements.txt
ADD setup.py setup.py
ADD README.md README.md

ENV LANG=en

RUN python setup.py install

CMD tapeterm --"$LANG"
