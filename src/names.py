import random
men_names = ["Алексей", "Александр", "Анатолий", "Андрей", "Антон", "Арсений", "Артем", "Борис", "Вадим", "Валентин",
             "Василий", "Виктор", "Владимир", "Владислав", "Вячеслав", "Геннадий", "Георгий", "Глеб", "Григорий", "Даниил", "Денис", "Дмитрий", "Евгений", "Егор", "Иван", "Игорь", "Илья", "Кирилл", "Константин", "Лев", "Максим", "Марк", "Матвей", "Михаил", "Никита", "Николай", "Олег", "Павел", "Петр", "Роман", "Руслан", "Сергей", "Станислав", "Степан", "Тимофей", "Федор", "Юрий", "Ярослав", "Адам", "Айдар", "Айрат", "Алекс", "Александр", "Алексей", "Али", "Амир", "Анатолий", "Андрей", "Антон", "Аркадий", "Арсен", "Арсений", "Артем", "Аскар", "Богдан", "Борис", "Вадим", "Валентин", "Валерий", "Василий", "Виктор", "Виталий", "Владимир", "Владислав", "Вячеслав", "Геннадий", "Георгий", "Глеб", "Григорий", "Давид", "Дамир", "Даниил", "Денис", "Дмитрий", "Евгений", "Егор", "Иван", "Игнат", "Игорь", "Илья", "Камиль", "Кирилл", "Константин", "Лев", "Леонид", "Магомед", "Максим", "Марат", "Марк", "Матвей", "Михаил", "Никита", "Николай", "Олег", "Павел", "Петр", "Рамиль", "Рашид", "Ринат", "Роберт", "Роман", "Руслан", "Рустам", "Сергей", "Станислав", "Степан", "Тимур", "Тимофей", "Федор", "Юрий", "Ярослав"]
men_surnames = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков",
                "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров", "Павлов", "Козлов", "Степанов", "Николаев", "Орлов", "Андреев", "Макаров", "Никитин", "Захаров", "Зайцев", "Соловьев", "Борисов", "Яковлев", "Григорьев", "Романов", "Воробьев", "Сергеев", "Кузьмин", "Фролов", "Александров", "Дмитриев", "Королев", "Гусев", "Киселев", "Ильин", "Максимов", "Поляков", "Сорокин", "Виноградов", "Ковалев", "Белов", "Медведев", "Антонов", "Тарасов", "Жуков", "Баранов", "Филиппов", "Комаров", "Давыдов", "Беляев", "Герасимов", "Богданов", "Осипов", "Сидоров", "Матвеев", "Титов", "Марков", "Миронов", "Крылов", "Куликов", "Карпов", "Власов", "Мельников", "Денисов", "Гаврилов", "Тихонов", "Казаков", "Афанасьев", "Данилов", "Савельев", "Тимофеев", "Фомин", "Чернов", "Абрамов", "Мартынов", "Ефимов", "Федотов", "Щербаков", "Назаров", "Калинин", "Исаев", "Чернышев", "Князев", "Головин", "Маслов", "Родионов", "Коновалов", "Лазарев", "Воронин", "Климов", "Филатов", "Пономарев", "Голубев", "Кудрявцев", "Прохоров", "Наумов", "Потапов", "Журавлев", "Овчинников", "Трофимов", "Леонтьев", "Соболев", "Ермаков", "Колесников", "Гончаров", "Емельянов", "Никифоров", "Грачев", "Котов", "Гришин", "Ефремов", "Архипов", "Громов", "Кириллов", "Маринин", "Алексеев"]
men_third = [
"Александрович", "Алексеевич", "Анатольевич", "Андреевич", "Антонович", "Аркадьевич", "Арсеньевич", "Артемович",
    "Борисович", "Вадимович", "Валентинович", "Валерьевич", "Васильевич", "Викторович", "Владимирович", "Владиславович", "Вячеславович", "Геннадьевич", "Георгиевич", "Глебович", "Григорьевич", "Данилович", "Денисович", "Дмитриевич", "Евгеньевич", "Егорович", "Иванович", "Игоревич", "Ильич", "Кириллович", "Константинович", "Львович", "Максимович", "Маркович", "Матвеевич", "Михайлович", "Никитич", "Николаевич", "Олегович", "Павлович", "Петрович", "Романович", "Русланович", "Сергеевич", "Станиславович", "Степанович", "Тимофеевич", "Федорович", "Юрьевич", "Ярославович", "Адамович", "Айдарович", "Айратович", "Алексеевич", "Александрович", "Александрович", "Алексеевич", "Алиевич", "Амирович", "Анатольевич", "Андреевич", "Антонович", "Аркадьевич", "Арсенович", "Арсеньевич", "Артемович", "Аскарович", "Богданович", "Борисович", "Вадимович", "Валентинович", "Валерьевич", "Васильевич", "Викторович", "Витальевич", "Владимирович", "Владиславович", "Вячеславович", "Геннадьевич", "Георгиевич", "Глебович", "Григорьевич", "Давидович", "Дамирович", "Даниилович", "Денисович", "Дмитриевич", "Евгеньевич", "Егорович", "Иванович", "Игнатьевич", "Игоревич", "Ильич", "Камильевич", "Кириллович", "Константинович", "Львович", "Леонидович", "Магомедович", "Максимович", "Маратович", "Маркович", "Матвеевич", "Михайлович", "Мухаметович", "Никитич", "Николаевич", "Олегович", "Олегович", "Олегович", "Олегович", "Павлович", "Петрович", "Равилевич", "Рашидович", "Ринатович", "Робертович", "Романович", "Русланович", "Сергеевич", "Станиславович", "Степанович", "Тагирович", "Тимофеевич", "Тимурович", "Федорович", "Хабибович", "Юрьевич", "Ярославович"]
women_names = [
"Августа",
"Авдотья",
"Аврора",
"Агата",
"Агапия",
"Агафья",
"Аглая",
"Агнесса",
"Агния",
"Агриппина",
"Агунда",
"Ада",
"Аделина",
"Аделаида",
"Адель",
"Адиля",
"Адриана",
"Аза",
"Азалия",
"Азиза",
"Айгуль",
"Айлин",
"Айнагуль",
"Аида",
"Айжан",
"Аксинья",
"Акулина",
"Алана",
"Алевтина",
"Александра",
"Алена",
"Алико",
"Алина",
"Алиса",
"Алия",
"Алла",
"Алсу",
"Альба",
"Альберта",
"Альбина",
"Альвина",
"Альфия",
"Альфреда",
"Аля",
"Амаль",
"Амелия",
"Амина",
"Амира",
"Анаит",
"Анастасия",
"Ангелина",
"Анеля",
"Анжела",
"Анжелика",
"Анисья",
"Анита",
"Анна",
"Антонина",
"Анфиса",
"Аполлинария",
"Арабелла",
"Ариадна",
"Ариана",
"Арина",
"Архелия",
"Асель",
"Асия",
"Ассоль",
"Астра",
"Астрид",
"Ася",
"Аурелия",
"Афанасия",
"Аэлита",
"Беатриса",
"Белинда",
"Белла",
"Берта",
"Бирута",
"Богдана",
"Божена",
"Борислава",
"Бронислава",
"Валентина",
"Валерия",
"Ванда",
"Ванесса",
"Варвара",
"Василина",
"Василиса",
"Венера",
"Вера",
"Вероника",
"Веселина",
"Весна",
"Веста",
"Вета",
"Вида",
"Викторина",
"Виктория",
"Вилена",
"Вилора",
"Виолетта",
"Виргиния",
"Виринея",
"Вита",
"Виталина",
"Влада",
"Владислава",
"Владлена",
"Габриэлла",
"Галина",
"Галия",
"Гаянэ",
"Гелена",
"Гаянэ",
"Гелена",
"Гелла",
"Генриетта",
"Георгина",
"Гера",
"Гертруда",
"Глафира",
"Глаша",
"Глория",
"Гражина",
"Грета",
"Гузель",
"Гулия",
"Гульмира",
"Гульназ",
"Гульнара",
"Гульшат",
"Дайна",
"Далия",
"Дамира",
"Дана",
"Даниэла",
"Данута",
"Дара",
"Дарина",
"Дарья",
"Даяна",
"Дебора",
"Джамиля",
"Джемма",
"Дженнифер",
"Джессика",
"Джулия",
"Джульетта",
"Диана",
"Дилара",
"Дильназ",
"Дильнара",
"Диля",
"Дина",
"Динара",
"Диодора",
"Дионисия",
"Долорес",
"Доля",
"Доминика",
"Дора",
"Ева",
"Евангелина",
"Евгения",
"Евдокия",
"Екатерина",
"Елена",
"Елизавета",
"Есения",
"Ефимия",
"Жанна",
"Жасмин",
"Жозефина",
"Забава",
"Заира",
"Замира",
"Зара",
"Зарема",
"Зарина",
"Захария",
"Земфира",
"Зинаида",
"Зита",
"Злата",
"Зоряна",
"Зоя",
"Зульфия",
"Зухра",
"Иванна",
"Иветта",
"Ивона",
"Ида",
"Изабелла",
"Изольда",
"Илария",
"Илиана",
"Илона",
"Инара",
"Инга",
"Ингеборга",
"Индира",
"Инесса",
"Инна",
"Иоанна",
"Иоланта",
"Ираида",
"Ирина",
"Ирма",
"Искра",
"Ия",
"Калерия",
"Камилла",
"Капитолина",
"Карима",
"Карина",
"Каролина",
"Катарина",
"Кира",
"Клавдия",
"Клара",
"Кларисса",
"Климентина",
"Констанция",
"Кора",
"Корнелия",
"Кристина",
"Ксения",
"Лада",
"Лайма",
"Лана",
"Лара",
"Лариса",
"Лаура",
"Лейла",
"Лейсан",
"Леокадия",
"Леонида",
"Лера",
"Леся",
"Лиана",
"Лидия",
"Лиза",
"Лика",
"Лилиана",
"Лилия",
"Лина",
"Линда",
"Лиора",
"Лира",
"Лия",
"Лола",
"Лолита",
"Лора",
"Луиза",
"Лукерья",
"Любовь",
"Людмила",
"Ляля",
"Люция",
"Магда",
"Магдалина",
"Мадина",
"Майя",
"Малика",
"Мальвина",
"Мара",
"Маргарита",
"Марианна",
"Марика",
"Марина",
"Мария",
"Марселина",
"Марта",
"Маруся",
"Марфа",
"Марьям",
"Матильда",
"Мелания",
"Мелисса",
"Мика",
"Мила",
"Милада",
"Милана",
"Милена",
"Милица",
"Милолика",
"Милослава",
"Мира",
"Мирослава",
"Мирра",
"Моника",
"Муза",
"Мэри",
"Надежда",
"Назира",
"Наиля",
"Наима",
"Нана",
"Наоми",
"Наталья",
"Нателла",
"Нелли",
"Неонила",
"Ника",
"Николь",
"Нина",
"Нинель",
"Нонна",
"Нора",
"Нурия",
"Одетта",
"Оксана",
"Октябрина",
"Олеся",
"Оливия",
"Ольга",
"Офелия",
"Павла",
"Павлина",
"Памела",
"Патриция",
"Пелагея",
"Перизат",
"Полина",
"Прасковья",
"Рада",
"Радмила",
"Раиса",
"Ревекка",
"Регина",
"Рема",
"Рената",
"Римма",
"Рина",
"Рита",
"Рогнеда",
"Роберта",
"Роза",
"Роксана",
"Ростислава",
"Рузалия",
"Рузанна",
"Рузиля",
"Румия",
"Русалина",
"Руслана",
"Руфина",
"Сабина",
"Сабрина",
"Сажида",
"Саида",
"Саломея",
"Самира",
"Сандра",
"Сания",
"Санта",
"Сара",
"Сати",
"Светлана",
"Святослава",
"Севара",
"Северина",
"Селена",
"Серафима",
"Сильва",
"Сима",
"Симона",
"Слава",
"Снежана",
"Соня",
"София",
"Станислава",
"Стелла",
"Стефания",
"Сусанна",
"Таира",
"Таисия",
"Тала",
"Тамара",
"Тамила",
"Тара",
"Татьяна",
"Тереза",
"Тина",
"Тора",
"Ульяна",
"Урсула",
"Устина",
"Устинья",
"Фаиза",
"Фаина",
"Фания",
"Фаня",
"Фарида",
"Фатима",
"Фая",
"Фекла",
"Фелиция",
"Феруза",
"Физура",
"Флора",
"Франсуаза",
"Фрида",
"Харита",
"Хилари",
"Хильда",
"Хлоя",
"Христина",
"Цветана",
"Челси",
"Чеслава",
"Чулпан",
"Шакира",
"Шарлотта",
"Шейла",
"Шелли",
"Шерил",
"Эвелина",
"Эвита",
"Эдда",
"Эдита",
"Элеонора",
"Элиана",
"Элиза",
"Элина",
"Элла",
"Эллада",
"Элоиза",
"Эльвина",
"Эльвира",
"Эльга",
"Эльза",
"Эльмира",
"Эльнара",
"Эля",
"Эмилия",
"Эмма",
"Эмили",
"Эрика",
"Эрнестина",
"Эсмеральда",
"Этель",
"Этери",
"Юзефа",
"Юлия",
"Юна",
"Юния",
"Юнона",
"Ядвига",
"Яна",
"Янина",
"Ярина",
"Ярослава",
"Ясмина",
]
women_surnames = ["Иванова", "Смирнова", "Кузнецова", "Попова", "Васильева", "Петрова", "Соколова", "Михайлова",
                  "Новикова", "Федорова", "Морозова", "Волкова", "Алексеева", "Лебедева", "Семенова", "Егорова", "Павлова", "Козлова", "Степанова", "Николаева", "Орлова", "Андреева", "Макарова", "Никитина", "Захарова", "Зайцева", "Соловьева", "Борисова", "Яковлева", "Григорьева", "Романова", "Воробьева", "Сергеева", "Кузьмина", "Фролова", "Александрова", "Дмитриева", "Королева", "Гусева", "Киселева", "Ильина", "Максимова", "Полякова", "Сорокина", "Виноградова", "Ковалева", "Белова", "Медведева", "Антонова", "Тарасова", "Жукова", "Баранова", "Филиппова", "Комарова", "Давыдова", "Беляева", "Герасимова", "Богданова", "Осипова", "Сидорова", "Матвеева", "Титова", "Маркова", "Миронова", "Крылова", "Куликова", "Карпова", "Власова", "Мельникова", "Денисова", "Гаврилова", "Тихонова", "Казакова", "Афанасьева", "Данилова", "Савельева", "Тимофеева", "Фомина", "Чернова", "Абрамова", "Мартынова", "Ефимова", "Федотова", "Щербакова", "Назарова", "Калинина", "Исаева", "Чернышева", "Князева", "Головина", "Маслова", "Родионова", "Коновалова", "Лазарева", "Воронина", "Климова", "Филатова", "Пономарева", "Голубева", "Кудрявцева", "Прохорова", "Наумова", "Потапова", "Журавлева", "Овчинникова", "Трофимова", "Леонтьева", "Соболева", "Ермакова", "Колесникова", "Гончарова", "Емельянова", "Никифорова", "Грачева", "Котова", "Гришина", "Ефремова", "Архипова", "Громова", "Кириллова", "Маринина", "Алексеева"]
women_third = ["Александровна", "Алексеевна", "Анатольевна", "Андреевна", "Антоновна", "Аркадьевна", "Арсеньевна",
                "Артемовна", "Борисовна", "Вадимовна", "Валентиновна", "Валерьевна", "Васильевна", "Викторовна", "Владимировна", "Владиславовна", "Вячеславовна", "Геннадьевна", "Георгиевна", "Глебовна", "Григорьевна", "Даниловна", "Денисовна", "Дмитриевна", "Евгеньевна", "Егоровна", "Ивановна", "Игоревна", "Ильинична", "Кирилловна", "Константиновна", "Львовна", "Максимовна", "Марковна", "Матвеевна", "Михайловна", "Никитична", "Николаевна", "Олеговна", "Павловна", "Петровна", "Романовна", "Руслановна", "Сергеевна", "Станиславовна", "Степановна", "Тимофеевна", "Федоровна", "Юрьевна", "Ярославовна", "Адамовна", "Айдаровна", "Айратовна", "Алексеевна", "Александровна", "Александровна", "Алексеевна", "Алиевна", "Амировна", "Анатольевна", "Андреевна", "Антоновна", "Аркадьевна", "Арсеновна", "Арсеньевна", "Артемовна", "Аскаровна", "Богдановна", "Борисовна", "Вадимовна", "Валентиновна", "Валерьевна", "Васильевна", "Викторовна", "Витальевна", "Владимировна", "Владиславовна", "Вячеславовна", "Геннадьевна", "Георгиевна", "Глебовна", "Григорьевна", "Давидовна", "Дамировна", "Данииловна", "Денисовна", "Дмитриевна", "Евгеньевна", "Егоровна", "Ивановна", "Игнатьевна", "Игоревна", "Ильинична", "Камильевна", "Кирилловна", "Константиновна", "Львовна", "Леонидовна", "Магомедовна", "Максимовна", "Маратовна"]
def random_phone():
    return "+7"+ str(random.randrange(1000000000, 9999999999))
organizations = ["ООО «Созвездие»",
"ИП «ГрандСтрой»",
"ЗАО «Прогресс»",
"ОАО «Энергия»",
"НКО «Союз добровольцев»",
"ГКУ «Центр социальной помощи»",
"Фонд «Развитие образования»",
"ПАО «Инновационные технологии»",
"ООО «Авангард»",
"ИП «МастерСервис»",
"ЗАО «Престиж-строй»",
"ОАО «Прогресс-Медиа»",
"НКО «Защита прав потребителей»",
"ГКУ «Медицинский центр»",
"Фонд «Поддержка талантов»",
"ПАО «Инвестиционный банк»",
"ООО «Вектор-Транс»",
"ИП «МегаПродукт»",
"ЗАО «СтройИнвест»",
"ОАО «Агрохолдинг»",
"НКО «Зеленый мир»",
"ГКУ «Центр занятости»",
"Фонд «Благотворительная помощь»",
"ПАО «Финансовая группа»",
"ООО «Эксперт-Консалт»",
"ИП «ТехноСервис»",
"ЗАО «Успех-Групп»",
"ОАО «СтройПром»",
"НКО «Общество экологов»",
"ГКУ «Центр культуры»",
"Фонд «Развитие спорта»",
"ПАО «Страховая компания»",
"ООО «ТехноПродукт»",
"ИП «Авто-Мастер»",
"ЗАО «Энергохим»",
"ОАО «Торговый дом»",
"НКО «Защита прав детей»",
"ГКУ «Музей истории»",
"Фонд «Социальное партнерство»",
"ПАО «Транспортная компания»",
"ООО «СтройГарант»",
"ИП «МедиаСервис»",
"ЗАО «Инновационные решения»",
"ОАО «ПромТорг»",
"НКО «Женский союз»",
"ГКУ «Центр здоровья»",
"Фонд «Поддержка молодежи»",
"ПАО «Индустриальная группа»",
"ООО «МегаТранс»",
"ИП «СтройПроект»",
"ЗАО «Эксперт-Строй»",
"ОАО «Финансовая компания»",
"НКО «Фонд здоровья»",
"ГКУ «Центр образования»",
"Фонд «Развитие культуры»",
"ПАО «Инжиниринговая компания»",
"ООО «ЭнергоСистемы»",
"ИП «ТехноСтрой»",
"ЗАО «СтройИнвест»",
"ОАО «АгроКомплекс»",
"НКО «Центр прав потребителей»",
"ГКУ «Центр социальной поддержки»",
"Фонд «Поддержка талантов и креативности»",
"ПАО «Инновационный банк развития»",
"ООО «Авангард-Транс»",
"ИП «СтройПромСервис»",
"ЗАО «ПрестижСтройИнвест»",
"ОАО «ЭнергоМедиа»",
"НКО «Общество защиты прав потребителей»",
"ГКУ «Медицинский центр здоровья»",
"Фонд «Поддержка образования и науки»",
"ПАО «Инвестиционный банк финансовых решений»",
"ООО «Вектор-Транспортные системы»",
"ИП «МегаПродуктСервис»",
"ЗАО «ПрестижСтройИнвестМонтаж»",
"ОАО «Агрохолдинг-Строй»",
"НКО «Зеленый мир экологов»",
"ГКУ «Центр занятости и трудоустройства»",
"Фонд «Благотворительная помощь в развитии»",
"ПАО «Финансовая группа инвестиций»",
"ООО «Эксперт-КонсалтИнвест»",
"ИП «ТехноСервисРемонт»",
"ЗАО «Успех-ГруппСтрой»",
"ОАО «СтройПромМонтаж»",
"НКО «Общество экологов и защиты природы»",
"ГКУ «Центр культуры и искусства»",
"Фонд «Развитие спорта и физической культуры»",
"ПАО «Страховая компания защиты имущества»",
"ООО «ТехноПродуктИнжиниринг»",
"ИП «Авто-МастерСервис»",
"ЗАО «ЭнергохимСтрой»",
"ОАО «Торговый домПродукты»",
"НКО «Защита прав детей и молодежи»",
"ГКУ «Музей истории и культуры»",
"Фонд «Социальное партнерство и поддержка»",
"ПАО «Транспортная компания логистики»",
"ООО «СтройГарантИнжиниринг»",
"ИП «МедиаСервисПроект»",
"ЗАО «Инновационные решенияТехнологии»",
"ОАО «ПромТоргКомплекс»",
"НКО «Женский союзРазвитие»",
"ГКУ «Центр здоровья и благополучия»",
"Фонд «Поддержка молодежи и талантов»",
"ПАО «Индустриальная группаРазвитие»",
"ООО «МегаТрансСервис»",
"ИП «СтройПроектИнжиниринг»",
"ЗАО «Эксперт-СтройИнвест»",
"ОАО «Финансовая компанияБанк»",
"НКО «Фонд здоровья и социальной поддержки»",
"ГКУ «Центр образования и науки»",
"Фонд «Развитие культуры и искусства»",
"ПАО «Инжиниринговая компанияСтроительство»",
"ООО «ЭнергоСистемыПром»",
"ИП «ТехноСтройРемонт»",
"ЗАО «СтройИнвестМонтаж»",
"ОАО «АгроКомплексСтрой»",
"НКО «Центр прав потребителейЗащита»",
"ГКУ «Центр социальной поддержкиМедицина»",
"Фонд «Поддержка талантов и креативностиОбразование»",
"ПАО «Инновационный банк развитияФинансы»",
"ООО «Авангард-ТрансСервис»",
"ИП «СтройПромСервисРемонт»",
"ЗАО «ПрестижСтройИнвестМонтажБизнес»",
"ОАО «ЭнергоМедиаТехнологии»",
"НКО «Общество защиты прав потребителейСоюз»",
"ГКУ «Медицинский центр здоровьяПомощь»",
"Фонд «Поддержка образования и наукиРазвитие»",
"ПАО «Инвестиционный банк финансовых решенийИнновации»",
"ООО «Вектор-Транспортные системыТранспорт»",
"ИП «МегаПродуктСервисПроизводство»",
"ЗАО «ПрестижСтройИнвестМонтажСтроительство»",
"ОАО «Агрохолдинг-СтройПродовольствие»",
"НКО «Зеленый мир экологовПрирода»",
"ГКУ «Центр занятости и трудоустройствоРазвитие»",
"Фонд «Благотворительная помощь в развитииСоциальная»",
"ПАО «Финансовая группа инвестицийФинансы»",
"ООО «Эксперт-КонсалтИнвестБизнес»",
"ИП «ТехноСервисРемонтСтроительство»",
"ЗАО «Успех-ГруппСтройИнвестРазвитие»",
"ОАО «СтройПромМонтажСтроительство»",
"НКО «Общество экологов и защиты природыЭкология»",
"ГКУ «Центр культуры и искусствоКультура»",
"Фонд «Развитие спорта и физической культурыСпорт»",
"ПАО «Страховая компания защиты имуществаСтрахование»",
"ООО «ТехноПродуктИнжинирингТехнологии»",
"ИП «Авто-МастерСервисАвтосервис»",
"ЗАО «ЭнергохимСтройПромПроизводство»",
"ОАО «Торговый домПродуктыБизнес»",
"НКО «Защита прав детей и молодежиЗащита»",
"ГКУ «Музей истории и культурыИстория»",
"Фонд «Социальное партнерство и поддержкаСоциальная»",
"ПАО «Транспортная компания логистикиТранспорт»",
"ООО «СтройГарантИнжинирингСтроительство»",
"ИП «МедиаСервисПроектМедиа»",
"ЗАО «Инновационные решенияТехнологииИнновации»",
"ОАО «ПромТоргКомплексПродажа»",
"НКО «Женский союзРазвитиеПоддержка»",
"ГКУ «Центр здоровья и благополучияЗдоровье»",
"Фонд «Поддержка молодежи и талантовРазвитие»",]
INN = [5340249607, 2743980554, 5627377681, 9759837716, 4230184469, 6047435799, 6656939031, 2364267032, 8731527160,
       7756596765, 5906859552, 9023903777, 8290156069, 8378401323, 3900278830, 8130206767, 3539256879, 7965675568, 2244136501, 8877906997, 7506299965, 9369383486, 1067670594, 7170737737, 5080479313, 1149172818, 5876469330, 6967203412, 2804226647, 8171863639, 7791968857, 4328504410, 4117502042, 3005256292, 6506659941, 5036412006, 4969167980, 8583309425, 7503323763, 6741554300, 8144354947, 3236219019, 7951304332, 9084143245, 6577783444, 7196595348, 3830151832, 9534753946, 4858094236, 9263369375, 4390526623, 8129152674, 6231800483, 6749268134, 2169217706, 2718762666, 2100811948, 4676107441, 6789138613, 1931944632, 8525343417, 5370058426, 1771937468, 4219164865, 9113513155, 9237329604, 2534953669, 1564853966, 2942300880, 2208725203, 8928495315, 4298810581, 2465464019, 7103656666, 7397520090, 4969435354, 9993765085, 9319953122, 3301971171, 2627937510, 6266948329, 2459442409, 9833453806, 8341516015, 8257464048, 8653657329, 2298685687, 2603528951, 4001972474, 4671033597, 7557880574, 7265213192, 1860529422, 5278866192, 8439249172, 9122249510, 4886613286, 8087611690, 5880533291, 4958861610, 5776012586, 4597603121, 2998239026, 7715595577, 5996212025, 4044512572, 2128918333, 8010777410, 1057332547, 3930472771, 8319895874, 1016743749, 5939629385, 5398025034, 4606482250, 2689386318, 4991150926, 3520745297, 8934154578, 5992712530, 2703161176, 2321182553, 8376262490, 5644770648, 6902938457, 6495580509, 4124345701, 2782269288, 2289458026, 4374871403, 1627852652, 9870812018, 1975347059, 7480264052, 2831387508, 3347181942, 9630391156, 4298838903, 9569678714, 6491288443, 2583946107, 5997030274, 8953463685, 7597307270, 3710733702, 6535080330, 9019616652, 2098093453, 5274634637, 8693747597, 5000989584, 8008891280, 1370541970, 1561810325, 1712865174, 1505130389, 9612975510, 4437564322, 5472903076, 1779864998, 9168172455, 1336370602, 8621793710, 8826809776, 6912843699, 8578253236, 5106056119, 9032711608, 9344362425, 9877291450, 2304107963, 9797461433, 1021176765, 2280886208, 4641875395, 7239312325, 2453038023, 5005588936, 2027601354, 9382625226, 2261563341, 9645152719, 5738962386, 1370983897, 6714199515, 7813072350, 1195638753, 8500695522, 6324906978, 4803172324, 3054282722, 1255079405, 8530619889, 3873567732, 1413382134, 2134222327, 9471364600, 8837240825, 8662429690, 5772975611]


