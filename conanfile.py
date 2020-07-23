# conanfile.py
from conans import ConanFile

class FoobarConan(ConanFile):
    name = 'foobar'
    version = '0.0.1'
    requires = 'Catch2/[>=2.0]@catchorg/stable'
    build_requires = 'b2/4.0.0'

    generators = 'b2'
    exports_sources = 'jamroot.jam'

    def build(self):
        self.run("b2")
