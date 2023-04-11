try:
  import pip
  pip.main(['install', '--user', '-r', 'requirements.txt'])
  print("Installation Successful")
except Exception as e:
  print("Installation not successful")
  print(e)
finally:
  print("Execution Complete.")
