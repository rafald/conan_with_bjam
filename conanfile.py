# conanfile.py
from conans import ConanFile

class FoobarConan(ConanFile):
    name = 'foobar'
    version = '0.0.1'
    requires = 'Catch2/[>=2.0]@catchorg/stable', 'folly/[>=2019.10.21.00]' 
    build_requires = 'b2/4.0.0'

    generators = 'b2'
    exports_sources = 'jamroot.jam'

    def build(self):
        self.run("b2 -d2")

#ExampleOnly
from conans import ConanFile, CMake, tools

class LibConan: #(ConanFile):
     def source(self):
         self.run("git clone https://github.com/conan-io/hello.git")

     def build(self):
         cmake = CMake(self)
         cmake.configure(source_folder="hello")
         cmake.build()
