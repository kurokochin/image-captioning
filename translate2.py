from googletrans import Translator
import io
import time

domains = ['translate.google.ac', 'translate.google.ad', 'translate.google.ae', 'translate.google.af', 'translate.google.ag', 'translate.google.al', 'translate.google.am', 'translate.google.as', 'translate.google.at', 'translate.google.az', 'translate.google.ba', 'translate.google.be', 'translate.google.bf', 'translate.google.bg', 'translate.google.bi', 'translate.google.bj', 'translate.google.bo', 'translate.google.bs', 'translate.google.bt', 'translate.google.by', 'translate.google.ca', 'translate.google.cc', 'translate.google.cd', 'translate.google.cf', 'translate.google.cat', 'translate.google.cg', 'translate.google.ch', 'translate.google.ci', 'translate.google.cl', 'translate.google.cm', 'translate.google.cn', 'translate.google.cv', 'translate.google.cz', 'translate.google.de', 'translate.google.dj', 'translate.google.dk', 'translate.google.dm', 'translate.google.do', 'translate.google.dz', 'translate.google.ec', 'translate.google.ee', 'translate.google.es', 'translate.google.fi', 'translate.google.fm', 'translate.google.fr', 'translate.google.ga', 'translate.google.ge', 'translate.google.gf', 'translate.google.gg', 'translate.google.gl', 'translate.google.gm', 'translate.google.gp', 'translate.google.gr', 'translate.google.gy']

print("Starting processing source...")
with open('captions.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print("Finish processing source!!!")

i = 0
j = len(domains) - 1
while(i <= 1000):
    translator = Translator(service_urls=[domains[j % len(domains)]])
    print("Starting translations from {} to {}".format(i, i+499))
    try:
        translations = translator.translate(content[i:i+500], dest='id')
    except Exception as e:
        print(e)
        print("Retrying...")
        j += 1
        continue

    print("Finish translations!!!")

    result = ""
    print("Starting parse result...")
    for translation in translations:
        result += translation.text + "\n"
    print("Finish parse result!!!")

    print("Writing to file...")
    with io.open('captions-indonesia/captions-indonesia-{}-{}.txt'.format(i, i+499), 'w+', encoding="utf-8") as f:
        f.write(result)
    print("Finish write to file from {} to {}!!!".format(i, i+499))

    i += 500
    j -= 1
    print('')
    time.sleep(1)
