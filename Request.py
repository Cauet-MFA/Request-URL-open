import urllib.request
try:
  site = urllib.request.urlopen("https://www.google.com.br")
except:
  print("O site não pode ser acessado")
else:
  print("O site foi acessado com sucesso!")
  print(site.read())
