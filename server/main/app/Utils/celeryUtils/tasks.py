from app.Utils.recUtils.RecEngine import recBooks
from app.Utils.celeryUtils.celapp import CELERY as c

async_recommend = c.task(recBooks)
