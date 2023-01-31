import random
GameOver=ValueError
# number --> kopyuter oylagan son
# guess  --> Foydalanuwchi tahmin qilgan son

# a=0
# while (a<3):
#         print(a)
#         a += 3

def chek_number(number, guess):
    if number > guess:
        return"Men oylangan sondan kichik son kirittingiz"
    if number < guess:
        return"Men oylangan sondan katta son kirittingiz"
    raise GameOver
# a=0
# while (a<3):
#     print(a)
#     a += 3
    
   
def main():
    number = random.randint(1,10)
    print(f"Salom taxmin oyinimizga hush kelibsiz . O'ylagan sonimni toping{number}")
    
    guess = int(input("Tahminingizni kiriting :"))
    
    a=0
    while (a<2):
        print(a)
        a +=1
    
    # if  (guess(3)): 


    while True:
       
        try :


            

            message = chek_number(number, guess)
            print(message)
            guess = int(input("Tahminingizni kiriting :"))

        except GameOver:

            print("Tabriklaymiz")
        
        a += 1
        break

       
if __name__=="__main__":
    main()