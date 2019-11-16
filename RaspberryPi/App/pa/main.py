import configparser as cp
from PyQt5.QtWidgets import QApplication
from ui.dashboard import Dashboard
from ui.tuning import Tuning
from model.enums import DashboardMode
import logging


def main():
    print("######### Test GUI app")

    # Read config
    config = cp.ConfigParser()
    config.read("app.ini", encoding="UTF-8")

    logging.basicConfig(level=logging.DEBUG)

    mode = DashboardMode[config.get(section="DASHBOARD", option="InitMode")]

    app = QApplication([])

    dashboard = Dashboard(mode)

    if config.getboolean(section="DASHBOARD", option="FullScreen"):
        dashboard.showFullScreen()
    else:
        dashboard.show()

    if config.getboolean(section="MAIN", option="ShowTuningUi"):
        tuning = Tuning(
            onRaceMode=lambda: dashboard.setMode(DashboardMode.race),
            onStreetMode=lambda:  dashboard.setMode(DashboardMode.street))
        tuning.show()

    app.exec_()


if __name__ == '__main__':
    main()
