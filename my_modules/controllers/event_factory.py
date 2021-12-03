
class EventFactory:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if EventFactory.__self_instance is None:
            EventFactory.__self_instance = EventFactory(**kwargs)
        return EventFactory.__self_instance

    def get(self, obj_type, **kwargs):

        if obj_type == "cse_ps_event":
            return CSEPSEvent.instantiate(**kwargs)
        elif obj_type == "club_ff_event":
            return ClubFFEvent.instantiate(**kwargs)
        
        return None

class CSEPSEvent:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if CSEPSEvent.__self_instance is None:
            CSEPSEvent.__self_instance = CSEPSEvent(**kwargs)
        return CSEPSEvent.__self_instance

class ClubFFEvent:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if ClubFFEvent.__self_instance is None:
            ClubFFEvent.__self_instance = ClubFFEvent(**kwargs)
        return ClubFFEvent.__self_instance