def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15
 class FahrenheitToCelcius(TemperatureConversion):
    def conversion(self):
        return (self._temp - 32) * 5/9
 class KelvinToCelcius(TemperatureConversion):
    def conversion(self):
        return self._temp - 273.15


 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")
 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
 convert = FahrenheitToCelcius(tempInFahrenheit)
 print(str(convert.conversion()) + " Celcius")
 tempInKelvin = float(input("Enter the temperature in Kelvin: "))
 convert = KelvinToCelcius(tempInKelvin)
 print(str(convert.conversion()) + " Celcius")



main()








