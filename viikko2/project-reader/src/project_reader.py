import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        c = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = c["tool"]["poetry"]["name"]
        desc = c["tool"]["poetry"]["description"]
        dependencies = c["tool"]["poetry"]["dependencies"]
        dev_dependencies = c["tool"]["poetry"]["dev-dependencies"]
        return Project(name, desc, dependencies, dev_dependencies)
