from googletrans import Translator
import io
import time

translator = Translator(service_urls=[
        'translate.google.co.id',
    ], timeout=10)

print("Starting processing source...")
with open('captions.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print("Finish processing source!!!")

i = 202500
while(i <= 413720):
    print("Starting translations from {} to {}".format(i, i+499))
    translations = translator.translate(content[i:i+500], dest='id')
    print("Finish translations!!!")

    print("Starting parse result...")
    result = ""
    for translation in translations:
        result += translation.text + "\n"
    print("Finish parse result!!!")

    print("Writing to file...")
    with io.open('captions-indonesia\captions-indonesia-{}-{}.txt'.format(i, i+499), 'w+', encoding="utf-8") as f:
        f.write(str(result))
    print("Finish write to file from {} to {}!!!".format(i, i+499))
    i += 500
    print('')
    time.sleep(500)
