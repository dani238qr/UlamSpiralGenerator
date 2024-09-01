import turtle
import time
import math

max_n=int(input("Size of spiral: "))
font_size=int(input("Font size(3 or smaller for spiral > 2000: "))

def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2== 0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2) == 0:
            return False
        i +=6
    return True

prime_count = 0
last=None

def draw():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    global prime_count, last
    x,y=0,0
    num=1
    stepsX,stepsY=2,1
    
    try:    

        while num<=max_n:
            # RIGHT
            for _ in range(stepsX):
                if is_prime(num):
                    prime_count+=1
                    turtle.color('red')
                    last=num
                   # print(num)
                else:
                    turtle.color('white')
                x+=20
                turtle.setposition(x,y)
                turtle.write(f'{num}',move=False,align='center',font=("Arial",font_size, "normal"))
                num +=1
            stepsY +=1

            if num > max_n:  
                break

            # UP
            for _ in range(stepsY):
                if is_prime(num):
                    prime_count+=1
                    turtle.color('red')
                    last=num
                   # print(num)
                else:
                    turtle.color('white')
                y +=20
                turtle.setposition(x,y)
                turtle.write(f'{num}', move=False,align='center',font=("Arial", font_size, "normal"))
                num +=1
            stepsX +=1

            if num > max_n:  
                break


            # LEFT
            for _ in range(stepsX):
                if is_prime(num):
                    prime_count+=1
                    turtle.color('red')
                    last=num
                    #print(num)
                else:
                    turtle.color('white')
                x -=20
                turtle.setposition(x, y)
                turtle.write(f'{num}', move=False, align='center',font=("Arial", font_size, "normal"))
                num +=1
            stepsY +=1

            if num > max_n:  
                break


            # DOWN
            for _ in range(stepsY):
                if is_prime(num):
                    prime_count+=1
                    turtle.color('red')
                    last=num
                    #print(num)
                else:
                    turtle.color('white')
                y -=20
                turtle.setposition(x, y)
                turtle.write(f'{num}',move=False,align='center',font=("Arial", font_size, "normal"))
                num +=1
            stepsX +=1

            if num > max_n:  
                break


        print(f"Last number: {num-1}")
        print(f"Last prime number: {last}")
        print(f"Total prime numbers: {prime_count}")
        #turtle.bye()

    except turtle.Terminator:

        print(f"Last number: {num-1}")
        print(f"Last prime number: {last}")
        print(f"Total prime numbers: {prime_count}")
        turtle.bye()

def main():

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor('black')
    
    draw()
    screen.mainloop()

main()

