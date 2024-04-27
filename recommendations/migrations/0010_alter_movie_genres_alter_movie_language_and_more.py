# Generated by Django 4.2.10 on 2024-04-27 20:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0009_recommendation_recommended_films_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('', 'No Preference'), ('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Ficti', 'Science Fiction'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=13), size=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('', 'No Preference'), ('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bi', 'Bislama'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('cn', 'Cantonese'), ('ca', 'Catalan'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('ny', 'Chichewa; Nyanja'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Divehi'), ('nl', 'Dutch'), ('dz', 'Dzongkha'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ff', 'Fulah'), ('gd', 'Gaelic'), ('gl', 'Galician'), ('lg', 'Ganda'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian; Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('ig', 'Igbo'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiaq'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('ki', 'Kikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('kj', 'Kuanyama'), ('ku', 'Kurdish'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('lb', 'Letzeburgesch'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('zh', 'Mandarin'), ('gv', 'Manx'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mh', 'Marshall'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('nv', 'Navajo'), ('nr', 'Ndebele'), ('nd', 'Ndebele'), ('ng', 'Ndonga'), ('ne', 'Nepali'), ('xx', 'No Language'), ('se', 'Northern Sami'), ('no', 'Norwegian'), ('nb', 'Norwegian Bokmål'), ('nn', 'Norwegian Nynorsk'), ('oc', 'Occitan'), ('oj', 'Ojibwa'), ('or', 'Oriya'), ('om', 'Oromo'), ('os', 'Ossetian; Ossetic'), ('pi', 'Pali'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('ps', 'Pushto'), ('qu', 'Quechua'), ('rm', 'Raeto-Romance'), ('ro', 'Romanian'), ('rn', 'Rundi'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sango'), ('sa', 'Sanskrit'), ('sc', 'Sardinian'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('sn', 'Shona'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('cu', 'Slavic'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('st', 'Sotho'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('ty', 'Tahitian'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tn', 'Tswana'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('ii', 'Yi'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang'), ('zu', 'Zulu')], max_length=2),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('', 'No Preference'), ('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Ficti', 'Science Fiction'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=13), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('', 'No Preference'), ('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bi', 'Bislama'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('cn', 'Cantonese'), ('ca', 'Catalan'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('ny', 'Chichewa; Nyanja'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Divehi'), ('nl', 'Dutch'), ('dz', 'Dzongkha'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ff', 'Fulah'), ('gd', 'Gaelic'), ('gl', 'Galician'), ('lg', 'Ganda'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian; Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('ig', 'Igbo'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiaq'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('ki', 'Kikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('kj', 'Kuanyama'), ('ku', 'Kurdish'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('lb', 'Letzeburgesch'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('zh', 'Mandarin'), ('gv', 'Manx'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mh', 'Marshall'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('nv', 'Navajo'), ('nr', 'Ndebele'), ('nd', 'Ndebele'), ('ng', 'Ndonga'), ('ne', 'Nepali'), ('xx', 'No Language'), ('se', 'Northern Sami'), ('no', 'Norwegian'), ('nb', 'Norwegian Bokmål'), ('nn', 'Norwegian Nynorsk'), ('oc', 'Occitan'), ('oj', 'Ojibwa'), ('or', 'Oriya'), ('om', 'Oromo'), ('os', 'Ossetian; Ossetic'), ('pi', 'Pali'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('ps', 'Pushto'), ('qu', 'Quechua'), ('rm', 'Raeto-Romance'), ('ro', 'Romanian'), ('rn', 'Rundi'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sango'), ('sa', 'Sanskrit'), ('sc', 'Sardinian'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('sn', 'Shona'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('cu', 'Slavic'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('st', 'Sotho'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('ty', 'Tahitian'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tn', 'Tswana'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('ii', 'Yi'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang'), ('zu', 'Zulu')], max_length=2), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='runtime_span',
            field=models.CharField(blank=True, choices=[('', 'No Preference'), ('0-90', '90 or less'), ('90-120', '90-120'), ('120-150', '120-150'), ('150-900', '150 or more')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='year_span',
            field=models.CharField(blank=True, choices=[('', 'No Preference'), ('1900-1960', '1960 and before'), ('1960-1979', '1960-1979'), ('1980-1999', '1980-1999'), ('2000-2024', '2000 and after')], max_length=9, null=True),
        ),
    ]
