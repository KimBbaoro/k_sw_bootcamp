#(100°F − 32) × 5/9 = 37.778°C

# def temp_converter(f):
#     c = (100*f-32)*(5/9)
#     return c
#
# f = float(input('화씨 온도 : '))
# print(temp_converter(f))

fahrenheit = float(input('화씨 온도 : '))
celsius = (fahrenheit - 32.0) * (5.0/9.0)
print(f'화씨 온도 {fahrenheit}도는 섭씨 온도 {celsius}입니다.')