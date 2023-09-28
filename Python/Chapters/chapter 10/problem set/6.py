from xml.dom import HierarchyRequestErr


class Sample:
    def __init__(self,name) -> None:
        self.name = name

b = Sample('Arya') 
print(b.name)