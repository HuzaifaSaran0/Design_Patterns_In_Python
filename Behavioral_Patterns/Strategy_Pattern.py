# (We have to use this Strategy pattern when you have a family of algorithms (or behaviors) and you want to make them interchangeable without changing the code that uses them.
# The difference between the Strategy pattern and State pattern is that the Strategy pattern is about selecting an algorithm at runtime, while the State pattern is about changing the behavior of an object when its internal state changes.
# )

# TIP: Iterator Pattern Contains 2 types of Classes:
# 1. Concrete Iterators of Different Types
# 2. Context(Main) Class

from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, image):
        pass


class Filter(ABC):
    @abstractmethod
    def apply(self, image):
        pass


class JpegCompressor(Compressor):
    def compress(self, image):
        print("Compressing using JPEG")


class PngCompressor(Compressor):
    def compress(self, image):
        print("Compressing using PNG")


class BmpCompressor(Compressor):
    def compress(self, image):
        print("Compressing using BMP")


class BrightnessFilter(Filter):
    def apply(self, image):
        print("Applying brightness filter")


class ContrastFilter(Filter):
    def apply(self, image):
        print("Applying contrast filter")

class BlurFilter(Filter):
    def apply(self, image):
        print("Applying blur filter")


class ImageStore:
    Compressor = None
    Filter = None
    def __init__(self, Compressor, Filter):
        self.Compressor = Compressor
        self.Filter = Filter
        self.images = []

    def store(self, image):
        compressed_image = self.Compressor.compress(image)
        filtered_image = self.Filter.apply(compressed_image)
        print("Storing image...")
        self.images.append(filtered_image)
        print("Image stored successfully.")
        return filtered_image


image_store = ImageStore(JpegCompressor(), BlurFilter())
image_store.store("Image1")
