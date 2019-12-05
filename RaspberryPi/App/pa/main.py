from configparser import ConfigParser
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from ui.dashboard import Dashboard
from ui.tuning import Tuning
from logic import Logic
from model.enums import DashboardMode
from model.enums import *
import logging





def main():
    print("######### Test GUI app")

    # Read config
    config = ConfigParser()
    config.read("app.ini", encoding="UTF-8")

    logging.basicConfig(level=logging.INFO)

    mode = DashboardMode[config.get(section="DASHBOARD", option="InitMode")]

    app = QApplication([])

    dashboard = Dashboard(mode)

    logic = Logic(config, dashboard)

    timer = QTimer()
    timer.timeout.connect(logic.tick)
    timer.start(2)






    # testLevel = DashboardLevel.inactive
    #
    #
    # def tick():
    #     print("Tick")
    #     if testLevel == DashboardLevel.ok:
    #         testLevel = DashboardLevel.warning






    if config.getboolean(section="MAIN", option="ShowTuningUi"):
        tuning = Tuning(
            onRaceMode=lambda: dashboard.setMode(DashboardMode.race),
            onStreetMode=lambda:  dashboard.setMode(DashboardMode.street))
        tuning.show()

    app.exec_()


if __name__ == '__main__':
    main()
