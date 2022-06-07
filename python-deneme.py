python_deneme = open("python_deneme.txt" , "w") # w r a 
text = "deneme"
python_deneme.write(text)
python_deneme.close()
python_deneme=open("python_deneme.txt" , "a")
python_deneme.write("\nDENEME")
python_deneme.write("\n2022\n")
python_deneme.close()
