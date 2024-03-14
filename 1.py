i = 1

while i <= 9:
  j = 1
    
   while j <= i:
        
        result = i * j
       
        print(f"{j} x {i} = {result}", end="\t")

         if result < 10:
            print('\t', end='')
        
   j += 1

  i += 1
    
    print()
