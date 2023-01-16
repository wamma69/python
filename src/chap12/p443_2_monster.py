class Monster :
   # 상수 값 정의 
   WEAK = 0
   NORMAL = 10
   STRONG = 20
   VERY_STRONG = 30

   def __init__(self) :
      self._health = Monster.NORMAL
