



# 인스턴스 변수, 메소드
# 클래스 변수, 메소드 
'''
    class 클래스명 : 
        클래스변수명 = 값

    # 클래스 메소드
    @classmethod
    def 메소드명(cls):
        메소드 내용
        
    # cls : 클래스 

        
    클래스 변수에 접근
    - 클래스명.변수명

'''

class Student:
    # name = ''     # 기본값 초기화
    # age = 0       #
    # tel ='' 
    # 클래스 변수 - 객체간에 공유할 값을 사용하는 변수
    count = 0
    student_list = []
    
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel            # ---> 인스턴스 변수 
        Student.count += 1
        Student.student_list.append(self)
    
    def __str__(self):
        return '{} / {} / {}' .format(self.name, self.age, self.tel)
    # 클래스 메소드
    # @이름     : 데코레이터 (자바에서는 어노테이션),
    #             해당 클래스나 메소드의 기능/용도를 명시하는 역할
    # @classmethod : 해당 메소드를 클래스 메소드로 명시 
    # 클래스 메소드의 첫번째 매개변수로 클래스(cls)를 받아온다.
    # 인스턴스 메소드의 첫번째 매개변수는 인스턴스(self)룰 받아온다. 
    @classmethod
    def show_info(cls):
        for student in cls.student_list:
            print( str(student) )

s1 = Student('김휴먼', 20, '010-1111-2222')
s2 = Student('이효리', 30, '010-1111-2222')
s3 = Student('손석구', 40, '010-1111-2222')

print('{} 명의 학생이 참여하엿ㅅ븐.ㅣ다.'.format(Student.count))

print( Student.show_info() )