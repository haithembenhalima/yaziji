#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data_const.py
#  
#  Copyright 2023 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from flask_babel import lazy_gettext as _

selectValues = {"fields": [
  "subject",
  "verb",
  "auxiliary",
  "tense",
  "voice",
  "negative",
  "object",
  "time",
  "place",
    "adjective",
  "phrase_type",

],
 "phrase_type":{ 
   "جملة فعلية":  _('جملة فعلية'),
 "جملة اسمية":  _('جملة اسمية'),
 },
"auxiliary":{
    "اِسْتَطَاعَ":_("اِسْتَطَاعَ"),
    "أَرَادَ":_("أَرَادَ"),
    "كَادَ":_("كَادَ"),
},
"verb":{
    "شَرِبَ":_("شَرِبَ"),
    "ضَرَبَ":_("ضَرَبَ"),
    "ذَهَبَ":_("ذَهَبَ"),
    "جَلَسَ":_("جَلَسَ"),
    "شَبِعَ":_("شَبِعَ"),
    "أَكَلَ":_("أَكَلَ"),
    "خَرَجَ":_("خَرَجَ"),
    "مَشَى":_("مَشَى"),
    "قَامَ":_("قَامَ"),
    "نَجَحَ":_("نَجَحَ"),
    "بَكَى":_("بَكَى"),
    "سَمِعَ":_("سَمِعَ"),
    "جَاءَ":_("جَاءَ"),
    "عَرَفَ":_("عَرَفَ"),
    "رَسَبَ":_("رَسَبَ"),
    "تَعَلَّمَ":_("تَعَلَّمَ"),
    "لَعِبَ":_("لَعِبَ"),
    "جَعَلَ":_("جَعَلَ"),
    "شَكَرَ":_("شَكَرَ"),
    "جَهَّزَ":_("جَهَّزَ"),
    "وَعَدَ":_("وَعَدَ"),
    "عَاشَ":_("عَاشَ"),
    "وَقَفَ":_("وَقَفَ"),
    "سَجَدَ":_("سَجَدَ"),
    "مَاتَ":_("مَاتَ"),
    "قَبَضَ":_("قَبَضَ"),
    "غَفَرَ":_("غَفَرَ"),
    "صَامَ":_("صَامَ"),
    "رَسَمَ":_("رَسَمَ"),
    "نَزَلَ":_("نَزَلَ"),
    "رَكَعَ":_("رَكَعَ"),
    "سَافَرَ":_("سَافَرَ"),
    "وَفَى":_("وَفَى"),
    "لَبِسَ":_("لَبِسَ"),
    "اجْتَهَدَ":_("اجْتَهَدَ"),
    "وَجَدَ":_("وَجَدَ"),
    "وَصَلَ":_("وَصَلَ"),
    "قَرَأَ":_("قَرَأَ"),
    "قَعَدَ":_("قَعَدَ"),
    "قَالَ":_("قَالَ"),
    "خَبَّرَ":_("خَبَّرَ"),
    "عَلِمَ":_("عَلِمَ"),
    "ضَرَبَ":_("ضَرَبَ"),
    "سَأَلَ":_("سَأَلَ"),
    "رَمَى":_("رَمَى"),
    "شَاهَدَ":_("شَاهَدَ"),
    "أَخَذَ":_("أَخَذَ"),
    "طَلَعَ":_("طَلَعَ"),
    "حَفِظَ":_("حَفِظَ"),
    "أَخْبَرَ":_("أَخْبَرَ"),
    "نَامَ":_("نَامَ"),
    "سَاعَدَ":_("سَاعَدَ"),
    "كَتَبَ":_("كَتَبَ"),
    "حَدَّثَ":_("حَدَّثَ"),
    "جَرَى":_("جَرَى"),
    "اشْتَرَى":_("اشْتَرَى"),
    "أَسْرَعَ":_("أَسْرَعَ"),
    "شَرِبَ":_("شَرِبَ"),
    "ذَهَبَ":_("ذَهَبَ"),
    "ذَاكَرَ":_("ذَاكَرَ"),
    "وَضَعَ":_("وَضَعَ"),
    "بَاعَ":_("بَاعَ"),
    "جَلَسَ":_("جَلَسَ"),
    "فَهِمَ":_("فَهِمَ"),
    "فَتَحَ":_("فَتَحَ"),
    "عَطِشَ":_("عَطِشَ"),
    "سَكَنَ":_("سَكَنَ"),
    "أَعْلَمَ":_("أَعْلَمَ"),
    "كَسَرَ":_("كَسَرَ"),
    "دَخَلَ":_("دَخَلَ"),
},
"tense":{
    "الماضي المعلوم":_("الماضي المعلوم"),
    "المضارع المعلوم":_("المضارع المعلوم"),
    "الأمر":_("الأمر"),
},
"voice":{
    "معلوم":_("معلوم"),
    "مبني للمجهول":_("مبني للمجهول"),
},
"negative":{
    "مثبت":_("مثبت"),
    "منفي":_("منفي"),
},
"object":{
    "حَلِيبٌ":_("حَلِيبٌ"),
    "بَابٌ":_("بَابٌ"),
    "أنا":_("أنا"),
    "نحن":_("نحن"),
    "أنت":_("أنت"),
    "أنتِ":_("أنتِ"),
    "أنتما":_("أنتما"),
    "أنتما مؤ":_("أنتما مؤ"),
    "أنتم":_("أنتم"),
    "أنتن":_("أنتن"),
    "هو":_("هو"),
    "هي":_("هي"),
    "هما":_("هما"),
    "هما مؤ":_("هما مؤ"),
    "هم":_("هم"),
    "هن":_("هن"),
        "تُفَاحَةٌ":_("تُفَاحَةٌ"),
    "تِلْمِيذٌ":_("تِلْمِيذٌ"),
    "ثَوْبٌ":_("ثَوْبٌ"),
    "جَبَلٌ":_("جَبَلٌ"),
    "حَقِيبَةٌ":_("حَقِيبَةٌ"),
    "حَلِيبٌ":_("حَلِيبٌ"),
    "خُضَرٌ":_("خُضَرٌ"),
    "دَرْسٌ":_("دَرْسٌ"),
    "رَجُلٌ":_("رَجُلٌ"),
    "شَعْرٌ":_("شَعْرٌ"),
    "صَحْرَاءٌ":_("صَحْرَاءٌ"),
    "صَوْتٌ":_("صَوْتٌ"),
    "طَعَامٌ":_("طَعَامٌ"),
    "طَلَبَةٌ":_("طَلَبَةٌ"),
    "عَصِيرٌ":_("عَصِيرٌ"),
    "عَلَمٌ":_("عَلَمٌ"),
    "فَوَاكِهٌ":_("فَوَاكِهٌ"),
    "قَمَرٌ":_("قَمَرٌ"),
    "قُرْآنٌ":_("قُرْآنٌ"),
    "قِصَّةٌ":_("قِصَّةٌ"),
    "قِطَّةٌ":_("قِطَّةٌ"),
    "كَأْسٌ":_("كَأْسٌ"),
    "كُرَةٌ":_("كُرَةٌ"),
    "كِتَابٌ":_("كِتَابٌ"),
    "لمْرأَةٌ":_("لمْرأَةٌ"),
    "مدْرَسةٌ":_("مدْرَسةٌ"),
    "مسْرَحِيَّةٌ":_("مسْرَحِيَّةٌ"),
    "مُعَلِمٌ":_("مُعَلِمٌ"),
    "مِحْفَظَةٌ":_("مِحْفَظَةٌ"),
    "نَاسٌ":_("نَاسٌ"),
},
"time":{
    "دَائِمًا":"دَائِمًا",
    "أَوَّلَ أَمْسِ":"أَوَّلَ أَمْسِ",
    "الْبَارِحَةَ":"الْبَارِحَةَ",
    "أَحْيَانًا":"أَحْيَانًا",
    "بَعْدَ غَدٍ":"بَعْدَ غَدٍ",
    "مَسَاءً":"مَسَاءً",
    "أَمْسِ":"أَمْسِ",
    "الْيَوْمَ":"الْيَوْمَ",
    "غَدًا":"غَدًا",
    "صَبَاحًا":"صَبَاحًا",
    "كُلَّ يَوْمٍ":"كُلَّ يَوْمٍ",
    # ~ "أَثْنَاءَ":_("أَثْنَاءَ"),
    "أَحْيَانًا":_("أَحْيَانًا"),
    "البَارِحَةَ":_("البَارِحَةَ"),
    "اليَوْمَ":_("اليَوْمَ"),
    # ~ "رَبِيعَ":_("رَبِيعَ"),
    "سَاعَةً":_("سَاعَةً"),
    "سَنَةً":_("سَنَةً"),
    "شِتَاءً":_("شِتَاءً"),
    "صَبَاحًا":_("صَبَاحًا"),
    "صَيْفًا":_("صَيْفًا"),
    "ظُهْرًا":_("ظُهْرًا"),
    # ~ "عَامٍ":_("عَامٍ"),
    "عَصْرًا":_("عَصْرًا"),
    "غَدًا":_("غَدًا"),
    "فَجْرًا":_("فَجْرًا"),
    # ~ "قَبْلَ":_("قَبْلَ"),
    "لَحْظَةَ":_("لَحْظَةَ"),
    "لَيْلًا":_("لَيْلًا"),
    "مَسَاءً":_("مَسَاءً"),
    "نَهْارًا":_("نَهْارًا"),
    # ~ "وَقْتَ":_("وَقْتَ"),    
},
"place":{
    "بَيْتٌ":_("بَيْتٌ"),
    "حَدِيقَةٌ":_("حَدِيقَةٌ"),
    "سُوقٌ":_("سُوقٌ"),
    "طَرِيقٌ":_("طَرِيقٌ"),
    "غُرْفَةٌ":_("غُرْفَةٌ"),
    "فِنَاءٌ":_("فِنَاءٌ"),
    "مَدِينَةٌ":_("مَدِينَةٌ"),
    "مَدْرَسَةٌ":_("مَدْرَسَةٌ"),
    "مَسْجِدٌ":_("مَسْجِدٌ"),
    "مَطْبَخٌ":_("مَطْبَخٌ"),    
    
    # ~ "أَمَاَمَ":_("أَمَاَمَ"),
    # ~ "بَيْنَ":_("بَيْنَ"),
    # ~ "تَحْتَ":_("تَحْتَ"),
    # ~ "جَنُوبَ":_("جَنُوبَ"),
    # ~ "حَوْلَ":_("حَوْلَ"),
    # ~ "خَارِجَ":_("خَارِجَ"),
    # ~ "خَلْفَ":_("خَلْفَ"),
    # ~ "دَاخِلَ":_("دَاخِلَ"),
    # ~ "شَرْقَ":_("شَرْقَ"),
    # ~ "شَمَالَ":_("شَمَالَ"),
    # ~ "غَرْبَ":_("غَرْبَ"),
    # ~ "فَوْقَ":_("فَوْقَ"),
    # ~ "وَرَاءَ":_("وَرَاءَ"),
    # ~ "وَسَطَ":_("وَسَطَ"),
    # ~ "يَسَارَ":_("يَسَارَ"),
    # ~ "يَمِينَ":_("يَمِينَ"),    
    },
"adjectives": {
    "أَنِيقٌ":_("أَنِيقٌ"),
    "بَخِيلٌ":_("بَخِيلٌ"),
    "بَشِعٌ":_("بَشِعٌ"),
    "بَطِيءٌ":_("بَطِيءٌ"),
    "جَمِيلٌ":_("جَمِيلٌ"),
    "حَزِينٌ":_("حَزِينٌ"),
    "حَنُونٌ":_("حَنُونٌ"),
    "ذَكِيٌ":_("ذَكِيٌ"),
    "سَرِيعٌ":_("سَرِيعٌ"),
    "سَعِيدٌ":_("سَعِيدٌ"),
    "سَمِينٌ":_("سَمِينٌ"),
    "شُجَاعٌ":_("شُجَاعٌ"),
    "ضَعِيفٌ":_("ضَعِيفٌ"),
    "طَوِيلٌ":_("طَوِيلٌ"),
    "غَبِيٌ":_("غَبِيٌ"),
    "فَرِحٌ":_("فَرِحٌ"),
    "قَصِيرٌ":_("قَصِيرٌ"),
    "قَوِيٌ":_("قَوِيٌ"),
    "كَرِيمٌ":_("كَرِيمٌ"),
    "كَسُولٌ":_("كَسُولٌ"),
    "لَئِيمٌ":_("لَئِيمٌ"),
    "مَسْرُورٌ":_("مَسْرُورٌ"),
    "مُبْتَهِجٌ":_("مُبْتَهِجٌ"),
    "مُجْتَهِدٌ":_("مُجْتَهِدٌ"),
    "مُرْتَفِعٌ":_("مُرْتَفِعٌ"),
    "مُنْخَفِضٌ":_("مُنْخَفِضٌ"),
    "هَزِيلٌ":_("هَزِيلٌ"),
    "وَسِيمٌ":_("وَسِيمٌ"),
    },
 "subject":{
    # "أَحْمَد":_("أَحْمَد"),
    "وَلَدٌ":_("وَلَدٌ"),
    "أنا":_("أنا"),
    "نحن":_("نحن"),
    "أنت":_("أنت"),
    "أنتِ":_("أنتِ"),
    "أنتما":_("أنتما"),
    "أنتما مؤ":_("أنتما مؤ"),
    "أنتم":_("أنتم"),
    "أنتن":_("أنتن"),
    "هو":_("هو"),
    "هي":_("هي"),
    "هما":_("هما"),
    "هما مؤ":_("هما مؤ"),
    "هم":_("هم"),
    "هن":_("هن"),
        "أَبٌ":_("أَبٌ"),
    "أَحْمَدُ":_("أَحْمَدُ"),
    "أَسَدٌ":_("أَسَدٌ"),
    "أُمٌّ":_("أُمٌّ"),
    "اِبْنٌ":_("اِبْنٌ"),
    "بِنْتٌ":_("بِنْتٌ"),
    "تَاجِرٌ":_("تَاجِرٌ"),
    "تِلْمِيذٌ":_("تِلْمِيذٌ"),
    "حِصَانٌ":_("حِصَانٌ"),
    "دِيكٌ":_("دِيكٌ"),
    "رَجُلٌ":_("رَجُلٌ"),
    "رَضِيعٌ":_("رَضِيعٌ"),
    "زُهُورٌ":_("زُهُورٌ"),
    "شُرْطِيٌّ":_("شُرْطِيٌّ"),
    "طَالِبٌ":_("طَالِبٌ"),
    "طَبِيبٌ":_("طَبِيبٌ"),
    "طِفْلٌ":_("طِفْلٌ"),
    "عَامِلٌ":_("عَامِلٌ"),
    "عُمَّالٌ":_("عُمَّالٌ"),
    "فَاطِمَةُ":_("فَاطِمَةُ"),
    "فَرَاشَةٌ":_("فَرَاشَةٌ"),
    "قَاضٌِ":_("قَاضٌِ"),
    "قِطٌّ":_("قِطٌّ"),
    "لَيْلَى":_("لَيْلَى"),
    "معَلِّمٌ":_("معَلِّمٌ"),
    "مَرْأَةٌ":_("مَرْأَةٌ"),
    "مَطَرٌ":_("مَطَرٌ"),
    "مُجْتَهِدٌ":_("مُجْتَهِدٌ"),
    "مُحَمَدُ":_("مُحَمَدُ"),
    "مُسْلِمٌ":_("مُسْلِمٌ"),
    "مُهَنْدِسٌ":_("مُهَنْدِسٌ"),
    "وَلَدٌ":_("وَلَدٌ"),      
},
"web-labels":
    {
    "نوع الجملة:":_("نوع الجملة:"),
    "جملة فعلية":_("جملة فعلية"),
    "جملة اسمية":_("جملة اسمية"),
    "فاعل":_("فاعل"),
    "فعل مساعد":_("فعل مساعد"),
    "فعل:":_("فعل:"),
    "زمن:":_("زمن:"),
    "مبني للمعلوم/مجهول:":_("مبني للمعلوم/مجهول:"),
    "مثبت/منفي:":_("مثبت/منفي:"),
    "مفعول":_("مفعول"),
    "ظرف زمان:":_("ظرف زمان:"),
    "ظرف مكان:":_("ظرف مكان:"),
    "بناء":_("بناء"),
    "عشوائي":_("عشوائي"),
    "عينة":_("عينة"),
    "حركة الإعراب":_("حركة الإعراب"),
        "مدونتي":_("مدونتي"),
    "الاستضافة بدعم من شركة":_("الاستضافة بدعم من شركة"),
    "إظهار حركة الإعراب في أواخر الكلمات":_("إظهار حركة الإعراب في أواخر الكلمات"),
    "اختيار عشوائي للمفردات":_("اختيار عشوائي للمفردات"),
    "نسخ عينة جيسون للتجارب البرمجية":_("نسخ عينة جيسون للتجارب البرمجية"),
    "بناء الجملة":_("بناء الجملة"),
    },
};


