from os import system, startfile
from subprocess import run, CalledProcessError
from src.log.logging import _logger

class PCUtils:
    def __init__(self):
        pass

    def open_app(self, app_path: str) -> bool:
        "Open app with app path"
        try:
            startfile(app_path)
            _logger.info(f"Opened app: {app_path}")

            return True

        except Exception as e:
            _logger.error(f"Error with open {app_path}: {str(e)}")
            return False
        
    def close_app(self, process_name: str) -> bool:
        "Close app by process name"
        try:
            run(['taskkill', '/IM', process_name, '/F'], check=True)
            _logger.info(f"Closed app: {process_name}")

            return True

        except CalledProcessError as e:
            _logger.error(f"Failed to close {process_name}: {str(e)}")
            return False

    def shutdown(self) -> bool:
        "Shutdown PC"
        try:
            system('shutdown /s /t 0')
            _logger.info("PC is shutting down...")

            return True

        except Exception as e:
            _logger.error(f"Failed to shutdown: {str(e)}")
            return False

    def reboot(self) -> bool:
        "Reboot PC"
        try:
            system('shutdown /r /t 0')
            _logger.info("PC is rebooting...")

            return True

        except Exception as e:
            _logger.error(f"Failed to reboot: {str(e)}")
            return False

    def sleep(self) -> bool:
        "Put PC to sleep mode"
        try:
            system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            _logger.info("PC is going to sleep...")

            return True

        except Exception as e:
            _logger.error(f"Failed to put PC to sleep: {str(e)}")
            return False
