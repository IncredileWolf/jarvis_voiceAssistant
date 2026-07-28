import subprocess

from data.applications import APPLICATIONS


class ApplicationCommands:

    @staticmethod
    def open_application(command):

        command = command.lower()

        for app, executable in APPLICATIONS.items():

            if app in command:

                subprocess.Popen(executable)

                return f"Opening {app}."

        return None