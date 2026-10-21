import math
import calc as ca 

def read_num(prompt):
   try:
      value=float(input(prompt))
   except ValueError:
      return None

   if not math.isfinite(value):
      return None
   if value.is_integer:
      return int(value)
   else:
      return value

def calculate(choice):
   symbol=ca.OPERATIONS[choice][1]
   count=read_num("HOW MANY NUMBER DO WANT CALCULATE:")
   if not isinstance(count , int) or count < 2 :
     print("Please enter the whole numbers atleast 2")
     return      

   numbers=[]
   for i in range(1,count +1):
      number=read_num(f"enter the number{i}: ")
      if number is None:
          print("Enter the valid number")
      numbers.append(number)

   result=ca.calculate_num(choice,numbers) 
   if result is False:
      print("cannot divide by zero")
      return
   print(f"{symbol}".join(map(str,numbers))+ f"={ca.clean(result)}")


def exponential():
   base=read_num("ENTER THE BASE NUMBER: ")
   power=read_num("ENTER  POWER NUMBER  FOR BASE : ")
   if base is None or power is None or abs(power) >100:
      print("INVALID INPUT(please enter the exponent below 100) ")
      return 
   result=ca.power_calc(base,power)
   if result is False :
     print("cannot calculate this power")
   elif isinstance(result,complex):
      print("result is not a real number")
   else:
      print(f"{base}**{power}={ca.clean(result)}")

def expression():
   text=input("ENTER THE EXPRESSION (eg. 2(3 +12)-12): ").strip()
   result=ca.expression_calc(text)
   if result is None:
      print("INVALID EXPRESSION")
   elif result is False :
      print("CANNOT DIVIDE BY ZERO")
   else:
      print(f"{text}={ca.clean(result)}")

def main():
   print("YOUR CALCULATOR") 
   print("="*20) 


   while True:
      Choice=read_num(
         "1. Add\n2. Subract\n3. Multiply\n4. Divide\n5.Expotential\n6. Expression\n7. exit\n ENTER YOUR CHOICE: calculator"
      )      


      match Choice :

         case 1 | 2 | 3 | 4:
           calculate(Choice)     
         case 5:
            exponential()
         case 6:
            expression() 

         case 7:
            print("THANK YOU")
            break
         case _:
            print("enter your choice between (1 to 7): ")     
if __name__ == "__main__":
   main()
