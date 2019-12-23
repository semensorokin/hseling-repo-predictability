FROM hseling/hseling-api-base:python3.6-alpine3.7 as build

LABEL maintainer="Sergey Pletenev <info@linghub.ru>"

RUN mkdir /dependencies
COPY ./hseling_api_predictability/requirements.txt /dependencies/requirements.txt
COPY ./hseling_api_predictability/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=build /dependencies /dependencies

COPY ./hseling_lib_predictability /dependencies/hseling_lib_predictability
RUN pip install /dependencies/hseling_lib_predictability

COPY ./hseling_api_predictability/hseling_api_predictability /app/hseling_api_predictability
COPY ./hseling_api_predictability/main.py /app/main.py

ENV HSELING_API_PREDICTABILITY_SETTINGS="/app/hseling_api_predictability/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost/healthz || exit 1
