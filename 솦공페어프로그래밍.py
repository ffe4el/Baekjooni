import sys
arr = []

def load_todo_list():
    with open("/Users/sola/Documents/GitHub/Baekjooni/테스트.txt", "r") as f:
        print("현재 To-Do List: ")
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())

def add_task(count):
    file = open('/Users/sola/Documents/GitHub/Baekjooni/테스트.txt', 'w')
    print("새로운 할 일을 입력하세요: ", end="")
    to_do = input()
    print(f"새로울 할 일 '{to_do}'가 To-Do List에 추가되었습니다.")
    file.write(f'{count}. '+to_do)
    file.close()

def main():
    print("1. To-Do List 불러오기")
    print("2. 새로운 할일 추가하기")
    choice = int(input("선택하세요 (1 또는 2): "))
    count = 0
    if choice ==1:
        load_todo_list()

    elif choice ==2:
        count += 1
        add_task(count)



if __name__ == "__main__":
    main()