
class UserFactory:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if UserFactory.__self_instance is None:
            UserFactory.__self_instance = UserFactory(**kwargs)
        return UserFactory.__self_instance

    def get(self, obj_type, **kwargs):

        if obj_type == "student":
            return Student.instantiate(**kwargs)
        elif obj_type == "teacher":
            return Teacher.instantiate(**kwargs)
        elif obj_type == "club":
            return Club.instantiate(**kwargs)
        elif obj_type == "admin":
            return Admin.instantiate(**kwargs)
        elif obj_type == "special":
            return Sepecial.instantiate(**kwargs)
        
        return None

class Student:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate( **kwargs):
        if Student.__self_instance is None:
            Student.__self_instance = Student(**kwargs)
        return Student.__self_instance

class Teacher:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate( **kwargs):
        if Teacher.__self_instance is None:
            Teacher.__self_instance = Teacher(**kwargs)
        return Teacher.__self_instance

class Club:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate( **kwargs):
        if Club.__self_instance is None:
            Club.__self_instance = Club(**kwargs)
        return Club.__self_instance

class Admin:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate( **kwargs):
        if Admin.__self_instance is None:
            Admin.__self_instance = Admin(**kwargs)
        return Admin.__self_instance

class Sepecial:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate( **kwargs):
        if Sepecial.__self_instance is None:
            Sepecial.__self_instance = Sepecial(**kwargs)
        return Sepecial.__self_instance