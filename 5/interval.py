
class Interval:
  start = 0
  end = 0
  weight = 0

  def __init__(self, start, end, weight = 0) -> None:
    self.start = start
    self.end = end
    self.weight = weight
    

  def split(self, bins):
    new_intervals = []
    current_start = self.start
    for bin in bins:
      if bin.covers(Interval(current_start, self.end)):
        return new_intervals + [Interval(current_start, self.end, bin.weight)]

      if current_start < bin.start:
        new_intervals.append(Interval(current_start, bin.start - 1))
        current_start = bin.start
      
      if bin.start <= current_start <= bin.end:
        new_intervals.append(Interval(current_start, bin.end, bin.weight))
        current_start = bin.end + 1

    return new_intervals + [Interval(current_start, self.end)]
      

  def merge(self, other):
    if self.covers(other):
      return Interval(self.start, self.end)
    
    if self.start <= other.start <= self.end:
      return Interval(self.start, other.end)
    
    if other.start <= self.start <= other.end:
      return Interval(other.start, self.end)
    
    return None


  def slide(self, dist):
    return Interval(self.start + dist, self.end + dist)
  

  def covers(self, other):
    return self.start <= other.start and self.end >= other.end
  

  def __str__(self) -> str:
    return f"[{self.start}, {self.end}]"
  

  def __repr__(self) -> str:
    return self.__str__()
  

  def __lt__(self, other) -> bool:
    return self.start < other.start or (self.start == other.start and self.end <= other.end)
