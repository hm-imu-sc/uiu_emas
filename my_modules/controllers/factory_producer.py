from .booth_factory import BoothFactory
from .user_factory import UserFactory
from .comment_factory import CommentFactory
from .event_factory import EventFactory
from .prize_factory import PrizeFactory
from my_modules.exceptions import FactoryNotFound

class FactoryProducer:

    def get(obj_type, **kwargs):

        if obj_type == "booth_factory":
            return BoothFactory.instantiate(**kwargs)
        elif obj_type == "event_factory":
            return EventFactory.instantiate(**kwargs)
        elif obj_type == "user_factory":
            return UserFactory.instantiate(**kwargs)
        elif obj_type == "comment_factory":
            return CommentFactory.instantiate(**kwargs)
        elif obj_type == "prize_factory":
            return PrizeFactory.instantiate(**kwargs)
        
        return None