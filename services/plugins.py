from djangoplugins.point import PluginPoint


class ServicePluginPoint(PluginPoint):
    def get_experience(self, text):
        pass

    def categories(self):
        return []


class SampleService(ServicePluginPoint):
    name = 'sample'
    title = 'sample plugin'

    def get_experience(self, text):
        return 'Sample Experience'

    def categories(self):
        return ['*']


class SampleService2(ServicePluginPoint):
    name = 'sample2'
    title = 'sample plugin2'

    def get_experience(self, text):
        return 'Sample Experience2'

    def categories(self):
        return ['*']
