# Blog part 2 (ET): four more posts, written natively in Estonian. Executed after et_seo.py; only adds posts.

T["blog"]["posts"].update({
    "ecommerce-cost": {
        "slug": "e-poe-hind.html",
        "title": "E-poe hind 2026: mis maksab e-poe tegemine? | BoostLab",
        "desc": "E-poe hind 2026: hinnatabel mahu järgi, mis tõstab e-poe tegemise hinda, igakuised kulud ning Shopify, WooCommerce ja kohandatud poe aus võrdlus.",
        "h1": "E-poe hind 2026: mis maksab e-poe tegemine Eestis?",
        "lead": "Selgitame, millest e-poe hind koosneb, mis kulud jätkuvad pärast avamist ja millal tasub valida Shopify, WooCommerce või kohandatud lahendus.",
        "date": "5. november 2026", "iso": "2026-11-05", "minutes": 7,
        "body": """<p>E-poe hinnapakkumised võivad Eestis erineda mitu korda, kuigi kirjeldus on pealtnäha sama: tootekataloog, ostukorv ja kassa. Erinevus peitub detailides. Mitu toodet ja varianti, millised makseviisid, kas tarne arvutatakse automaatselt, kas tellimused liiguvad raamatupidamisse ja mitmes keeles pood töötab. Selles artiklis võtame need detailid lahti, et saaksid pakkumisi võrrelda ja eelarve realistlikult paika panna.</p>
<h2>E-poe hind mahu järgi</h2>
<p>BoostLabis maksab e-pood alates €3,500 ja valmib tavaliselt 3-5 nädalaga. Allolev tabel näitab, kuidas maht hinda ja ajakava mõjutab.</p>
<table><thead><tr><th>Lahendus</th><th>Mida sisaldab</th><th>Hind alates</th><th>Ajakava</th></tr></thead><tbody>
<tr><td>Ühe toote või kampaania leht</td><td>Üks toode või komplekt, tellimisvorm või lihtne makse</td><td>€700</td><td>5-7 tööpäeva</td></tr>
<tr><td>Ettevõtte koduleht väikese kataloogiga</td><td>Teenused ja tooted, päringuvorm, ilma täisostukorvita</td><td>€1,700</td><td>2-3 nädalat</td></tr>
<tr><td>E-pood</td><td>Kataloog, filtrid, ostukorv, kassa, maksed, tarne, halduspaneel</td><td>€3,500</td><td>3-5 nädalat</td></tr>
<tr><td>E-pood koos CRM-i või platvormiga</td><td>B2B hinnakirjad, kliendikontod, laotarkvara, keerukad reeglid</td><td>€4,500</td><td>alates 4 nädalast</td></tr>
</tbody></table>
<p>Kõik hinnad on koondatud lehele <a href="/et/hinnad.html">hinnad</a>. Lõpliku hinna saad pärast lühikest kõnet, kui maht on selge.</p>
<h2>Mis tõstab e-poe tegemise hinda</h2>
<ul>
<li><strong>Kataloogi suurus ja variandid.</strong> Kakskümmend toodet ja kaks tuhat toodet suuruste, värvide ja filtritega on erinev töö. Suure kataloogi puhul on vaja importi failist või tarnija voost, mitte käsitsi sisestamist.</li>
<li><strong>Makseviisid.</strong> Eesti ostja ootab pangalinke ja kaardimakset. Montonio annab ühe liidestusega Eesti, Läti ja Leedu pangalingid, Stripe sobib hästi kaardimakseteks ja rahvusvahelisteks ostjateks. Järelmaks ja liisingud lisavad seadistust.</li>
<li><strong>Tarneliidestused.</strong> Omniva, DPD ja SmartPosti pakiautomaatide valik otse kassas ning pakisildi loomine halduspaneelist säästab iga päev aega. Iga vedaja liidestus vajab seadistust ja testimist.</li>
<li><strong>Raamatupidamine ja ladu.</strong> Tellimuste ja arvete eksport Meritisse, Directosse või muusse tarkvarasse ning laoseisu sünkroonimine laotarkvaraga.</li>
<li><strong>Keeled ja turud.</strong> Eesti, inglise ja vene keel, vajadusel Läti, Leedu või Soome. Iga keel tähendab tõlkeid, hreflangi ja vahel ka eraldi hindu või tarnereegleid.</li>
<li><strong>Käibemaks ja arved.</strong> Eestis on käibemaks 24% ja hinnad peavad poes, korvis ja arvel kokku minema. Kui müüd ka teistesse EL-i riikidesse, vajab käibemaksu loogika eraldi tähelepanu.</li>
<li><strong>B2B funktsioonid.</strong> Kliendipõhised hinnakirjad, ettevõtte kontod ja arvega maksmine teevad poest sisuliselt platvormi.</li>
</ul>
<h2>Igakuised kulud pärast avamist</h2>
<p>Arendus on ühekordne kulu, kuid e-pood maksab ka töötades. Planeeri eelarvesse:</p>
<ul>
<li><strong>Majutus ja domeen.</strong> E-pood vajab kiiret ja turvalist serverit ning igapäevaseid varukoopiaid. Meie seadistame majutuse ja arveldame selle omahinnaga.</li>
<li><strong>Maksetasud.</strong> Makseteenuse pakkuja võtab tasu iga tehingu pealt. Tasud sõltuvad pakkujast, makseviisist ja käibest, seega võrdle Montonio, Stripe'i ja pangalepingute tingimusi oma eeldatava käibe järgi.</li>
<li><strong>Tarne.</strong> Vedajate hinnad sõltuvad lepingust ja mahust. Otsusta varakult, kas tarne on kliendile tasuta, fikseeritud või arvutatakse.</li>
<li><strong>Hooldus.</strong> Turvauuendused, väikesed muudatused ja uued kampaanialehed. Valmisplatvormidel lisanduvad teemade ja pluginate litsentsid.</li>
<li><strong>Turundus.</strong> Uus pood ei too külastajaid iseenesest. Kohalike reklaamikampaaniate puhul soovitame vähemalt €500-1,000 kuus reklaamikuluks, haldustasu eraldi. Kampaania seadistus maksab meil alates €599.</li>
</ul>
<h2>Shopify, WooCommerce või kohandatud e-pood</h2>
<p>Ükski variant ei ole kõigile parim. Aus võrdlus:</p>
<table><thead><tr><th></th><th>Shopify</th><th>WooCommerce</th><th>Kohandatud e-pood</th></tr></thead><tbody>
<tr><td>Alustamine</td><td>Kiire, valmisteemad</td><td>Kiire, palju pluginaid</td><td>3-5 nädalat</td></tr>
<tr><td>Kuukulu</td><td>Paketi kuutasu ja rakenduste tasud</td><td>Majutus ja pluginate litsentsid</td><td>Majutus ja valikuline tugi</td></tr>
<tr><td>Balti makse- ja tarneliidestused</td><td>Rakenduste kaudu, kvaliteet erineb</td><td>Pluginate kaudu, vajab hooldust</td><td>Ehitatakse täpselt vajaduse järgi</td></tr>
<tr><td>Paindlikkus</td><td>Platvormi piirides</td><td>Suur, kuid pluginate konfliktid on tavalised</td><td>Piiranguteta</td></tr>
<tr><td>Kiirus</td><td>Hea, sõltub rakendustest</td><td>Sõltub majutusest ja pluginatest</td><td>Ainult vajalik kood</td></tr>
</tbody></table>
<p>Kui sul on väike kataloog ja tahad homme müüma hakata, on Shopify mõistlik algus. Kui meeskonnas on keegi, kes WordPressi tunneb, võib WooCommerce sobida. Kohandatud e-pood tasub end ära siis, kui vajad erilisi hinnareegleid, B2B kontosid, mitut turgu, tihedat liidestust lao ja raamatupidamisega või lihtsalt poodi, mis on kiire ja kuulub täielikult sulle.</p>
<h2>Mis peab igas e-poes hinnas olema</h2>
<p>Mobiilile kavandatud kassa, pangalingid ja kaardimaksed, pakiautomaadid, tellimuskinnitused e-postiga, halduspaneel toodete ja tellimuste haldamiseks, SEO-struktuur ja schema-märgendus tootelehtedele, Google Analytics 4 koos ostu mõõtmisega ning GDPR-ile vastav küpsiste nõusolek. Kui midagi neist pakkumisest puudub, küsi, kas see on lisatasu eest.</p>
<h2>Kus saab mõistlikult kokku hoida</h2>
<p>Kõike ei pea tegema esimeses versioonis. Alusta ühe turu ja ühe-kahe keelega, kui suurem osa müügist tuleb Eestist. Vali kaks-kolm makseviisi, mida su ostjad päriselt kasutavad, ja üks-kaks vedajat. Tooteandmed valmista ette ühtses tabelis, sest korralik import on odavam kui käsitsi sisestamine. Kokku hoida ei tasu aga kassa, mobiilivaate ja mõõtmise pealt. Just need kolm otsustavad, kas külastaja ostab ja kas sa tead, kust ostja tuli.</p>
<h2>Kuidas saada fikseeritud pakkumine</h2>
<ol>
<li>Pane kirja toodete arv ja variandid, makse- ja tarneviisid ning raamatupidamistarkvara, mida kasutad.</li>
<li>Märgi turud ja keeled, kuhu müüd kohe, ning need, mis tulevad aasta jooksul.</li>
<li>Lisa kaks-kolm e-poodi, mis sulle meeldivad, ja selgita miks.</li>
<li>Pärast 30-minutilist kõnet saad kirjaliku pakkumise mahu, ajakava ja fikseeritud hinnaga.</li>
</ol>
<p>Loe lähemalt meie lehelt <a href="/et/e-poe-tegemine.html">e-poe tegemine</a>. Kui kaalud lihtsamat lahendust, aitab artikkel <a href="/et/blog/kui-palju-maksab-koduleht.html">kui palju maksab koduleht</a>.</p>""",
        "faq": [
            ("Kui palju maksab e-poe tegemine?", "BoostLabis maksab e-pood alates €3,500 ja valmib 3-5 nädalaga. Hind sõltub kataloogi suurusest, makse- ja tarneliidestustest, keeltest ja raamatupidamise ekspordist."),
            ("Millised on e-poe igakuised kulud?", "Majutus, mille arveldame omahinnaga, makseteenuse tehingutasud, tarnekulud ja valikuline hooldus. Kohandatud poe koodile litsentsitasusid ei ole."),
            ("Kas Shopify on odavam kui kohandatud e-pood?", "Alguses tavaliselt jah. Pikas plaanis lisanduvad paketi kuutasu ja rakenduste tasud ning Balti makse- ja tarneliidestused sõltuvad kolmandatest osapooltest. Võrdle kogukulu mitme aasta peale."),
        ],
        "services": ["web"],
    },
    "crm-construction": {
        "slug": "crm-ehitusettevottele.html",
        "title": "CRM ehitusettevõttele: objektid ja pakkumised | BoostLab",
        "desc": "CRM ehitusettevõttele: päringud kodulehelt, hinnapakkumised, objektikaardid, alltöövõtjad, fotoaruanded, aktid ja arved ning materjalikulu ühes kohas.",
        "h1": "CRM ehitusettevõttele: päringust üleandmisaktini",
        "lead": "Ehitus- ja remondifirma töö ei lõpe tehinguga, see alles algab. Kirjeldame, mida peab ehitusettevõtte CRM sisaldama ja millal valida kohandatud süsteem.",
        "date": "5. november 2026", "iso": "2026-11-05", "minutes": 7,
        "body": """<p>Tüüpiline müügi CRM lõpeb hetkel, kui tehing on võidetud. Ehitusettevõttel algab siis kõige keerulisem osa: objekt, meeskonnad, alltöövõtjad, materjalid, lisatööd, aktid ja arved. Kui see kõik elab Excelis, WhatsAppi gruppides ja projektijuhi peas, kaob raha märkamatult. Selles artiklis kirjeldame, kuidas näeb välja CRM, mis sobib ehitus- ja remondiettevõttele.</p>
<h2>1. Päringud ühte kohta</h2>
<p>Päringud tulevad kodulehe vormist, telefonist, e-postist, Facebookist ja soovitajatelt. CRM kogub need ühte nimekirja, märgib allika ja määrab vastutaja. Kodulehe vormis tasub küsida kohe olulist: töö liik, objekti asukoht, pindala, soovitud algus ja fotod. Nii saab hindaja esimese kõne ajal juba sisuliselt rääkida ning näed hiljem, milline kanal toob tellimusi, mitte ainult kõnesid.</p>
<h2>2. Hinnapakkumised ja kalkulatsioonid</h2>
<p>Pakkumine on ehitusfirmas müügi süda. CRM-is koostatakse see töö- ja materjaliridade põhjal, kasutades sinu enda ühikuhindu ja juurdehindlust. Pakkumisest tekib PDF sinu kujundusega, mis saadetakse kliendile otse süsteemist. Süsteem jätab meelde versioonid, sest pakkumine muutub sageli kaks-kolm korda, ja tuletab meelde, kui klient pole mõne päeva jooksul vastanud.</p>
<h2>3. Objektikaart</h2>
<p>Kui pakkumine on kinnitatud, muutub see objektiks. Objektikaardil on ühes kohas:</p>
<ul>
<li>kliendi ja kontaktisikute andmed, aadress ja ligipääsu info;</li>
<li>kinnitatud pakkumine, leping ja kõik lisatööd eraldi ridadena;</li>
<li>ajakava ja etapid, vastutav projektijuht ja meeskonnad;</li>
<li>dokumendid, joonised ja kirjavahetus;</li>
<li>eelarve võrdlus tegelike kuludega.</li>
</ul>
<p>Lisatööd on koht, kus raha kõige sagedamini kaob. Kui lisatöö kirjutatakse objektikaardile kohe ja klient kinnitab selle e-posti teel, ei teki lõpparvel vaidlust.</p>
<h2>4. Alltöövõtjad</h2>
<p>Elektrikud, torulukksepad, plaatijad ja katusemeistrid on sageli alltöövõtjad. CRM-is on igal alltöövõtjal oma kaart: kontaktid, valdkond, hinnad, varasemad objektid ja märkmed kvaliteedi kohta. Objektil näed, kes millal kohal on ja milline töö on neile antud. Vajadusel saab alltöövõtja piiratud ligipääsuga vaadata ainult oma ülesandeid.</p>
<h2>5. Fotoaruanded objektilt</h2>
<p>Foto enne, ajal ja pärast tööd on ehituses parim tõend. Meister teeb pildid telefoniga otse objektikaardile, süsteem lisab kuupäeva ja etapi. Varjatud tööd, näiteks hüdroisolatsioon või juhtmestik enne seina sulgemist, on dokumenteeritud ka siis, kui garantiiküsimus tekib aastate pärast. Fotodest saab koostada kliendile aruande ühe nupuvajutusega.</p>
<h2>6. Aktid ja arved</h2>
<p>Etapi lõpus koostatakse CRM-is akt tehtud tööde kohta, klient kinnitab selle ja aktist tekib arve. Ettemaksu-, vahe- ja lõpparved on objektiga seotud, nii et näed alati, kui palju on arveldatud ja kui palju laekunud. Arved saab eksportida raamatupidamistarkvarasse, näiteks Meritisse või Directosse, et andmeid ei peaks kaks korda sisestama.</p>
<h2>7. Materjalikulu</h2>
<p>Materjalide ostud märgitakse objektile kas käsitsi, tšeki fotoga või hankija arve põhjal. Nii näed objekti tegelikku kasumit juba töö käigus, mitte kuu lõpus. Kui materjalikulu ületab eelarvet, saab projektijuht sellest teada siis, kui veel on aega reageerida.</p>
<h2>8. Mobiil objektil</h2>
<p>Ehituses ei istu keegi kontoris arvuti taga. CRM peab töötama telefonis: tänased ülesanded, objekti aadress navigeerimiseks, fotode üleslaadimine, materjali märkimine ja akti allkirjastamine. Kui ühendus objektil on nõrk, peab rakendus andmed hiljem sünkroonima. Vajadusel saab CRM-i juurde teha ka eraldi <a href="/et/mobiilirakendused.html">mobiilirakenduse</a>.</p>
<h2>9. Aruanded juhile</h2>
<p>Kui andmed on ühes kohas, tekivad aruanded iseenesest. Juht näeb, mitu päringut tuli ja kui suur osa neist muutus pakkumiseks ja lepinguks, milline on objektide tegelik kasum võrreldes eelarvega, kui palju on arveldamata ja laekumata ning millised alltöövõtjad peavad tähtaegadest kinni. Need numbrid aitavad otsustada, milliseid töid tasub rohkem müüa ja kus hinnastus vajab ülevaatamist.</p>
<h2>Mida jätta esimesest versioonist välja</h2>
<p>Ehitusettevõtte CRM ei pea esimesel päeval kõike oskama. Kõige rohkem väärtust annavad tavaliselt päringud, pakkumised, objektikaart ja fotod. Aktid, materjalikulu ja alltöövõtjate portaal võivad tulla teises etapis, kui meeskond on süsteemiga harjunud. Nii jõuab CRM kiiremini kasutusse ja edasiarendus põhineb päris kogemusel, mitte oletustel.</p>
<h2>Valmislahendus või kohandatud CRM</h2>
<table><thead><tr><th></th><th>Valmis CRM või projektitarkvara</th><th>Kohandatud CRM</th></tr></thead><tbody>
<tr><td>Alustamine</td><td>Päevad</td><td>Alates 4 nädalast</td></tr>
<tr><td>Hind</td><td>Kuutasu kasutaja kohta</td><td>Ühekordne arendus alates €4,500</td></tr>
<tr><td>Pakkumised sinu ühikuhindadega</td><td>Sageli piiratud või lisamoodul</td><td>Sinu kalkulatsiooniloogika järgi</td></tr>
<tr><td>Aktid, lisatööd, alltöövõtjad</td><td>Osaliselt, eri tööriistades</td><td>Ühes süsteemis</td></tr>
<tr><td>Meistrite ligipääs</td><td>Iga kasutaja lisab kuutasu</td><td>Kasutajate arv kulu ei suurenda</td></tr>
</tbody></table>
<p>Kui ettevõttes on paar inimest ja objektid on väikesed, alusta valmislahendusega. Kui meistreid ja alltöövõtjaid on palju ning pakkumised, aktid ja lisatööd on igapäevane töö, on kohandatud CRM tavaliselt pikas plaanis odavam ja sobib protsessiga paremini. Arvutusloogika on lahti kirjutatud artiklis <a href="/et/blog/kohandatud-crm-voi-pipedrive.html">kohandatud CRM või Pipedrive</a>.</p>
<h2>Kuidas alustada</h2>
<ol>
<li>Kirjelda ühe tüüpilise objekti teekond päringust lõpparveni.</li>
<li>Märgi kohad, kus andmeid kopeeritakse käsitsi või info läheb kaduma.</li>
<li>Otsusta, mis peab olema esimeses versioonis ja mis võib tulla hiljem.</li>
</ol>
<p>Kaardistuskõne järel saad klõpsatava prototüübi ja fikseeritud hinna. Vaata lähemalt lehte <a href="/et/crm-susteemid.html">CRM-süsteemid</a>.</p>""",
        "faq": [
            ("Kui palju maksab CRM ehitusettevõttele?", "Kohandatud CRM maksab meil alates €4,500 ja arendus võtab alates 4 nädalast. Pakkumiste, aktide, alltöövõtjate ja mobiilse kasutusega süsteemile teeme fikseeritud pakkumise pärast kaardistuskõnet."),
            ("Kas meistrid saavad CRM-i telefonis kasutada?", "Jah. Ülesanded, objekti info, fotod, materjalikulu ja aktid on telefonis kättesaadavad. Vajadusel teeme ka eraldi mobiilirakenduse."),
            ("Kas CRM saab arved raamatupidamisse saata?", "Jah. Arved ja aktid saab eksportida raamatupidamistarkvarasse, näiteks Meritisse või Directosse, et andmeid ei peaks kaks korda sisestama."),
        ],
        "services": ["crm"],
    },
    "google-ads-small-business": {
        "slug": "google-ads-vaikeettevottele.html",
        "title": "Google Ads reklaam väikeettevõttele: juhend | BoostLab",
        "desc": "Google Ads reklaam väikeettevõttele Eestis: eelarve loogika, otsingureklaam või Performance Max, märksõnad, konversioonide mõõtmine ja esimese kuu plaan.",
        "h1": "Google Ads reklaam väikeettevõttele: kuidas mitte raha põletada",
        "lead": "Google Ads võib väikeettevõttele tuua päringuid juba esimesel nädalal või kulutada eelarve ilma ühegi kõneta. Vahe tuleb seadistusest, mitte eelarve suurusest.",
        "date": "5. november 2026", "iso": "2026-11-05", "minutes": 7,
        "body": """<p>Väikeettevõtte omanik käivitab Google Adsi sageli ise: paar märksõna, päevaeelarve ja reklaamitekst. Paari nädala pärast on raha kulunud, kuid päringuid pole ja tunne on, et "Google Ads ei tööta". Tavaliselt töötab Google Ads hästi, kui mõõtmine, märksõnad ja maandumisleht on paigas. Siin on juhend, mis aitab seda teha õigesti.</p>
<h2>Eelarve loogika</h2>
<p>Google Ads on oksjon. Iga kord, kui keegi otsib, võistlevad reklaamijad koha pärast. Hinda mõjutavad sinu pakkumine ja kvaliteediskoor (Quality Score), mis sõltub reklaami asjakohasusest, eeldatavast klikkimissagedusest ja maandumislehe kogemusest. Parem reklaam ja parem leht tähendavad sama koha eest madalamat klikihinda.</p>
<p>Eelarve tuleb tuletada eesmärgist, mitte vastupidi. Lihtne arvutus: kui palju maksab klikk sinu märksõnadel, mitu klikki on vaja ühe päringu saamiseks ja mitu päringut ühe kliendi saamiseks. Kohalike kampaaniate puhul soovitame alustada vähemalt €500-1,000 kuus reklaamikuluga, haldustasu eraldi. Väiksema eelarvega kogub kampaania andmeid liiga aeglaselt ja otsused põhinevad juhusel.</p>
<h2>Otsingureklaam või Performance Max</h2>
<ul>
<li><strong>Otsingureklaam</strong> näitab sinu reklaami inimestele, kes otsivad konkreetset teenust, näiteks "katusepesu Tallinn". Kontroll märksõnade üle on suur ja tulemusi on lihtne lugeda. Väikeettevõttele on see peaaegu alati õige algus.</li>
<li><strong>Performance Max</strong> näitab reklaami otsingus, YouTube'is, Gmailis, kaartidel ja partnerlehtedel ning otsustab ise, kus. See vajab head konversioonide mõõtmist ja piisavalt andmeid. Ilma nendeta võib eelarve minna odavatele, kuid kasututele näitamistele.</li>
</ul>
<p>Mõistlik järjekord: alusta otsingureklaamiga, seadista mõõtmine ja lisa Performance Max hiljem, kui konversioone on piisavalt. E-poele võib Performance Max tootevooga sobida varem.</p>
<h2>Märksõnad ja negatiivsed märksõnad</h2>
<p>Vali märksõnad, mis näitavad ostukavatsust: teenus koos linna, hinna või sõnaga "tellida". Väldi liiga laiu sõnu, näiteks lihtsalt "remont", mis toob otsijaid, kes otsivad õpetusi, töökohti või hoopis midagi muud.</p>
<p>Negatiivsed märksõnad on sama olulised kui märksõnad. Lisa kohe algul sõnad nagu "tasuta", "töö", "koolitus", "ise" ja "kasutatud", kui need sinu ärile ei sobi. Esimestel nädalatel vaata otsinguterminite aruannet mitu korda nädalas ja lisa negatiivseks kõik, mis ei too kliente. Eestis tasub eraldi mõelda ka keelele: eesti- ja venekeelsed otsingud vajavad eraldi reklaamirühmi ja tekste.</p>
<h2>Maandumisleht</h2>
<p>Reklaam toob inimese lehele, aga müüb leht. Hea maandumisleht vastab otsingule otse: sama teenus, mis märksõnas, selge hind või hinnavahemik, usaldust tekitavad faktid ja üks selge samm, näiteks vorm või helistamisnupp. Leht peab telefonis kiiresti laadima, sest suur osa kohalikest otsingutest tehakse mobiilis. Kui sul sellist lehte pole, saab maandumislehe teha 5-7 tööpäevaga alates €700. Rohkem loe artiklist <a href="/et/blog/maandumisleht-voi-koduleht.html">maandumisleht või koduleht</a>.</p>
<h2>Konversioonide mõõtmine</h2>
<p>Ilma mõõtmiseta ei tea sina ega Google, millised klikid toovad kliente. Mõõda vähemalt:</p>
<ul>
<li>vormi saatmist tänulehe või sündmuse põhjal;</li>
<li>kõnesid: klikki telefoninumbril ja vajadusel reklaamist tulnud kõnesid;</li>
<li>klikki e-posti aadressil;</li>
<li>e-poe puhul ostu koos summaga.</li>
</ul>
<p>Seadista Google Analytics 4 ja Google Adsi konversioonid nii, et need järgiksid küpsiste nõusolekut. Kontrolli testpäringuga, et konversioon päriselt jõuab Google Adsi.</p>
<h2>Reklaamitekstid ja laiendused</h2>
<p>Hea reklaamitekst kordab otsingut ja annab põhjuse klikkida: hind, tarneaeg, garantii, piirkond või kogemus. Kirjuta mitu pealkirja ja kirjeldust, et Google saaks kombinatsioone testida, kuid hoia sõnum täpne. Lisa laiendused: telefoninumber, asukoht, lisalingid teenuselehtedele ja täpsustused nagu "tasuta hinnapakkumine". Need muudavad reklaami suuremaks ja annavad kasutajale rohkem põhjusi just sind valida. Kohaliku äri puhul seo reklaamikontoga ka Google'i ettevõtteprofiil, et aadress ja arvustused oleksid nähtavad.</p>
<h2>Esimese 30 päeva plaan</h2>
<table><thead><tr><th>Aeg</th><th>Tegevus</th></tr></thead><tbody>
<tr><td>Enne käivitamist</td><td>Konto sinu nimele, mõõtmine, märksõnad, negatiivsed märksõnad, reklaamid, maandumisleht</td></tr>
<tr><td>1. nädal</td><td>Otsinguterminite kontroll 2-3 korda, negatiivsete lisamine, eelarve jaotuse kontroll</td></tr>
<tr><td>2. nädal</td><td>Kallid ja tulemusteta märksõnad pausile, reklaamitekstide võrdlus</td></tr>
<tr><td>3. nädal</td><td>Maandumislehe parandused päris käitumise põhjal, ajakava ja asukoha korrigeerimine</td></tr>
<tr><td>4. nädal</td><td>Kokkuvõte: kulu, päringud, hind päringu kohta, järgmise kuu plaan</td></tr>
</tbody></table>
<p>Pärast esimest kuud on sul päris number: mis maksab üks päring. Võrdle seda kliendi keskmise väärtusega. Kui päring maksab vähem, kui ettevõte selle pealt teenib, tasub eelarvet järk-järgult tõsta. Kui rohkem, vaata enne eelarve kärpimist üle märksõnad, reklaamitekstid ja maandumisleht.</p>
<h2>Tüüpilised vead</h2>
<ul>
<li>Konversioone ei mõõdeta või mõõdetakse lehe avamist, mitte päringut.</li>
<li>Reklaam viib avalehele, mitte otsingule vastavale lehele.</li>
<li>Asukoha seadistus näitab reklaami ka väljaspool teeninduspiirkonda.</li>
<li>Negatiivseid märksõnu pole ja eelarve kulub kõrvalistele otsingutele.</li>
<li>Kampaaniat muudetakse iga päev, enne kui andmeid on piisavalt.</li>
<li>Reklaamikonto on agentuuri nimel ja koostöö lõppedes kaob ajalugu.</li>
</ul>
<p>Meie loome kontod alati kliendi nimele. Kampaania seadistus maksab alates €599, reklaam koos sotsiaalmeedia haldusega €1,399 kuus. Vaata lähemalt lehte <a href="/et/google-ads-reklaam.html">Google Ads reklaam</a> või hinnad lehel <a href="/et/hinnad.html">hinnad</a>.</p>""",
        "faq": [
            ("Kui suur peaks olema väikeettevõtte Google Adsi eelarve?", "Kohalike kampaaniate puhul soovitame vähemalt €500-1,000 kuus reklaamikuluks. Haldustasu on eraldi. Väiksema eelarvega kogub kampaania andmeid liiga aeglaselt."),
            ("Kas alustada otsingureklaami või Performance Maxiga?", "Väikeettevõttele on otsingureklaam tavaliselt parem algus, sest kontroll märksõnade üle on suurem. Performance Max sobib siis, kui konversioonide mõõtmine töötab ja andmeid on piisavalt."),
            ("Kelle nimele reklaamikonto luuakse?", "Meie loome Google Adsi ja Analyticsi kontod alati kliendi nimele, nii et kampaaniate ajalugu ja andmed jäävad sulle ka koostöö lõppedes."),
        ],
        "services": ["ads", "web"],
    },
    "redesign-without-seo-loss": {
        "slug": "kodulehe-uuendamine-ilma-seo-kaotuseta.html",
        "title": "Kodulehe uuendamine ilma SEO kaotuseta | BoostLab",
        "desc": "Kodulehe uuendamine ilma Google'i positsioone kaotamata: URL-ide inventuur, 301-ümbersuunamised, sisu ja metaandmed, hreflang ning kontroll pärast avamist.",
        "h1": "Kodulehe uuendamine ilma SEO kaotuseta",
        "lead": "Uus disain ei tohi maksta Google'i positsioone. Siin on samm-sammuline plaan, mida järgime iga kodulehe ümbertegemisel, ja kontrollnimekiri pärast avamist.",
        "date": "5. november 2026", "iso": "2026-11-05", "minutes": 7,
        "body": """<p>Kõige tavalisem lugu: ettevõte teeb uue ja ilusa kodulehe ning paari nädala pärast langeb päringute arv. Põhjus pole tavaliselt disainis, vaid selles, et vanad aadressid kadusid, hästi järjestuv sisu kustutati ja Google pidi lehte otsast peale tundma õppima. Kodulehe uuendamine ilma SEO kaotuseta on täiesti võimalik, kui töö tehakse õiges järjekorras.</p>
<h2>1. URL-ide inventuur</h2>
<p>Enne kui uus struktuur paika pannakse, kogu kokku kõik vana lehe aadressid. Allikad:</p>
<ul>
<li>vana lehe sitemap ja lehe roomamine SEO-tööriistaga;</li>
<li>Search Console'i tulemuste aruanne, kus on näha, millised lehed saavad näitamisi ja klikke;</li>
<li>Google Analytics 4, kust näed, millised lehed toovad külastusi ja päringuid;</li>
<li>välislinkide nimekiri, sest teistelt saitidelt tulevad lingid on väärtus, mida ei tohi kaotada.</li>
</ul>
<p>Märgi tabelis iga URL-i juurde klikid, näitamised ja konversioonid. Nii on selge, millised lehed on kriitilised.</p>
<h2>2. 301-ümbersuunamiste kaart</h2>
<p>Iga vana URL peab viima kõige sobivamale uuele lehele püsiva 301-ümbersuunamisega. Mitte avalehele ja mitte 404-lehele. Kui teenus "katuse remont" liigub aadressilt /teenused/katus aadressile /katuse-remont.html, peab ümbersuunamine olema just nende kahe vahel. Väldi ümbersuunamiste ahelaid, kus A viib B-le ja B viib C-le. Iga vana aadress peab viima otse lõppsihtkohta.</p>
<p>Kui URL saab jääda samaks, jäta see samaks. Kõige turvalisem ümbersuunamine on see, mida pole vaja.</p>
<h2>3. Säilita sisu, mis järjestub</h2>
<p>Lehed, mis toovad Google'ist liiklust, on seda teinud oma sisu tõttu. Kui uus disain lühendab teksti kolmeks lauseks, kaob ka põhjus, miks Google lehte näitas. Säilita hästi järjestuvate lehtede põhisisu, alapealkirjad ja KKK-d. Tekst võib olla parem ja paremini struktureeritud, kuid teema ja vastused peavad alles jääma. Kui kaks vana lehte liidetakse üheks, peab uus leht katma mõlema teema.</p>
<h2>4. Metaandmed ja struktuur</h2>
<ul>
<li>Too üle title ja meta description, mis töötavad. Muuda neid teadlikult, mitte malli tõttu.</li>
<li>Kontrolli, et igal lehel oleks üks H1 ja loogiline alapealkirjade struktuur.</li>
<li>Canonical peab viitama uuele aadressile, mitte arenduskeskkonnale.</li>
<li>Schema-märgendus, näiteks Organization, Service, FAQPage ja BreadcrumbList, tuleb uuel lehel uuesti seadistada.</li>
<li>Siselingid peavad viitama uutele aadressidele otse, mitte ümbersuunamiste kaudu.</li>
</ul>
<h2>5. Mitmekeelne leht ja hreflang</h2>
<p>Eestis on kodulehed sageli eesti, inglise ja vene keeles. Iga keeleversioon vajab oma ümbersuunamisi ja hreflangi märgendeid, mis viitavad üksteisele vastastikku. Kui vana leht kasutas keele jaoks parameetrit ja uus kasutab kausta, näiteks /et/ ja /en/, tuleb kaardistada iga keele iga URL. Vale hreflang võib tähendada, et venekeelne leht ilmub eestikeelses otsingus või vastupidi.</p>
<h2>6. Kiirus</h2>
<p>Uus leht peab olema vähemalt sama kiire kui vana, eelistatult kiirem. Mõõda vana lehe Core Web Vitals enne ja võrdle pärast. Suured pildid, uued animatsioonid ja kolmanda osapoole skriptid on tavalised põhjused, miks ilus uus leht on telefonis aeglasem.</p>
<h2>Mida mitte teha</h2>
<ul>
<li>Ära muuda korraga disaini, domeeni, URL-e ja sisu, kui seda saab vältida. Mida vähem muutujaid, seda lihtsam on probleemi leida.</li>
<li>Ära kustuta vanu blogipostitusi ainult sellepärast, et need on vanad. Kui need toovad liiklust, uuenda neid.</li>
<li>Ära suuna kõiki vanu aadresse avalehele. Google käsitleb seda sageli nagu 404-lehte.</li>
<li>Ära ava uut lehte reede õhtul ega enne puhkust. Esimesed päevad vajavad kedagi, kes jälgib vigu.</li>
</ul>
<h2>7. Avamise päev</h2>
<ol>
<li>Eemalda arenduskeskkonna noindex ja kontrolli robots.txt-i.</li>
<li>Lülita sisse ümbersuunamised ja testi need nimekirja põhjal läbi.</li>
<li>Esita uus sitemap Search Console'is.</li>
<li>Kontrolli, et GA4 ja konversioonid töötavad ning vormid saadavad kirju.</li>
</ol>
<p>Hoia vana lehe koopia ja URL-ide tabel alles vähemalt mõneks kuuks. Kui mõni leht kaotab nähtavust, saad võrrelda, mis täpselt muutus: tekst, pealkiri, siselingid või aadress. Ilma võrdlusmaterjalita on põhjust palju raskem leida.</p>
<h2>Kontrollnimekiri pärast avamist</h2>
<table><thead><tr><th>Millal</th><th>Mida kontrollida</th></tr></thead><tbody>
<tr><td>Avamise päev</td><td>Ümbersuunamised, noindex, robots.txt, sitemap, vormid, analüütika</td></tr>
<tr><td>1. nädal</td><td>Search Console'i indekseerimise ja 404-vigade aruanne, URL-i kontroll olulistele lehtedele</td></tr>
<tr><td>2.-4. nädal</td><td>Näitamiste ja klikkide võrdlus vana perioodiga, kriitiliste lehtede positsioonid</td></tr>
<tr><td>2. kuu</td><td>Konversioonide võrdlus, vead, mis ilmusid hiljem, siselinkide parandused</td></tr>
<tr><td>3. kuu</td><td>Kokkuvõte, millised lehed kasvasid ja millised vajavad sisu parandamist</td></tr>
</tbody></table>
<p>Väike kõikumine esimestel nädalatel on normaalne, sest Google töötleb uusi aadresse. Kui kriitiline leht kaotab nähtavust ka mõne nädala pärast, kontrolli kõigepealt ümbersuunamist, sisu ja canonicalit.</p>
<h2>Kokkuvõte</h2>
<p>Kodulehe uuendamine ilma SEO kaotuseta tähendab kolme asja: tea, mis vanal lehel töötab, suuna iga vana aadress õigesse kohta ja jälgi tulemusi pärast avamist. Meie projektides on URL-ide kaardistus ja ümbersuunamised osa tööst, mitte lisateenus. Ettevõtte koduleht maksab alates €1,700 ja valmib 2-3 nädalaga. Vaata lehte <a href="/et/kodulehe-tegemine.html">kodulehe tegemine</a> ja üldisemat nimekirja artiklis <a href="/et/blog/seo-kontrollnimekiri-enne-avamist.html">SEO kontrollnimekiri enne avamist</a>.</p>""",
        "faq": [
            ("Kas uus koduleht kaotab Google'i positsioonid?", "Ei pea kaotama. Kui vanad URL-id kaardistatakse, seadistatakse 301-ümbersuunamised ja hästi järjestuv sisu säilitatakse, jäävad positsioonid enamasti alles. Väike kõikumine esimestel nädalatel on normaalne."),
            ("Kui kaua peavad 301-ümbersuunamised kehtima?", "Soovitame jätta need püsivalt alles, eriti aadressidele, millele on välislinke. Ümbersuunamise kustutamine toob vana lingi 404-lehele."),
            ("Kas ümbersuunamised on kodulehe hinna sees?", "Jah. Meie projektides on URL-ide kaardistus, 301-ümbersuunamised, hreflang ja Search Console'i kontroll uue kodulehe töö osa."),
        ],
        "services": ["web"],
    },
})
