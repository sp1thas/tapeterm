FROM rothgar/mpsyt:latest

RUN pip install git+https://github.com/sp1thas/tapeterm.git

ENTRYPOINT ["tt"]

CMD ["--youtube-api-key", "$API_KEY"]
