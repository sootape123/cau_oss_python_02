import math # math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기

class Line:
    __length = None #클래스에서 length 값을 숨기기 위해 사용, 모든 필드의 기본값 None 으로 정의.

    def __init__(self, length = 1):
        # 클래스의 생성자 메서드, 매개변수 length의 기본값은 1
        if not ((isinstance(length, int) or isinstance(length, float)) and length > 0):
            self.__length = 1
        else : self.__length = length 

    def set_length(self, length):
        # __length 필드에 접근하기 위한 메서드
        if not ((isinstance(length, int) or isinstance(length, float)) and length > 0):
            self.__length = 1
        else : self.__length = length #필드의 범위, 유효성을 미리 판단하여 적용 가능능

    def get_length(self): #__length 필드에 접근하기 위한 메서드
        return self.__length #필드의 값을 읽기 전용으로 생성
    
def area_square(line):
    """함수 area_square는 Line클래스의 객체를 매개변수로 받아, length**2인 정사각형의 넓이 반환
    Args : 매개변수 line : 반지름의 길이
        매개변수 line(클래스): figure.main에서 모듈로 figure.py를 불러옴. 그리고 figure.main에서 myline이라는 figure.py의 Line 클래스 생성.
        매개변수 line은 figure.py의 area_square 함수의 매개변수로 받는 클래스이다.
    Returns :
        반환 타입 : line의 클래스가 Line이 아닌경우 0을 반환하고, 맞는경우 length의 제곱을 반환한다."""
    if (type(line) != Line):
        return 0
    else :
        return line.get_length() **2
    
def area_circle(line):
    #예시
    """ 길이를 입력받아 원의 넓이를 구하는 함수.
    Args : (매개변수 line )
        line (Line) : 반지름의 길이.igure.main에서 모듈로 figure.py를 불러옴. 그리고 figure.main에서 myline이라는 figure.py의 Line 클래스 생성.
        매개변수 line은 figure.py의 area_square 함수의 매개변수로 받는 클래스이다.
    Returns : (line의 클래스가 Line이 아닌경우 0을 반환하고, 맞는경우 length 제곱에 파이를 곱한 값을 반환)
        int or float : 원의 넓이를 반환"""
    if (type(line) != Line):
        return 0
    else :
        return line.get_length() **2 * math.pi
    
def area_regular_triangle(line):
    """길이를 입력받아 삼각형의 넓이를 구하는 함수.
    Args : (매개변수 line )
        line (Line) : 삼각형의 한 변의 길이.igure.main에서 모듈로 figure.py를 불러옴. 그리고 figure.main에서 myline이라는 figure.py의 Line 클래스 생성.
        매개변수 line은 figure.py의 area_square 함수의 매개변수로 받는 클래스이다.
    Returns : (line의 클래스가 Line이 아닌경우 0을 반환하고, 맞는경우 length 제곱에 루트3 /4를 곱한 값을 반환한다.)
        int or float : 삼각형의 넓이를 반환한다"""
    if (type(line) != Line):
        return 0
    else :
        return line.get_length() **2*math.sqrt(3) / 4
