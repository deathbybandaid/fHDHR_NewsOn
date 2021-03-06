

class Startup_Tasks():
    endpoints = ["/api/startup_tasks"]
    endpoint_name = "api_startup_tasks"
    endpoint_methods = ["GET", "POST"]

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

        self.epg_update_url = "/api/epg?method=update"
        self.channel_update_url = "/api/channels?method=scan"

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        # Hit Channel Update API
        haseverscanned = self.fhdhr.db.get_fhdhr_value("channels", "scanned_time")
        updatechannels = False
        if not haseverscanned:
            updatechannels = True
        elif self.fhdhr.config.dict["fhdhr"]["chanscan_on_start"]:
            updatechannels = True

        if updatechannels:
            self.fhdhr.api.get(self.channel_update_url)

        # Hit EPG Update API
        for epg_method in self.fhdhr.device.epg.epg_methods:
            self.fhdhr.api.get("%s&source=%s" % (self.epg_update_url, epg_method))

        return "Success"
