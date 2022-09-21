FROM sphinxdoc/sphinx:5.0.2

WORKDIR /docs
ADD requirements.txt /docs
RUN pip install --upgrade pip && pip install -r /docs/requirements.txt
