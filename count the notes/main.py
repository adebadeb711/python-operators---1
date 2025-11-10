Amount =int(input("Please Enter Amount for Withdrawal:"))

note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print(note1 , "notes of 100 taka")
print(note2 , "notes of 50 taka")
print(note3 , "notes of 10 taka")