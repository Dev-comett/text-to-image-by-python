import pywhatkit as pw

txt=input("enter your text to convert into image")

pw.text_to_handwriting(txt,"sample",[255,0,0])
print("end")