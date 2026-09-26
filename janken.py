import random
hands=["グー","チョキ","パー"]
win=0
lose=0
draw=0

for i in range(3):
     player=input("グー、チョキ、パーどれかを入力:")
     computer=random.choice(hands)

     print("あなた:"+player)
     print("コンピュータ:"+computer)

if player==computer:
     print("あいこ！")
     draw+=1

elif(player=="グー"and computer=="チョキ")or\
 (player=="チョキ"and computer=="パー")or\
 (player=="パー"and computer=="グー"):
     print("あなたの勝ち！")
     win+=1

else:
     print("あなたの負けｗ")
     lose+=1

print("-----結果-----")
print("勝ち:"+str(win))
print("負け:"+str(lose))
print("あいこ:"+str(draw))
