# 민생회복 지원금 신청 프로그램
birth_year = input("출생년도를 입력하세요.")
last_digit = birth_year[-1] # 출생연도 끝자리 선택
#print(last_digit)
#출생년도가 1900년보다 작거나 2006년 보다 큰 경우
#"출생년도는 1900년부터2006년 사이여야 됩니다." 출력"

if int(birth_year) < 1900 or int(birth_year) > 2006:
    print(f"출생년도는 1900년부터2006년 사이여야 됩니다. 다시 입력하세요")
else:    
    if last_digit == "1" or last_digit == "6":
        print("신청일은 월요일입니다")
    elif last_digit == "2" or last_digit == "7":   
        print("신청일은 화요일입니다")
    elif last_digit == "3" or last_digit == "8":   
        print("신청일은 수요일입니다")
    elif last_digit == "4" or last_digit == "9":   
        print("신청일은 목요일입니다")
    elif last_digit == "5" or last_digit == "0":   
        print("신청일은 금요일입니다")
    else:
        print("신청요일이 없습니다.")                



