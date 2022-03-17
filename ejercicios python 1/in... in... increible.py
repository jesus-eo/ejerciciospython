def stutter(nombre):
  x = nombre[0:2]
  y = nombre + '?'
  print(f"{x}...{x}...{y}")

print(stutter("incredible"))

def hola(palabra):
  a = palabra[0:2]
  b = palabra + '?'
  c = a + '... '
  return (c + c + b)

print(hola("enthusiastic"))
