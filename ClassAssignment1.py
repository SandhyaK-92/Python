class multipleFunctions():
    
    def Subfields():
        aisubfields = ('Sub-fields in AI are:', 
                 'Machine Learning',
                 'Neural Networks', 
                 'Vision',
                 'Robotics', 
                 'Speech Processing', 
                 'Natural Language Processing')
        print("\n".join(aisubfields))


    
    def OddEven():
        num = int(input("Enter a number:"))
       
        if(num%2==0):
            print(num,"is Even number")
            check = "Even number"
        else:
            print(num,"is Odd number")
            check = "Odd number"

            

    def eligible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
    
        if Gender == "Male" and Age < 21:
            print("NOT ELIGIBLE")
            check = "NOT ELIGIBLE"
    
        elif Gender == "Male" and Age >= 21:
            print("ELIGIBLE")
            check = "ELIGIBLE"
    
        elif Gender == "Female" and Age < 18:
            print("NOT ELIGIBLE")
            check = "NOT ELIGIBLE"
    
        elif Gender == "Female" and Age >= 18:
            print("ELIGIBLE")
            check = "ELIGIBLE"
    
        
        return check
        

   
           
        def add(Subject1, Subject2, Subject3, Subject4, Subject5):
                     total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
                     return total
        def percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
                     total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
                     return (total / 500) * 100
                
        def triangle(Height,Breadth):
            area = (Height*Breadth)/2
            return area
        
        def perimeter(Height1,Height2,Breadth):
            return Height1+Height2+Breadth
                    
            

