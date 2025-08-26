#Python Script showing object-oriented programming
class studentInput:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree

    def getStudent(self):
        return "My name is " + self.name + ", and I'm studying " + self.degree + "."

#Example
elijah = studentInput("Elijah", "Computer Science")
nick = studentInput("Nick", "Information Technology")

print (elijah.getStudent())
print (nick.getStudent())



