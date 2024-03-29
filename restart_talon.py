import os

from talon import Module, app, ui, actions

mod = Module()


@mod.action_class
class Actions:
    def talon_relaunch():
        """Quit and relaunch the Talon app"""
        from shlex import quote
        from subprocess import Popen

        talon_app = ui.apps(pid=os.getpid())[0]
        talon_app_path = quote(talon_app.path)
        if app.platform == "mac":
            Popen(
                [
                    "/bin/sh",
                    "-c",
                    f"/usr/bin/open -W {talon_app_path} ; /usr/bin/open {talon_app_path}",
                ],
                start_new_session=True,
            )
            actions.sleep("100ms")
            talon_app.quit()
