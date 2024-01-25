# Set of structs / enums that are autogenerated / used in the C++ engine
from csp.impl.enum import Enum
from csp.impl.struct import Struct

CSP_AUTOGEN_HINTS = {"cpp_header": "csp/engine/csp_autogen/autogen_types.h"}


class DynamicBasketEvent(Struct):
    key: object
    added: bool


class DynamicBasketEvents(Struct):
    events: [DynamicBasketEvent]

    @property
    def added(self):
        """Note a key could be added, removed, added in a single cycle for some nefarious reason"""
        return [event.key for event in self.events if event.added]

    @property
    def removed(self):
        return [event.key for event in self.events if not event.added]


class TimeIndexPolicy(Enum):
    """An enum that specifies the policy for handling the start and end values in functions like values_at."""

    INCLUSIVE = 1
    EXCLUSIVE = 2
    EXTRAPOLATE = 3  # NOTE: FORCED uses DuplicatePolicy.LAST_VALUE on the tick.
