import math

class BitBooleanFlags:
    def __init__(self, *args):
        self._bitflags = {}
        for index, arg in enumerate(args):
            self._bitflags[arg] = 1 << index
        self.max_power = len(self._bitflags)
        

    def __call__(self,*holders):
        holder_combined = 0
        for holder in holders:
            bit_len = 0
            if(holder>0):
                bit_len = int(math.log(int(holder),2)) + 1 #Find bit length
            if (type(holder) is int and holder>=0 and  bit_len<=self.max_power):
                holder_combined = holder_combined | holder
            else:
                raise Exception('Invalid Flag Store, flag variable should be an integer under the bit range of flags !')
        return self.Inner(self,holder_combined)

    def mappedFlags(self):
        return self._bitflags
        
    
    class Inner:
        def __init__(self, booleanFlags,holder):
            self._holder = holder
            self.booleanFlags = booleanFlags

        def add(self, *flags):
            for flag in flags:
                self._holder = self._holder | self.booleanFlags._bitflags[flag]
            return self._holder

        def remove(self, *flags):
            for flag in flags:
                self._holder = self._holder ^ self.booleanFlags._bitflags[flag]
            return self._holder 

        def orHas(self, *flags):
            for flag in flags:
                if ((self._holder & self.booleanFlags._bitflags[flag])!=0):
                    return True
            return False

        def has(self, *flags):
            for flag in flags:
                if ((self._holder & self.booleanFlags._bitflags[flag])==0):
                    return False
            return True