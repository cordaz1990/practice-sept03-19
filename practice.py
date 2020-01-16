#inside class Time:

def __add__(self, other):
    if isinstance(other, Time):
         return self.add_time(other)
    else:
        return self.increment(other)
      
     def add_time(self, other):
         seconds = self.time_to_int() + other.time_to_int()
         return int_to_time(seconds)
        
     def increment(self,seconds):
         seconds += self.time_to_int()
         return int_to_time(seconds)
