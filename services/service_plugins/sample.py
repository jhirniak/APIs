from services.plugins import ServicePluginPoint


class SampleService(ServicePluginPoint):
    name = 'sample'
    title = 'sample plugin'

    def get_experience(self, text):
        return 'Sample Experience'

    def categories(self):
        return ['*']
