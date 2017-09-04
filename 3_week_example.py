# 입력 받는 방법
# print("Enter your name")
# somebody = input()
# print("Hi", somebody)

# temperature = float(input("온도를 입력하세요 : "))
# print(temperature);


# 섭씨 화씨 온도를 변환하는 프로그램을 만드시오
# temperature = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요 :"))
# print(temperature)
# print("섭씨온도 : ",temperature)
# fahrenheit = ((9/5) * temperature) + 32
# print("화씨온도 : ",float(fahrenheit))

# List 또는 Array
# 시퀀스 자료형, 여러 데이터들의 집합(Int, Float 같은 다양한 데이터 Type 포함)
colors = ["red","blue","green"]
print(colors[0])
print(colors[1])
print(colors[2])
# 슬라이싱  - list의 값들을 잘라서 쓰는 것
city = ["서울","부산","인천","대구","대전","광주","울산"]
print(city[0:6]) # 0부터 5번째까지
print(city[:])  # 전체
print(city[-50:50]) # 범위를 넘어가면 전체를
print(city[::2]," AND ", city[::-1]) # 2칸씩 이동후 뒤에서 한칸씩 이동

print(colors + city) # 두 데이터 합치기
print(len(colors)) # 리스트의 길이
print('blue1' in colors)# 존재여부 확인
print(colors * 2) # 2번 출력해라

# 리스트 추가와 삭제
colors.append("white")  # 추가
colors.extend(["black","purple"]) # 리스트에 새로운 리스트 추가
colors.insert(0,"orange") # 0번째 주소에 추가
print(colors)
colors.remove("white") # 삭제
del colors[0]    # 0번째 주소 객체 삭제
print(colors)

a = [5,4,3,2,1]
b = [1,2,3,4,5]
b = a   # '='의 의미는 같다가 아닌 메모리 주소에 해당 값을 할당(연결)한다는 의미
a.sort()
print(b)

# 패킹 : 한 변수에 여러개의 데이터를 넣는 것
# 언패킹 : 한 변수의 데이터를 각각의 변수로 반환
t = [1,2,3] # 1,2,3을 변수 t 패킹
d,f,g = t # t에 있는 값을 언패킹
print(t,d,f,g)
