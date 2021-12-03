
class PrizeFactory:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if PrizeFactory.__self_instance is None:
            PrizeFactory.__self_instance = PrizeFactory(**kwargs)
        return PrizeFactory.__self_instance

    def get(self, obj_type, **kwargs):

        if obj_type == "prize":
            return Prize.instantiate(**kwargs)
        
        return None

class Prize:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if Prize.__self_instance is None:
            Prize.__self_instance = Prize(**kwargs)
        return Prize.__self_instance