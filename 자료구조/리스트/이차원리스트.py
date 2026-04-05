# 이차원 리스트
matrix = [
    [1 ,2, 3],
    [4, 5, 6]
]

print(matrix)
print(type(matrix)) #<class 'list'>

# 행 출력
print(matrix[0]) #[1, 2, 3]
print(matrix[1]) #[4, 5, 6]

#특정 요소(값) 출력
print(matrix[0][0]) #1
print(matrix[0][1]) #2
print(matrix[0][2]) #3

# 전체 요소 출력 - 중첩 for
# row는 행(리스트) 반복, row에서 val(요소) 순회
for row in matrix:
    for val in row:
        print(val, end= " ")
    print()
print(row, end= " ")            


# 요소 변경
matrix[1][0] = 10
print(matrix) #[[1, 2, 3], [10, 5, 6]]

# 리스트 추가
matrix.append([7, 8, 9])
print(matrix) #[[1, 2, 3], [10, 5, 6], [7, 8, 9]]

# 리스트 삭제
del matrix[1] #2행 [[1, 2, 3], [7, 8, 9]]
print(matrix) 
