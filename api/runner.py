from services.plugin_points import ServicePluginPoint
from multiprocessing import Pool


def run_plugin((plugin, processed_text)):
    return plugin.get_experience(processed_text)


class Runner:
    def __init__(self, pool_size):
        self.pool_size = pool_size

    def gather_experiences(self, processed_text, categories):
        plugins_to_be_run = self.__get_plugins_to_run(categories)

        experiences = []

        if len(plugins_to_be_run) > 0:
            experiences = self.__run_plugins(plugins_to_be_run, processed_text)

        return experiences

    def __get_plugins_to_run(self, categories):
        plugins = ServicePluginPoint.get_plugins()

        if plugins is not None:
            plugins_to_be_run = []
            categories_set = set(categories)

            for plugin in plugins:
                if plugin.is_active():
                    same_categories = set.intersection(categories_set, set(plugin.categories()))

                    if len(same_categories) > 0:
                        plugins_to_be_run += [plugin]

            return plugins_to_be_run
        else:
            return []

    def __run_plugins(self, plugins, processed_text):
        pool = Pool(processes=self.pool_size)

        processed_text_list = [processed_text for x in range(0, len(plugins))]

        zipped = zip(plugins, processed_text_list)

        result = pool.map_async(run_plugin, zipped)

        return result.get()
