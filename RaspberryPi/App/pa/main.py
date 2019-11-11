import configparser as cp
from PyQt5.QtWidgets import QApplication
from ui.dashboard import Dashboard
from ui.tuning import Tuning
from model.enums import DashboardMode
import logging


print("######### Test GUI app")

# Read config
config = cp.ConfigParser()
config.read("app.ini", encoding="UTF-8")


print("config = " + str(config.getboolean(section="DASHBOARD", option="FullScreen")))






def main():
    logging.basicConfig(level=logging.DEBUG)

    mode = DashboardMode[config.get(section="DASHBOARD", option="InitMode")]

    app = QApplication([])

    dashboard = Dashboard(mode)
    dashboard.show()
    # dashboard.showFullScreen()

    tuning = Tuning(
        onRaceMode=lambda: dashboard.setMode(DashboardMode.race),
        onStreetMode=lambda:  dashboard.setMode(DashboardMode.street))
    tuning.show()

    app.exec_()


if __name__ == '__main__':
    main()