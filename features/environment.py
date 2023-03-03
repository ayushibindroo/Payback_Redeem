import time
from features.utility.UtilityClass import UtilityClass


def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    time.sleep(1)

    UtilityClass.browser_maximise(context)
    time.sleep(1)

    UtilityClass.launch_app(context)
    time.sleep(1)


def after_scenario(context, driver):
    time.sleep(1)
    UtilityClass.close_browser(context)