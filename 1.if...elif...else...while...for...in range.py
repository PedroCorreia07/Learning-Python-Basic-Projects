
score=int(input("What is the score?"))
if score>=50 and score<=100:
    print(f"You have passed with {score}")
elif score<50 and score>=0:
    print(f"You have failed with {score}")
    valor_falta=0
    score_final=score+valor_falta
    while score+valor_falta!=50: #enquanto o score+valor em falta != (not equal) a 50
        valor_falta+=1
    for i in range(3):
        print("Calculating...")
    print(f"You have failed for {valor_falta} percent")
else:
    passou="Not valid value"
    print(passou)



