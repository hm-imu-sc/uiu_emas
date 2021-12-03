
class BoothFactory:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate():
        if BoothFactory.__self_instance is None:
            BoothFactory.__self_instance = BoothFactory()
        return BoothFactory.__self_instance

    def get(self, obj_type, **kwargs):

        if obj_type == "cse_ps_booth":
            return CSEPSBooth.instantiate(**kwargs)
        elif obj_type == "club_ff_booth":
            return ClubFFBooth.instantiate(**kwargs)
        
        return None

class CSEPSBooth:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if CSEPSBooth.__self_instance is None:
            CSEPSBooth.__self_instance = CSEPSBooth(**kwargs)
        return CSEPSBooth.__self_instance

class ClubFFBooth:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if ClubFFBooth.__self_instance is None:
            ClubFFBooth.__self_instance = ClubFFBooth(**kwargs)
        return ClubFFBooth.__self_instance