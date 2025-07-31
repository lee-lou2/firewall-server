import os

from apscheduler.schedulers.background import BackgroundScheduler
from apps.device.v1.tasks import recent_10_min_data_monitor


def start():
    if not os.environ.get("RUN_MAIN"):
        return
    scheduler = BackgroundScheduler()

    # 스케쥴러
    scheduler.add_job(
        recent_10_min_data_monitor,
        "interval",
        seconds=60 * 10,
        id="recent_10_min_data_monitor",
        replace_existing=True,
    )

    scheduler.start()
