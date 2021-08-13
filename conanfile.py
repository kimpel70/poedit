from conans import ConanFile, tools


class PoeditConan(ConanFile):
    name = "poedit"
    version = "2.2.3"
    description = "Werkzeug um Übersetzungen für Anwendungen zu unterstützen (32bit-Release)"
    url = "https://poedit.net/"
    license = "None"
    author = "Václav Slavík"
    topics = None

    def package(self):
        build_type="Release"
        self.copy("*", src=build_type + "/GetTextTools", dst="GetTextTools")
        self.copy("*", src=build_type + "/Resources", dst="Resources")
        self.copy("*", src=build_type + "/Translations", dst="Translations")
        self.copy("Poedit.exe", src=build_type)
        self.copy("WinSparkle.dll", src=build_type)
        self.copy("icuin57.dll", src=build_type)
        self.copy("mCtrl.dll", src=build_type)
        self.copy("icuuc57.dll", src=build_type)
        self.copy("icudt57.dll", src=build_type)
        self.copy("icudt57l.dat", src=build_type)


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

    # install <reference> ruft deploy auf
    def deploy(self):
        self.copy("*")
