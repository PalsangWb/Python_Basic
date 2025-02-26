# Can you choose the self parameter inside a class to something else (say 'Palsang'). Try changing self to 'slf'
# or 'Palsang' and see the effects.

class Sample:
    def __init__(palsang, name):
        palsang.name = name

obj = Sample("You can use anything without 'self' but if you do that others will get confused.")
print(obj.name)




    