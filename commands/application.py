import subprocess

from data.applications import APPLICATIONS


class ApplicationCommands:

    @staticmethod
    def open_application(command):

        command = command.lower()

        for app, executable in APPLICATIONS.items():

            if app in command:

                try:

                    subprocess.Popen(executable)

                    return f"Opening {app.title()}."

                except FileNotFoundError:

                    return f"{app.title()} is not installed."

                except Exception as e:

                    return f"Unable to open {app}. {e}"

        return None