# %%

import figure
print(help(figure))
myline = figure.Line(10)

# 따로 생성자의 값을 수정하지 않았다면 출력값은
print(myline.get_length())
print(figure.area_square(myline))   # 100
print(figure.area_circle(myline))   # 314.1592~~~
print(figure.area_regular_triangle(myline)) # 43.3012~~~

myline.set_length(3)
# 따로 값을 수정하지 않았다면 출력값은
print(myline.get_length())
print(figure.area_square(myline))   # 9
print(figure.area_circle(myline))   # 28.2743~~~
print(figure.area_regular_triangle(myline)) # 3.8971~~~
# %%

