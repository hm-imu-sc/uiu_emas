
class CommentFactory:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if CommentFactory.__self_instance is None:
            CommentFactory.__self_instance = CommentFactory(**kwargs)
        return CommentFactory.__self_instance

    def get(self, obj_type, **kwargs):

        if obj_type == "cse_ps_comment":
            return CSEPSComment.instantiate(**kwargs)
        elif obj_type == "club_ff_comment":
            return ClubFFComment.instantiate(**kwargs)
        
        return None

class CSEPSComment:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if CSEPSComment.__self_instance is None:
            CSEPSComment.__self_instance = CSEPSComment(**kwargs)
        return CSEPSComment.__self_instance

class ClubFFComment:
    __self_instance = None

    def __init__(self, **kwargs):
        pass

    def instantiate(**kwargs):
        if ClubFFComment.__self_instance is None:
            ClubFFComment.__self_instance = ClubFFComment(**kwargs)
        return ClubFFComment.__self_instance

