# pip       : pypi.org 에서 코드를 본인의 컴퓨터에 설치하는것
# import    : 다른 파일의 클래스, 함수, 변수를 가져다 사용함
import googletrans
from googletrans import Translator
 

 
text1 = "Hello welcome to my website!"

 
translator = Translator()
trans1 = translator.translate(text1, src='en', dest='ja')
print("English to Japanese: ", trans1.text)
print(googletrans.LANGUAGES)