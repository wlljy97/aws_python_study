
def main():
    from userManagement.view.MenuView import MenuView # 모듈명 -> 'MenuView' import 'MenuView' <-클래스명
    while(MenuView.index()):
        pass

if __name__ == "__main__":
    main()
    print("프로그램이 종료되었습니다.")