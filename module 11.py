class Publication:
    def __init__ (self,type, name):
        self.type = type
        self.name = name

    def print_information(self):
        print(f"{self.type} : {self.name}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__("Magazine", name)
        self.chief_editor = chief_editor

    def print_information(self):
        super(). print_information()
        print(f"Editor: {self.chief_editor}")


publication = Publication("Book", "This book is called book" )
publication.print_information()

magazine = Magazine("Ako Ankka", "Akki Hyppa")
magazine.print_information()