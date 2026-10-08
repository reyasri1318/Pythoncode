class grandparent():
    def __init__(self,grandfather,grandmother):
        self.grandfather=grandfather
        self.grandmother=grandmother

    def details(self):
        print(f"""
              Grandfather: {self.grandfather}
              Grandmother: {self.grandmother}
              """)

class parent(grandparent):
    def __init__(self,grandfather,grandmother,father,mother):
        grandparent.__init__(self,grandfather,grandmother)
        self.father=father
        self.mother=mother

    def details(self):
        print(f"""
              Grandfather: {self.grandfather}
              Grandmother: {self.grandmother}
              Father: {self.father}
              Mother: {self.mother}
              """)

class child(grandparent):
    def __init__(self,grandfather,grandmother,father,mother,sister,brother):
        parent.__init__(self,grandfather,grandmother,father,mother)
        self.sister=sister
        self.brother=brother

    def details(self):
        print(f"""
              Grandfather: {self.grandfather}
              Grandmother: {self.grandmother}
              Father: {self.father}
              Mother: {self.mother}
              Sister: {self.sister}
              Brother: {self.brother}
              """)

family=child("Subramani","Rani","Raja","suhasini","Thulasi","Reyan")
family.details()
