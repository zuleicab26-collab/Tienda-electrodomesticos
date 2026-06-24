print("Bienvenido a Electrodomesticos Computron")
nombre = input("Por favor ingrese su nombre para la factura:")
correo = input("Ingrese su correo para la facturacion:")
ci_Ruc = int(input("Ingrese su CI O RUC:"))

lp = ("Laptop")
mo = ("Mouse") 
si = ("Silla")
esc = ("Escritorio")
Te = ("Teclado")
Li = ("Librero")
 
lp_ = ("1200")
mo_ = ("25") 
si_ = ("350")
esc_ = ("500")
Te_ = ("70")
Li_ = ("200")

Cate = ("Tech")
Categ = ("Mueble")

s_stock = ("0 unidades disponibles")
b_stock = ("1 a 5 unidades disponibles")
n_stock = ("6 o mas unidades disponibles")

for i in range(1):
 print("i + Sin stok:",esc )
 print("i + Stock bajo:", si)
 print("i +Stock bajo:", lp)

 print("____________Inventario______________")
 print("1. Laptop.....................$1200")
 print("2. Mouse......................$25")
 print("3. Silla......................$350")
 print("4. Escritorio.................$500")
 print("5. Teclado....................$75")
 print("6. Librero....................$200")
 elec = int(input("Por favor ingrese el producto que desee adquirir:"))
 if elec == 1:
     print("Ha seleccionado: La opcion", lp)
     print("Categoria:", Cate)
     print("Valor a pagar:", lp_) 
     print("Unidades disponibles:", b_stock)
 elif elec == 2:
     print("Ha seleccionado: La opcion", mo)
     print("Categoria:", Cate)
     print("Valor a pagar:", mo_) 
     print("Unidades disponibles:", n_stock)
 elif elec == 3:
     print("Ha seleccionado: La opcion", si)
     print("Categoria:", Categ)
     print("Valor a pagar:", si_) 
     print("Unidades disponibles:", b_stock)
 elif elec == 4:
     print("Ha seleccionado: La opcion", esc)
     print("Categoria:", Categ)
     print("Valor a pagar:", esc_) 
     print("Unidades disponibles:", s_stock)
 elif elec == 5:
     print("Ha seleccionado: La opcion", Te)
     print("Categoria:", Cate)
     print("Valor a pagar:", Te_) 
     print("Unidades disponibles:", n_stock)
 elif elec == 6:
     print("Ha seleccionado: La opcion", Li)
     print("Categoria:", Categ)
     print("Valor a pagar:", Li_) 
     print("Unidades disponibles:", n_stock)
 else:
     print("Valor no valido, por favor ingrese bien")