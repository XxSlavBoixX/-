print("Как играть:")
print("Это новогодняя игра работает в стиле выбирай свое приключение, это значит, что вам даются ситуации и действия, Связанные сними, которые вы можете выполнять. Вам будет приведён текст, а за ним несколько Действий {Действие 1, Действие 2} Вы печатаете цифру действия, которое хотите исполнить, А затем нажимаете enter и вам даётся ещё текст и ещё действия. Классно поиграть!")
print("Старт Ночь с 24 на 25 декабря, вас будит неожиданный грохот у вашей входной двери. Один, два, три раза вы слышите этот жуткий звук, будто кто то старается снести вам дверь. Вы тихонько достаёте из под подушки ваш Глок - Снежок - 17  Модель Ёлка калибра 9 валенок х 19 чашек какао, вы убираете его в резинку штанов вашей пижамы и идёте в прихожую. Звук вроде прекратился. Вы решаетесь посмотреть в дверной глазок и видите как массивная красная фигура мчится к двери на полной скорости. Вы не успеваете отскочить, как дверь разлетается в дребезги и вас откидывает на метр назад, вы приземляетесь на лопатки еле в сознание, у вас ужасно болят рёбра с левой стороны, левая рука и голова, в глазах двоится. Вы видите, как в двери стоит эта гиганстская красная фигура в красном колпаке и красным костюме, по эго сторонам стоят грозные эльфы, ростом чуть меньше метра с бронежилетами из мандариновой кожуры и гирлянд. К вам в квартиру вломился злой Дед Мороз...")
print("Действие 1 Открыть Рождестенский огонь по разьярённому деду")
print("Действие 2 Спросить  какого снеговика он здесь делает")
a = input()
if a == "2":
    print("Он хохочет и своим глубоким голосом отвечает: Ох, Вы были плохими в зтом году! Не сдали зачёты, поставляли оружие в Ирак, Судан, Афганистан, Колумбию, Бразилию, Иран, Саудовскую Арабию, грабили первоклашек, кидали восьмые корсары в школьные туалеты и устраивали немыслимое количество политических переворотов и революций в северной Африке! В результате всего этого вы попали на мой список плохих детей, пора наказать тебя, хулигана!")
if a == "1":
    print("Вы хлёстко достаёте ваш праздничный ствол из пижам и делаете два выстрела в центр массы деда, гильзы из леденцов с треском падают на пол. За долю секунды до столкновения вокруг Морза образуется полу прозрачный щит, похожь на гигантскую ёлочную игрушку, пули с дребезгом разлетаются на фрагменты как только касаются этой праздничной но эффективной защиты. Он хохочет, щелкает пальцем и один из эльфов дает ему большую, длинную коробку, завёрнутую как подарок, Он не спеша её открывает и достает оттуда свой Benelli M3 Супер Санта 90 заряжан дробью из фантиков и осколков ёлочных игрушек калибра 12 саней / 70 эльфов. Вам Рождественский капец. Дед Мороз превращает вас в рождественское привидение экспресс способом и каждый год с 24 декабря по 1 Января Вы просыпаетесь чтобы терроризировать плохих мальчиков девочек. Вы обречены на вечность, не надо было стрелять в мороза без нормального прикрытия. Конец.")
if a != "1" and a!= "2":
    print("Такой опции нет")
if a == "1":
    SystemExit
if a == "2":
    print("Действие 1 Попробовать убежать от деда")
    print("Действие 2 Промолчать")
b = input()
if b == "1":
    print("Вы хлёстко достаёте ваш праздничный ствол из пижам и делаете четыре выстрела в пол перед дедом морозом, щепки от контакта с полом временно ослепляют деда мороза и его эльфов, вы быстро поднимаетесь и бежите через всю квартиру и в конце концов находите себя в тупике в кухне. Вы смотрите в окно и видите прямо под ним сани Деда Мороза, единственный выход из этой ситуации, это прыгнуть из окна в них...")
    print("Действие 1 Прыгать сейчас")
    print("Действие 2 Пострелять в Деда и эльфов")
c = input()
if c == "1":
    print("Вы решаетесь прыгнуть сейчас, не теряя времени вы простреливаете окно и прыгаете из него вы успешно приземляетесь в сани, в которых стоит эльф, который ими управляет...")
if c == "1":
    print("Действие 1 Сказать эму, чтобы тот свалил")
    print("Действие 2 Направить на бедного маленького эльфа свою праздничную пушку (совсем крыша поехала, да?)")
e = input()
if e == "1":
    print("Ельф вас понял и прыгает в сугроб под вами с ужасно смешным визгом, сани ваши…")
    print("Действие 1 Улететь куда подальше от этого безумия")
    print("Действие 2 Отомстить Деду, за то, что не дал поспать")
f = input()
if f == "1":
    print("1")
if f == "2":
    print("2")
qqSystemExit
if e == "2":
    print("Это был плохим решением, встроенный искусственный интеллект саней заметил чужое оружие в санях и сразу же инициировал процесс катапультирования эльфа и самоуничтожение саней , Вас превратили в новогодние привидение и последние что вы слышали перед этим, это смех улетающего эльфа (не надо обижать невинных эльфов…)")    
    SystemExit 
if e != "1" and e != "2":
    print("Такой опции нет")
if b == "2":
    print("Белая борода щелкает пальцами, ельфы достают две гигантские базуки раскрашенные как конфетные палочки и открывают по вам огонь, перый взрыв фантиков и мишуры пролетает мимо вашего правого уха, второй попадает к вам прямо под ноги, вас покрывать щепками и вас подкидывает до потолка, вы приземляетесь с грохотом. Он к вам медленно подходит и останавливается прямо перед вами. Всё ясно, Дед хочет войны...   Вы поднимаетесь с пола и говорите 'Ну давай попляшем, старик...'")
    print("Действие 1 Попробовать забайтить деда и просто прыгнуть из окна в гигансткий сугроб")
    print("Действие 2 Закончить это раз и на всегда")
d = input()
if d == "1":
    print("Вы мигом поворачивайтесь, открываете окно и прыгайте в сугроб, как только вы встаёте вы окружены отрядом эльфов, которые похожи стояли по всему периметру здания... Конец.")
if d == "2":
    print("Выподнимаетись с пола, мигом досаёте свою пушку и опустошаете целый магазин из 17 конфет в сторону Деда и ельфов, ваш град сладостей задел ельфа и оглушил Мороза, вы делаете ноги к кухонному столу, под которым у вас Карабин M4подарка калибра .223снежинки, вы вырываете его из под скотча, отдергиваетезатвор и переключаете режим стрельбы на автоматический. Похоже, ваша обоймой сахара не на долго их остановила, так как грохот шагов разъярённого Деда быстро приближается. Вы становитесь с лева от входа в кухню за каменной стеной, оставляя только правое плечо, голову и руки неприкрытыми. Вы перемещаете указательный палец  на курок и задерживаете дыхание, цевьё праздничной винтовки выглядывает из-за пририкрытия, ожидая бойя. Вы чувствуете себя неловко...")

if c == "2":
    print("Вы находите позицию с хорошим укрытием и хорошим углом, А это всё оказывается неважно, так как вы видите как созванном отскакивает от стены граната, украшенная как ёлочная игрушка, котороя приземляется прямо у ваших ног…. Вас превратили в рождественская привидение, и теперь вы обязаны терроризировать каждое Рождество и новый год плохих детей. Конец.")
if c != "1" and c != "2":
    print("Такой опции нет")
if b != "1" and b != "2":
    print("Такой опции нет")
if e != "1" and e != "2":
    print("Такой опции нет")

if b == "2":
    print("Действие 1 Попробовать забайтить деда и просто прыгнуть из окна в гигансткий сугроб")
    print("Действие 2 Закончить это раз и на всегда")
d = input()
if c != "1" and c != "2":
    print("Такой опции нет")

if d == "1":
    print("Вы мигом поворачивайтесь, открываете окно и прыгайте в сугроб, как только вы встаёте вы окружены отрядом эльфов, которые похожи стояли по всему периметру здания... Конец.")
if d == "2":
    print("Выподнимаетись с пола, мигом досаёте свою пушку и опустошаете целый магазин из 17 конфет в сторону Деда и ельфов, ваш град сладостей задел ельфа и оглушил Мороза, вы делаете ноги к кухонному столу, под которым у вас Карабин M4подарка калибра .223снежинки, вы вырываете его из под скотча, отдергиваетезатвор и переключаете режим стрельбы на автоматический. Похоже, ваша обоймой сахара не на долго их остановила, так как грохот шагов разъярённого Деда быстро приближается. Вы становитесь с лева от входа в кухню за каменной стеной, оставляя только правое плечо, голову и руки неприкрытыми. Вы перемещаете указательный палец  на курок и задерживаете дыхание, цевьё праздничной винтовки выглядывает из-за пририкрытия, ожидая бойя. Вы чувствуете себя неловко...")

if d != "1" and d != "2":
    print("Такой опции нет")