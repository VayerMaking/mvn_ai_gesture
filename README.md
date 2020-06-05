# MVN A.I.



Система,която разпознава жестове с помощта на изкуствения интелект и извършва определени операции спрямо тях.



## Като за начало

    git clone https://github.com/VayerMaking/mvn_ai_gesture

## Инсталиране на нужните библиотеки

  1. За хора с хубави видео карти на Nvidia

    pip install -r requirements_gpu.txt

  2. За хора без

    pip install -r requirements_cpu.txt

## Инструкции за стартиране на проекта


##Създаване на жест

Първо направете хистограма на ръката ви. Не е нужно да го правите отново, ако вече сте го направили. Но вие трябва да го направите, ако условията на осветление се променят. За целта въведете командата, дадена по-долу и следвайте инструкциите по-долу.

    python set_hand_hist.py

-Ще се появи прозорец "Set hand histogram" ще се появи.
-"Set hand histogram" ще има 50 квадрата (5x10).
-Сложи си ръката на тези квадратчета. Уверете се, че ръката ви покрива всички квадрати.
-Натиснете 'c'. 1 друг прозорец ще се появи "Thresh ".
-При натискане на "c" на прозореца на "Thresh" трябва да се появят само бели петна, съответстващи на частите на изображението, които са с цвета на кожата ви.
-Уверете се, че всички квадрати са покрити от ръката ви.
-Ако не успеете, преместете ръката си малко и натиснете "c" отново. Повторете това, докато получите добра хистограма.
-След като получите добра хистограма натиснете 's', за да запази хистограмата. Всички прозорци се затварят.

2.За да създадете свои собствени жестове или замените нашите жестове, направете следното. Това се прави от командата, дадена по-долу. При стартиране на изпълнението на тази програма, ще трябва да въведете номера на жеста и името на жеста или текст. След това OpenCV прозорец, наречен "Capturing gestures",  ще се появи.Ще видите зелен прозорец (вътре ще трябва да направите вашия жест) и брояч, който брои броя на снимките, съхранени.

    python create_gestures.py


3.Когато приключите с добавянето на нови жестове, стартирайте файла load_images.py веднъж. Не е необходимо да стартирате този файл отново, докато не добавите нов жест.

    python load_images.py

##Тестване на жестове

Използваме модела на Keras, тъй като зареждането на модела в паметта и използването му за разпознаване е по-лесно.
1)Създаваме жест,както е показано по-горе
2)За разпознаване стартирайте файла recognize_gesture.py.

    python recognize_gesture.py

3)Ще имате малка зелена кутия, в която трябва да направите  жестовете си.
## Използвани технологии
[keras](https://keras.io/) - Keras е библиотека с невронна мрежа с отворен код, написана на Python. Той може да работи над TensorFlow, Microsoft Cognitive Toolkit, R, Theano или PlaidML. Създаден, за да позволи бързи експерименти с дълбоки невронни мрежи, той се фокусира върху това да бъде удобен за потребителя, модулен и разтегателен

[Tensorflow](https://www.tensorflow.org/) - TensorFlow е безплатна и с отворен код софтуерна библиотека за поток от данни и диференциално програмиране в редица задачи.Това е символична математическа библиотека и се използва също за приложения за машинно обучение като невронни мрежи.

[Raspberr Pi 3b+](https://www.raspberrypi.org/) - Raspberry Pi или RPI е серия от едноплаткови компютри с размери на кредитна карта, разработена в Обединеното кралство от специално създадена за целта фондация (Raspberry Pi Foundation) с цел популяризиране на обучението по основи на компютърните науки в училищата.[

[Python](https://www.python.org/) - Python е интерпретируем, интерактивен, обектно-ориентиран език за програмиранe




## Информация за авторите на проекта (задължително)

Мартин Вайер - програмист/хардуерист - [VayerMaking](https://github.com/VayerMaking)

Владислав Колев - програмист

Никола Маноилов - програмист/дизаинер
