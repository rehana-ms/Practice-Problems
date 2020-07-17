"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
    def addItem(self,s):
        self.items.append(s)
        print(self.items)
    def classiness(self):
        result=0
        for s in self.items:
            if(s=="tophat"):
                result+=2
            elif(s=="bowtie"):
                result+=4
            elif(s=="monocle"):
                result+=5
        print(result)
        return result

         
c=Classy()
c.addItem("tophat")
c.addItem("rehana")
c.addItem("bowtie")
c.addItem("jacket")
c.addItem("monocle")
result=c.classiness()