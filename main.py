from conversor_medidas import ConversorMedididas
from converterter_temperatura import ConverterTemperatura

print('''
[1]. Centimeters to Meters
[2]. Meters to Centimeters
[3]. Celsius to Fahrenheit
[4]. Fahrenheit to Celsius
''')

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = ConversorMedididas.converte_cm_para_m(value)
elif choice == '2':
    result = ConversorMedididas.converte_m_para_cm(value)
elif choice == '3':
    result = ConverterTemperatura.celsius_to_fahrenheit(value)
else:
    result = ConverterTemperatura.fahrenheit_to_celsius(value)
    
print('Result:', result)