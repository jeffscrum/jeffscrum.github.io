FROM sphinxdoc/sphinx:5.2.1

WORKDIR /docs
ADD requirements.txt /docs
RUN pip install --upgrade pip && pip install -r /docs/requirements.txt
