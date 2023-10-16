import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('survey.db')

# 커서 생성
cursor = conn.cursor()

# 설문 시작
while True:
    print("★좋아하는 음식 종류 설문조사★")
    print("1.설문 참여하기")
    print("2.설문 현황보기")
    print("3.종료")
    # 참여할지 현황볼지 종료할지 선택
    a = int(input("선택:"))
    # 설문 참여하기
    if a == 1:
        cursor.execute("SELECT * FROM FOOD")
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"{row[0]}. {row[1]}")
        print("0. 기타(직접입력)")

        b = int(input("선택:"))

        if b == 0:
            # 추가할 음식 입력
            c = input("음식 종류 입력:")
            cursor.execute("INSERT INTO FOOD (TYPENAME,VOTE) VALUES (?, ?)", (c,0))
            conn.commit()
        else:
            # 투표 추가
            cursor.execute("UPDATE FOOD SET VOTE = VOTE + 1 WHERE NUM = (?)",(b,))
            conn.commit()
    # 설문 현황보기
    elif a == 2:
        # 푸드 테이블에서 모든 데이터 가져오기
        cursor.execute("SELECT * FROM FOOD")
        rows = cursor.fetchall()

        # 결과 출력
        for row in rows:
            print(f"{row[0]}. {row[1]} ===> {row[2]}표")
    # 프로그램 종료
    elif a == 3:
        print("프로그램이 종료되었습니다.")
        break

# 커서와 연결 닫기
cursor.close()
conn.close()

