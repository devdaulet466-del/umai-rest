# mock_data for the UMAI restaurant

special_menu = {
    "name": {
        "en": "Special Menu",
        "ru": "Специальное меню",
        "kk": "Арнайы мәзір"
    },
    "items": [
        {
            "id": 1,
            "name": {
                "en": "Iftar set №1",
                "ru": "Ифтар сет №1",
                "kk": "Ауызашар сет №1"
            },
            "price": 8500,
            "description": {
                "en": "Warm salad, lentil soup, drink",
                "ru": "Теплый салат, чечевичный суп, напиток",
                "kk": "Жылы салат, жасымық сорпасы, сусын"
            },
            "image": "images/foodImages/IMG_1025.JPG",
            "weight": "500g"
        },
        {
            "id": 101,
            "name": {
                "en": "Chef's Special Beef",
                "ru": "Фирменная говядина от шефа",
                "kk": "Аспаздың фирмалық сиыр еті"
            },
            "price": 12500,
            "description": {
                "en": "Slow-cooked beef with signature sauce",
                "ru": "Томленая говядина с фирменным соусом",
                "kk": "Фирмалық тұздықпен бұқтырылған сиыр еті"
            },
            "image": "images/foodImages/IMG_1440.JPG",
            "weight": "400g"
        },
        {
            "id": 102,
            "name": {
                "en": "Seasonal Fruit Platter",
                "ru": "Сезонная фруктовая тарелка",
                "kk": "Маусымдық жеміс тарелкасы"
            },
            "price": 6000,
            "description": {
                "en": "Fresh seasonal exotic fruits",
                "ru": "Свежие сезонные экзотические фрукты",
                "kk": "Жаңа піскен маусымдық экзотикалық жемістер"
            },
            "image": "images/foodImages/IMG_1443.JPG",
            "weight": "800g"
        }
    ]
}

menu_categories = [
    {
        "id": "breakfasts",
        "name": {
            "en": "Breakfasts",
            "ru": "Завтраки",
            "kk": "Таңғы ас"
        },
        "subcategories": [
            {
                "id": "eggs",
                "name": {
                    "en": "Eggs",
                    "ru": "Яйца",
                    "kk": "Жұмыртқа"
                },
                "items": [
                    {
                        "id": 2,
                        "name": {
                            "en": "Dranik with salmon, fresh vegetables and poached egg",
                            "ru": "Драник с лососем, свежими овощами и яйцом пашот",
                            "kk": "Лосось, жаңа піскен көкөністер және пашот жұмыртқасы бар драник"
                        },
                        "price": 5900,
                        "description": {
                            "en": "Crispy potato pancake served with salted salmon and a soft poached egg",
                            "ru": "Хрустящий картофельный драник со слабосоленой семгой и нежным яйцом пашот",
                            "kk": "Тұздалған лосось және пашот жұмыртқасы берілетін қытырлақ картоп құймағы"
                        },
                        "image": "images/foodImages/IMG_1440.JPG"
                    },
                    {
                        "id": 3,
                        "name": {
                            "en": "Benedict with salmon on brioche",
                            "ru": "Бенедикт с лососем на бриоши",
                            "kk": "Бриошь нанындағы лосось қосылжен бенедикт"
                        },
                        "price": 6400,
                        "description": {
                            "en": "Classic Eggs Benedict with smoked salmon and hollandaise sauce on a buttery brioche bun",
                            "ru": "Классические яйца Бенедикт с копченым лососем и голландским соусом на сливочной бриоши",
                            "kk": "Сарымайға пісірілген бриошь нанындағы голланд тұздығы және ысталған лосось қосылған классикалық Бенедикт жұмыртқасы"
                        },
                        "image": "images/foodImages/IMG_1443.JPG"
                    },
                    {
                        "id": 301,
                        "name": {
                            "en": "Omelette with mushrooms",
                            "ru": "Омлет с лесными грибами",
                            "kk": "Саңырауқұлақ қосылған омлет"
                        },
                        "price": 4500,
                        "description": {
                            "en": "Fluffy three-egg omelette filled with sautéed wild mushrooms and cheese",
                            "ru": "Пышный омлет из трех яиц с обжаренными лесными грибами и сыром",
                            "kk": "Қуырылған орман саңырауқұлақтары мен ірімшік қосылған үш жұмыртқадан жасалған үлпілдек омлет"
                        },
                        "image": "images/foodImages/IMG_1440.JPG"
                    }
                ]
            },
            {
                "id": "house_bread_specials",
                "name": {
                    "en": "House Bread Specials",
                    "ru": "Фирменный хлеб",
                    "kk": "Фирмалық нан"
                },
                "items": [
                    {
                        "id": 4,
                        "name": {
                            "en": "Classic shakshuka with yoghurt and grain bread",
                            "ru": "Классическая шакшука с йогуртом и зерновым хлебом",
                            "kk": "Йогурт және астық нанымен классикалық шакшука"
                        },
                        "price": 4100,
                        "description": {
                            "en": "Eggs cooked in a rich tomato and pepper sauce, served with greek yoghurt and house grain bread",
                            "ru": "Яйца, запеченные в насыщенном соусе из томатов и болгарского перца, с греческим йогуртом",
                            "kk": "Қызанақ пен болгар бұрышынан жасалған қанық тұздықта пісірілген жұмыртқа, йогуртпен беріледі"
                        },
                        "image": "images/foodImages/IMG_1456.JPG"
                    },
                    {
                        "id": 401,
                        "name": {
                            "en": "Avocado toast on rye toast",
                            "ru": "Авокадо тост на ржаном хлебе",
                            "kk": "Қара бидай нанындағы авокадо тосты"
                        },
                        "price": 3800,
                        "description": {
                            "en": "Smashed avocado with cherry tomatoes and microgreens on toasted rye bread",
                            "ru": "Размятое авокадо с помидорами черри и микрозеленью на поджаренном ржаном хлебе",
                            "kk": "Қуырылған қара бидай нанындағы шие қызанақтары мен микрокөкөніс қосылған езілген авокадо"
                        },
                        "image": "images/foodImages/IMG_1456.JPG"
                    }
                ]
            },
            {
                "id": "sweet_breakfasts",
                "name": {
                    "en": "Sweet Breakfasts",
                    "ru": "Сладкие завтраки",
                    "kk": "Тәтті таңғы ас"
                },
                "items": [
                    {
                        "id": 402,
                        "name": {
                            "en": "Syrniki with berry jam",
                            "ru": "Сырники с ягодным джемом",
                            "kk": "Жидек тосабы қосылған сырниктер"
                        },
                        "price": 3500,
                        "description": {
                            "en": "Soft cottage cheese pancakes served with homemade berry jam and sour cream",
                            "ru": "Нежные творожные сырники, подаются с домашним ягодным вареньем и сметаной",
                            "kk": "Үйдің жидек тосабы және қаймақпен берілетін жұмсақ сүзбе сырниктері"
                        },
                        "image": "images/foodImages/IMG_1443.JPG"
                    },
                    {
                        "id": 403,
                        "name": {
                            "en": "Oatmeal with fresh fruits",
                            "ru": "Овсяная каша со свежими фруктами",
                            "kk": "Жаңа піскен жемістер қосылған сұлы ботқасы"
                        },
                        "price": 2800,
                        "description": {
                            "en": "Creamy oatmeal topped with seasonal berries, bananas, and a drizzle of honey",
                            "ru": "Тающая во рту овсяная каша с сезонными ягодами, бананами и каплей меда",
                            "kk": "Маусымдық жидектер, банан және бал тамызылған ауызда еритін сұлы ботқасы"
                        },
                        "image": "images/foodImages/IMG_1456.JPG"
                    }
                ]
            }
        ]
    },
    {
        "id": "salads",
        "name": {
            "en": "Salads",
            "ru": "Салаты",
            "kk": "Салаттар"
        },
        "subcategories": [
             {
                "id": "fresh_salads",
                "name": {
                    "en": "Fresh Salads",
                    "ru": "Свежие салаты",
                    "kk": "Жаңа піскен салаттар"
                },
                "items": [
                     {
                        "id": 5,
                        "name": {
                            "en": "Summer Salad",
                            "ru": "Летний салат",
                            "kk": "Жазғы салат"
                        },
                        "price": 3200,
                        "description": {
                            "en": "A refreshing mix of seasonal greens, cucumbers, tomatoes, and a light vinaigrette",
                            "ru": "Освежающий микс сезонной зелени, огурцов, помидоров с легкой заправкой",
                            "kk": "Жаңа піскен шөптер, қияр, қызанақ және жеңіл тұздық қосылған сергітетін салат"
                        },
                        "image": "images/foodImages/IMG_1469.JPG"
                    },
                    {
                        "id": 501,
                        "name": {
                            "en": "Greek Salad with Feta",
                            "ru": "Греческий салат с фетой",
                            "kk": "Фета ірімшігі қосылған грек салаты"
                        },
                        "price": 3900,
                        "description": {
                            "en": "Classic Mediterranean salad with feta cheese, calamata olives, and olive oil",
                            "ru": "Классический средиземноморский салат с сыром фета, оливками каламата и оливковым маслом",
                            "kk": "Фета сыры, каламата зәйтүндері және зәйтүн майы қосылған классикалық жерорта теңізі салаты"
                        },
                        "image": "images/foodImages/IMG_1469.JPG"
                    }
                ]
            },
            {
                "id": "warm_salads",
                "name": {
                    "en": "Warm Salads",
                    "ru": "Теплые салаты",
                    "kk": "Жылы салаттар"
                },
                "items": [
                    {
                        "id": 502,
                        "name": {
                            "en": "Warm Salad with Beef",
                            "ru": "Теплый салат с говядиной",
                            "kk": "Сиыр еті қосылған жылы салат"
                        },
                        "price": 4800,
                        "description": {
                            "en": "Tender strips of grilled beef over mixed greens with a savory balsamic glaze",
                            "ru": "Нежные кусочки говядины гриль на подушке из микс-салата с пикантным бальзамическим соусом",
                            "kk": "Микс-салат және бальзамдық тұздықпен берілетін грильде піскен сиыр етінің кесектері"
                        },
                        "image": "images/foodImages/IMG_1025.JPG"
                    },
                    {
                        "id": 503,
                        "name": {
                            "en": "Grilled Vegetables with Halloumi",
                            "ru": "Овощи гриль с халлуми",
                            "kk": "Халлуми қосылған грильдегі көкөністер"
                        },
                        "price": 4200,
                        "description": {
                            "en": "Seasonal grilled vegetables paired with perfectly seared halloumi cheese",
                            "ru": "Сезонные овощи гриль, поданные с безупречно обжаренным сыром халлуми",
                            "kk": "Керемет қуырылған халлуми ірімшігі және маусымдық гриль көкөністері"
                        },
                        "image": "images/foodImages/IMG_1025.JPG"
                    }
                ]
            }
        ]
    },
    {
        "id": "mains",
        "name": {
            "en": "Mains",
            "ru": "Основные блюда",
            "kk": "Негізгі тағамдар"
        },
        "subcategories": [
             {
                "id": "meat_poultry",
                "name": {
                    "en": "Meat & Poultry",
                    "ru": "Мясо и птица",
                    "kk": "Ет және құс еті"
                },
                "items": [
                     {
                        "id": 6,
                        "name": {
                            "en": "Ribeye Steak with Asparagus",
                            "ru": "Стейк Рибай со спаржей",
                            "kk": "Қояншөп қосылған Рибай стейкі"
                        },
                        "price": 14000,
                        "description": {
                            "en": "Premium cut ribeye steak cooked to your liking, served with buttered asparagus",
                            "ru": "Премиальный стейк Рибай нужной вам прожарки, подается со спаржей в сливочном масле",
                            "kk": "Сарымайға қуырылған қояншөппен берілетін премиум Рибай стейкі"
                        },
                        "image": "images/foodImages/IMG_1440.JPG"
                    },
                    {
                        "id": 601,
                        "name": {
                            "en": "Chicken Breast with Quinoa",
                            "ru": "Куриная грудка с киноа",
                            "kk": "Киноа қосылған тауық төс еті"
                        },
                        "price": 5500,
                        "description": {
                            "en": "Juicy grilled chicken breast served on a bed of healthy, seasoned quinoa",
                            "ru": "Сочная куриная грудка на гриле на подушке из полезного киноа со специями",
                            "kk": "Дәмдәуірлері бар пайдалы киноаның үстіндегі шырынды гриль тауық төс еті"
                        },
                        "image": "images/foodImages/IMG_1443.JPG"
                    }
                ]
            },
            {
                "id": "pasta_risotto",
                "name": {
                    "en": "Pasta & Risotto",
                    "ru": "Паста и ризотто",
                    "kk": "Паста және ризотто"
                },
                "items": [
                    {
                        "id": 602,
                        "name": {
                            "en": "Truffle Mushroom Risotto",
                            "ru": "Трюфельное ризотто с грибами",
                            "kk": "Саңырауқұлақ және трюфель ризоттосы"
                        },
                        "price": 6200,
                        "description": {
                            "en": "Creamy Arborio rice with wild mushrooms, finished with premium truffle oil",
                            "ru": "Сливочный рис Арборио с лесными грибами и премиальным трюфельным маслом",
                            "kk": "Орман саңырауқұлақтары және премиум трюфель майы қосылған кілегейлі Арборио күріші"
                        },
                        "image": "images/foodImages/IMG_1456.JPG"
                    },
                    {
                        "id": 603,
                        "name": {
                            "en": "Carbonara",
                            "ru": "Паста Карбонара",
                            "kk": "Карбонара пастасы"
                        },
                        "price": 4900,
                        "description": {
                            "en": "Authentic Italian spaghetti with crispy pancetta, egg yolk, and pecorino romano",
                            "ru": "Аутентичные итальянские спагетти с хрустящей панчеттой, яичным желтком и пекорино романо",
                            "kk": "Қытырлақ панчетта, жұмыртқаның сарыуызы және пекорино романо қосылған италияндық спагетти"
                        },
                        "image": "images/foodImages/IMG_1469.JPG"
                    }
                ]
            }
        ]
    },
    {
        "id": "desserts",
        "name": {
            "en": "Desserts",
            "ru": "Десерты",
            "kk": "Десерттер"
        },
        "subcategories": [
            {
                "id": "cakes",
                "name": {
                    "en": "Cakes",
                    "ru": "Торты",
                    "kk": "Торттар"
                },
                "items": [
                    {
                        "id": 701,
                        "name": {
                            "en": "Honey Cake",
                            "ru": "Медовик",
                            "kk": "Балды торт"
                        },
                        "price": 2800,
                        "description": {
                            "en": "Traditional Russian layered honey cake with sour cream frosting",
                            "ru": "Традиционный слоеный медовый торт со сметанно-сливочным кремом",
                            "kk": "Қаймақ-кілегей кремі бар дәстүрлі қабатты балды торт"
                        },
                        "image": "images/foodImages/IMG_1025.JPG"
                    },
                    {
                        "id": 702,
                        "name": {
                            "en": "San Sebastian Cheesecake",
                            "ru": "Чизкейк Сан-Себастьян",
                            "kk": "Сан-Себастьян чизкейкі"
                        },
                        "price": 3500,
                        "description": {
                            "en": "Basque burnt cheesecake with a beautifully caramelized exterior and creamy center",
                            "ru": "Баскский обожженный чизкейк с карамелизированной корочкой и нежным центром",
                            "kk": "Карамельденген қабығы бар және ортасы өте жұмсақ Баск күйдірілген чизкейкі"
                        },
                        "image": "images/foodImages/IMG_1443.JPG"
                    }
                ]
            }
        ]
    }
]
