def dia_da_semana(n):
   match n:
      case 0: return "Segunda"
      case 1: return "Terca"
      case 2: return "Quarta"
      case 3: return "Quinta"
      case 4: return "Sexta"
      case 5: return "Sabado"
      case 6: return "Domingo"
      case _: return "Numero do dia invalido"
print (dia_da_semana(3))
print (dia_da_semana(6))
print (dia_da_semana(7))