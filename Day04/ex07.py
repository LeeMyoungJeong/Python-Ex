import math

class Circle:
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            print('반지름은 양수여야만 합니다.')
            self.__radius = 0
            return
        
        self.__radius = value

    @radius.getter
    def radius(self):
        return self.__radius

circle = Circle()

circle.radius = -10
print('circle - radius : {}'.format( circle.radius )  )
# java에서 통장 만들었던 예제(캡슐화) 리뷰해라.
# 설 연휴동안 쌔빠지겠노 
# 나는새삥 모든것이쌔삥쌔ㅃ입쌔빠지는쌔삥
# 나는빈티지나너도너도빈티지