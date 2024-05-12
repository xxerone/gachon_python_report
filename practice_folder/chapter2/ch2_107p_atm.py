itemPrice = int(input("물건값을 입력하시오: ")) 
coin1000 = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: ")) 
coin100 = int(input("100원 동전개수: "))

change = coin1000*1000 + coin500*500 + coin100*100 - itemPrice

print(change)

nCoin500 = change//500
change = change%500

nCoin100 = change//100
change = change%100

nCoin10 = change//10
change = change%10

nCoin1 = change//1
change = change%1

print(f"500원: {nCoin500}개, 100원: {nCoin100}개, 10원: {nCoin10}개, 1원: {nCoin1}개")
