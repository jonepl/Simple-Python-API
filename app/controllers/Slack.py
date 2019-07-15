import os
from app.controllers.Controller import Controller

# TODO: find a better place for this
resources = [
    {
        "name" : "Intro Service",
        "resource" : "intro",
        "method" : "_runIntro"
    },
    {
        "name" : "File Service",
        "resource" : "files",
        "method" : "_runFiles"
    }
]

class Slack(Controller):
    
    def __init__(self, resources=resources):
        self._validateResources(resources)
        self.resources = resources
        self.apiResources = self._generateApiResources(resources)

    def listResources(self) :
        return self.apiResources

    # TODO: Find a better way to execute all resource method rather using if else
    def runResource(self, resource):
        if resource == "intro" :
            return self._executeIntroResource()
        elif resource == "files":
            return self._executeFileResource()
        else :
            return { "message" : "ERROR: NOT FOUND." }

    def _generateApiResources(self, resources) :
        apiResources = []
        for resource in resources:
            x = resource.copy()
            del x["method"]
            apiResources.append(x)

        return apiResources

    def _executeIntroResource(self):
        return { "content": "The cat is fat", "type": "text" }

    def _executeFileResource(self):
        filename = "app/controllers/temp/tokoyami.png"
        if(os.path.exists(filename)) :
            return { "content": filename, "type": "file" }
        else :
            return {}

    def _validateResources(self, resources) :
        for resource in resources :
            if ("name" in resource and "resource" in resource and "method" in resource):
                return True
            else:
                raise ValueError("Resources do not have all required fields")


if __name__ == "__main__":
    print('Subclass: ' + str(issubclass(Slack, App)))
    print('Instance: ' + str(isinstance(Slack(), App)))
