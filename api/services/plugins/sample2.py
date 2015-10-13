from api.services.plugin_points import ServicePluginPoint


class SampleService2(ServicePluginPoint):
    name = 'sample2'
    title = 'sample plugin2'

    def get_experience(self, text):
        return 'Sample Experience2'

    def categories(self):
        return ['*']
