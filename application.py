from flask import *
import numpy
import requests
from PIL import Image
# import json

# from tensorflow.keras.preprocessing import image
# from keras.models import load_model




result_reply = {0:"'Name_en':'Burger','Name_hi':'बर्गर','Name_mr':'बर्गर','Name_ta':'பர்கர்','en_description':'Let me describe a burger to you. A burger is a culinary delight that combines various flavors and textures to create a mouthwatering experience. Imagine a soft, toasted bun enveloping a juicy patty made from the finest meats or plant-based alternatives. The patty is expertly seasoned, grilled to perfection, and topped with melting cheese that adds a creamy richness. To enhance the burger, we layer it with crisp lettuce, ripe tomato slices, and tangy pickles for a satisfying crunch. A generous spread of zesty sauces like ketchup, mustard, or mayonnaise completes this masterpiece. Each bite offers a symphony of savory, smoky, and tangy notes that will leave you craving for more. A burger is not just a fast-food item; it is a culinary creation that satisfies both the palate and the soul.','hin_description':'आइए मैं आपको एक बर्गर का वर्णन करूँ। एक बर्गर एक खाद्य खज़ाना है जो विभिन्न स्वाद और बनावटों को मिलाकर एक मज़ेदार अनुभव पैदा करता है। किसी सॉफ़्ट, टोस्टेड बन में एक नरम पैटी भरी हुई हो, जो बेहतरीन मांस या प्लांट-आधारित विकल्पों से बनी हो। पैटी को मसाले से सजाया जाता है, परफ़ेक्ट ग्रिल किया जाता है, और उस पर मेल्ट हो जाने वाला पनीर रखा जाता है जो इसमें क्रीमी पानी देता है। बर्गर को और बेहतर बनाने के लिए, हम इसमें ताजगी भरे हुए पत्ते वाली सलाद, पके हुए टमाटर के टुकड़े और तीखे अचार रखते हैं जो चबावन्नी सुखदारी प्रदान करते हैं। केचप, मस्टर्ड, या मेयोनेज़ जैसी चटनीयों का विशाल अपवाद इस महाकृति को पूरा करता है। प्रत्येक भोजन बर्गर में मिश्रित नमकीन, धूम्रपान और तीखा स्वाद देता है, जो आपको और अधिक बढ़-चढ़कर खाने के लिए विक्षिप्त कर देगा। बर्गर केवल एक फ़ास्ट-फ़ूड आइटम नहीं है; यह खाद्य निर्माण है जो न केवल जीभ को संतुष्ट करता है, बल्कि आत्मा को भी प्रसन्न करता है।','marathi_description':'एक शेफ म्हणून, माझं आपल्याला बर्गरचं वर्णन करायला द्या. बर्गर हा एक खाद्यात्मक खाजगी आहे ज्याने आपली जीभाला त्याच्या चवदार स्वादाने बघायला देतं. पाहा: आपली जीभ बघत आहे की, त्याच्या आरामासाठी आंदळीला टोस्ट केलेला पाव एका रसदार आणि ताजेतवारीतून वापरणारा पैटीच्या घोलाने घटवलेला आहे. त्या पैटीला परिपूर्णतेने मसालेने साजवलेलं आहे, त्याची शेवटचीच चव ठेवण्यासाठी अवघड ग्रिल केलं आहे आणि त्याच्यावर मोठ्या पावसारखं घडवलेलं पनीर ठेवलं आहे ज्याने त्यात क्रीमी मऊ भरलं आहे. त्याच्या अपेक्षेनुसार, आपण त्यात स्वादिष्ट, ताज्या लचकणारी सलाद, पिकलेल्या टोमॅटो तुकडे आणि चटपटीत अचार ठेवतो. केचप, मस्टर्ड, किंवा मेयोनेज याप्रमाणे मिठास देणारी चटणींची अवधारणा या रचनेच्या पूर्णतेने करतात. प्रत्येक एक खाण्याचं संगणक खाण्यांमध्ये मिश्रित चव, धूम्रपान आणि थोडं चवकट स्पष्टीकरण देतं ज्यामुळे तुम्हाला अधिक काढण्याची इच्छा वाढेल. बर्गर केवळ एक फ़ास्ट-फ़ूड अवयव नाही; तो आहे एक खाद्य कलाकृती आहे ज्या जीभाला मग आत्मा दोन्हां तृप्त करते.','tamil_description':'நான் உங்களுக்கு ஒரு பர்கரை விவரிக்கிறேன். ஒரு பர்கர் என்பது ஒரு சமையல் மகிழ்ச்சியாகும், இது பல்வேறு சுவைகள் மற்றும் அமைப்புகளை ஒருங்கிணைத்து ஒரு சுவையான அனுபவத்தை உருவாக்குகிறது. ஒரு மென்மையான, வறுக்கப்பட்ட ரொட்டி சிறந்த இறைச்சிகள் அல்லது தாவர அடிப்படையிலான மாற்றுகளிலிருந்து தயாரிக்கப்பட்ட ஒரு ஜூசி பாட்டியை மூடுவதை கற்பனை செய்து பாருங்கள். பஜ்ஜி திறமையாக சுவையூட்டப்பட்டு, கச்சிதமாக வறுக்கப்பட்டது, மேலும் கிரீமி செழுமையைச் சேர்க்கும் உருகும் சீஸுடன் முதலிடம் வகிக்கிறது. பர்கரை மேம்படுத்த, மிருதுவான கீரை, பழுத்த தக்காளித் துண்டுகள் மற்றும் கசப்பான ஊறுகாயுடன் ஒரு திருப்திகரமான க்ரஞ்சிற்காக அடுக்குகிறோம். கெட்ச்அப், கடுகு அல்லது மயோனைஸ் போன்ற சுவையான சாஸ்களின் தாராளமாக பரவுதல் இந்த தலைசிறந்த படைப்பை நிறைவு செய்கிறது. ஒவ்வொரு கடியும் சுவையான, புகைபிடிக்கும் மற்றும் கசப்பான குறிப்புகளின் சிம்பொனியை வழங்குகிறது, இது உங்களை மேலும் ஏங்க வைக்கும். பர்கர் என்பது துரித உணவுப் பொருள் மட்டுமல்ல; இது அண்ணம் மற்றும் ஆன்மா இரண்டையும் திருப்திப்படுத்தும் ஒரு சமையல் படைப்பு.'"}






#doing ocr to scanning menu items
import easyocr
def recognize_text(img_path):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path, detail=0)



#identifying food image using model
from tensorflow.keras.preprocessing import image
from keras.models import load_model
food_model = load_model('model_v1_inceptionV3.h5')
def classify(file_path):
    img_ = image.load_img(file_path, target_size=(299, 299))
    img_array = image.img_to_array(img_)
    img_processed = numpy.expand_dims(img_array, axis=0)
    img_processed /= 255.

    prediction = food_model.predict(img_processed)

    index = numpy.argmax(prediction)
    # description = classes[index]
    return index

#translation
from googletrans import Translator
def translate(sent, lang):
    translator = Translator()
    text = translator.translate(sent, src="auto", dest=lang)
    return text.text


app = Flask(__name__)

#home
@app.route('/')
def index():
    return "welcome to app"

#food identification
@app.route('/predict', methods=['GET', 'POST'])
def food_identify():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['img']
        #f = request.get_json()
        #img_url = f["url"]
        #img = Image.open(requests.get(img_url, stream = True).raw)
        f.save("img.jpg")
        # Make prediction
        result = classify("img.jpg")
        #f = open('data.json')
        return result_reply[result]
    return None

#menu scanner
@app.route('/menu', methods=['POST'])
def menu_scan_api():
    if request.method == 'POST':
        f = request.files['img']
        #f = request.get_json()
        #img_url = f["url"]
        #img = Image.open(requests.get(img_url, stream = True).raw)
        f.save('img_menu.jpg')
        result = recognize_text('img_menu.jpg')
        return result
    return None

#translation
@app.route("/translate", methods=["POST","GET"])
def translate_():
    if request.method == "POST":
        # if "sentence" not in request.form:
        #     flash("NO sentence post")
        # elif request.form['sentence'] == '':
        #     flash("no sentence")
        # else:
        #     sent = request.form['sentence']
        #     translated = translate.translation(sent)
        #     return translated
        data = request.get_json()
        sent = data["sent"]
        lang = data["lang"]
        result = translate(sent, lang)
        return result
    return None

# audio file
import pyttsx3
@app.route('/audio',methods=['POST'])
def audio_api():
    if request.method == 'POST':
        data = request.get_json()
        sentence = data['sent']
        result = audio_generation(sentence)
        # @after_this_request
        # os.remove('test.mp3')
        return send_file(result)

def audio_generation(sentence):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.save_to_file(sentence, 'test.mp3')
    engine.runAndWait()
    return "test.mp3"


if __name__ == '__main__':
    app.run()
