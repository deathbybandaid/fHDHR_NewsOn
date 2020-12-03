from flask import request, render_template


class Diagnostics_HTML():
    endpoints = ["/diagnostics", "/diagnostics.html"]
    endpoint_name = "page_diagnostics_html"

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        button_list = []

        button_list.append({
                            "label": "Debug Json",
                            "hdhr": None,
                            "rmg": None,
                            "other": "/api/debug",
                            })

        button_list.append({
                            "label": "Cluster Json",
                            "hdhr": None,
                            "rmg": None,
                            "other": "/api/cluster?method=get",
                            })

        button_list.append({
                            "label": "Lineup XML",
                            "hdhr": "/lineup.xml",
                            "rmg": None,
                            "other": None,
                            })

        button_list.append({
                            "label": "Lineup JSON",
                            "hdhr": "/lineup.json",
                            "rmg": None,
                            "other": None,
                            })

        button_list.append({
                            "label": "Lineup Status",
                            "hdhr": "/lineup_status.json",
                            "rmg": None,
                            "other": None,
                            })

        button_list.append({
                            "label": "Discover Json",
                            "hdhr": "/discover.json",
                            "rmg": None,
                            "other": None,
                            })

        button_list.append({
                            "label": "Device XML",
                            "hdhr": "/hdhr/device.xml",
                            "rmg": "/rmg/device.xml",
                            "other": None,
                            })

        button_list.append({
                            "label": "RMG Identification XML",
                            "hdhr": "",
                            "rmg": "/rmg",
                            "other": None,
                            })

        return render_template('diagnostics.html', request=request, fhdhr=self.fhdhr, button_list=button_list)
