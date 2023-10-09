num1=float(input("Enter a number:"))
operator=input("Enter the operator:")
num2=float(input("Enter second number:"))
match operator:
	case "+":print("Sum is ",num1+num2)
	case "-":print("Difference is",num1-num2)
	case "*":print("Product is",num1*num2)
	case "/":print("Division is",num1/num2)
	case "%":print("Modulo is",num1%num2)