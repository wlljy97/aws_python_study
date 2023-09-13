class Student:

    # 생성자
    # self == this -> 자기 자신의 주소(생성된 객체의 주소)
    # 파이썬 에서는 생성자 쪽이 중요하다.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString()
    def __str__(self):
        return f"Student[name: {self.name}, age: {self.age}]"

    def setName(self, name):
        self.name = name


def main():
    # new 키워드가 필요없다.
    s1 = Student("김준일", 30)
    print(s1.name)

if __name__ == "__main__":
    main()

print("학생모듈", __name__)