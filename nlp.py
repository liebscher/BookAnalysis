import RAKE

Rake = RAKE.Rake(RAKE.SmartStopList())

with open('sample.txt', 'r') as file:
    txt = file.read()

    print([elm[0] for elm in Rake.run(txt, minCharacters = 3, maxWords = 5, minFrequency = 1)])
