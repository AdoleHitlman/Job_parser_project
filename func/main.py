# Начало работы программы
input("для начала нажмите 'enter'")


from api import SuperJobAPI,HeadHunterAPI
from output import main_menu
from choice import choice_one,choice_two,choice_three,coice_four,choice_five,end_question



#Тело программы
def user_interaction():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    while True:
        choice = main_menu()
        if choice == '1':
            choice_one(hh_api)
            if not end_question():
                break
        elif choice == "2":
            choice_two(superjob_api)
            if not end_question():
                break
        elif choice == "3":
            choice_three(hh_api, superjob_api)
            if not end_question():
                break
        elif choice == "4":
            coice_four()
            if not end_question():
                break
        elif choice == "5":
            choice_five()
            if not end_question():
                break
        elif choice == "0":
            break


if __name__ == "__main__":
    user_interaction()
    input("Для завершения программы нажмите 'Enter'")
