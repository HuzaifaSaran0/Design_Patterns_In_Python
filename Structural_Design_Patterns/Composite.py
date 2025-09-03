# 🌳 Composite Pattern (Structural)
# 🎯 Purpose

# The Composite Pattern lets you treat a group of objects and a single object in the same way.
# group of objects -> (composite) and single object -> (leaf)
# It’s great when you have tree-like structures.

# 🧩 Easy Example

# Imagine you’re building a File Explorer:

# File → single item (leaf).
# Folder → can contain files or other folders (composite).

# You want to be able to do things like:

# open()
# delete()
# get_size()

# 👉 With Composite, you can call these methods on both files and folders, without caring if it’s a single file or a folder with many things inside.

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class File(FileSystemComponent):
    def show(self):
        print("Showing file.")

    def delete(self):
        print("Deleting file.")


class Folder(FileSystemComponent):
    def __init__(self):
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show(self):
        print("Showing folder.")
        for child in self.children:
            child.show()

    def delete(self):
        print("Deleting folder.")
        for child in self.children:
            child.delete()


folder1 = Folder()
# file = File()
folder1.add(File())
folder1.add(File())
folder1.add(Folder())

folder2 = Folder()
folder2.add(File())

folder1.show()
folder2.show()
# OUTPUT
# Showing folder.
# Showing file.
# Showing file.
# Showing folder.
# Showing folder.
# Showing file.

# folder1.delete()
# file.show()
# file.delete()
