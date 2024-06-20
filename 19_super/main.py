class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Hey this is parent_method inside ChildClass")
        super().parent_method()
    def child_method(self):
        print("This is a child method.")
        super().parent_method()
        


child_obj  = ChildClass()
child_obj.child_method()
child_obj.parent_method() ##this will call the parent_method inside ChildCLass

##Now suppose there is no parent_method in ChildClass then it will automatically get inherited from the ParentClass and it will run paren_method from ParenClass

