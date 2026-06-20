import time
import config
from plyer import notification



if __name__ == "__main__":
    while True:
        notification.notify(
            title = config.task,
            app_name = config.app_name,
            message = config.message,
            toast=True,
            timeout= 1,
        )
        time.sleep(config.x)