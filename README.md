# IT Drafts

Репозиторий статей с сайта https://pages.ksomov.ru

Также, в репозитории лежит несколько Dockerfile для сборки собственного Sphinx image

1. Dockerfile-html - для сборки имиджа генератора html
2. Dockerfile-ru-latexpdf - для сборки имиджа генератора pdf

``docker build -f <Dockerfile-...> -t <image-name>:<version> .``
