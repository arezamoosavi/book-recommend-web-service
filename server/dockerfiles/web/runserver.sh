#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


# run gunicorn
gunicorn wsgi:app -b 0.0.0.0:5000 --access-logfile '-' --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIMEOUT} $*