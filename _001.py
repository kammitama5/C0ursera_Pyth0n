# Ferm@t's Theorem

def check_fermat(a, b, c, n):
    input_value = ((a ** n) + (b ** n))
    output_value = (c ** n)
    if input_value == output_value:
      if n > 2:
        print("Holy Smokes, Fermat was wrong!")
      else:
        print("correct")
    else:
      print("No, that doesn't work")
      
      
check_fermat(1, 2, 3, 4)
check_fermat(2, 3, 4, 5)
check_fermat(1, 2, 2, 1)
    