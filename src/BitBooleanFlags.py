import threading
import functools

class BitBooleanFlags:
    def __init__(self, *args):
        self._bitflags = {arg: 1 << index for index, arg in enumerate(args)}
        self.max_power = len(self._bitflags)
        self._lock = threading.Lock()

    def __call__(self, *holders):
        with self._lock:
            holder_combined = 0
            for holder in holders:
                bit_len = self._highest_set_bit_position(holder) + 1 if holder > 0 else 0
                if isinstance(holder, int) and holder >= 0 and bit_len <= self.max_power:
                    holder_combined |= holder
                else:
                    raise Exception('Invalid Flag Store, flag variable should be an integer under the bit range of flags!')
            return self.Inner(self, holder_combined)

    @functools.lru_cache(maxsize=None)
    def mappedFlags(self):
        with self._lock:
            return self._bitflags.copy()

    def _highest_set_bit_position(self, n):
        position = -1
        while n:
            position += 1
            n >>= 1
        return position

    class Inner:
        def __init__(self, booleanFlags, holder):
            self._holder = holder
            self.booleanFlags = booleanFlags
            self._lock = booleanFlags._lock

        def add(self, *flags):
            with self._lock:
                for flag in flags:
                    self._holder |= self.booleanFlags._bitflags[flag]
                return self._holder

        def remove(self, *flags):
            with self._lock:
                for flag in flags:
                    self._holder &= ~self.booleanFlags._bitflags[flag]
                return self._holder

        def orHas(self, *flags):
            with self._lock:
                return any(self._holder & self.booleanFlags._bitflags[flag] for flag in flags)

        def has(self, *flags):
            with self._lock:
                return all(self._holder & self.booleanFlags._bitflags[flag] for flag in flags)