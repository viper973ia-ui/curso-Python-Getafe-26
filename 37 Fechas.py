import datetime

print(f"fecha de hoy: {datetime.date.today()}")
print(f"hora actual:  {datetime.datetime.now().time()}")   
f_posterior=datetime.datetime.now()+datetime.timedelta(days=20,hours=60)

print (f_posterior)

fecha_actual=datetime.datetime.now()
print(f"La fecha y hora actuales {datetime.datetime.strftime(fecha_actual,"%d/%m/%Y - %H:%M:%S")}")



