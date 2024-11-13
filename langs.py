from dataclasses import dataclass

@dataclass
class Language:
    text: str
    language: str


languages = [
    # Language(text='1', language='1'),
    # Language(text='2', language='2'),
    # Language(text='3', language='3'),
    # Language(text='4', language='4'),
    Language(text="Në një fshat të vogël buzë një liqeni të kthjellët, jetonte një burrë i moshuar me emrin Ilir. Ai kishte kaluar tërë jetën e tij në atë vend të qetë dhe të largët, ku njerëzit jetonin në harmoni me natyrën. Çdo mëngjes, Iliri zgjohej herët dhe shkonte në liqen për të peshkuar. Me rrjetën e tij të vjetër, ai nxirrte peshq të freskët për vaktet e tij të përditshme. Në ditë me diell, ai ulej nën hijen e pemës së vjetër të ullirit dhe lexonte libra të vjetër, të cilat i kishte mbledhur gjatë viteve. Një ditë, ndërsa peshkonte, ai pa diçka të çuditshme në thellësi të ujit. Një shkëlqim i fortë vinte nga fundi i liqenit. Kur u zhyt për të parë më mirë, gjeti një gur të rrallë, që shkëlqente me një dritë të jashtëzakonshme. I habitur, ai e mori gurin dhe u kthye në shtëpi. Nga ajo ditë, fshati filloi të përjetonte ndryshime të çuditshme. Toka u bë më pjellore, pemët nisën të japin fruta më të bollshme dhe njerëzit ndiheshin më të lumtur. Por lajmi për gurin magjik u përhap shpejt dhe njerëz nga qytetet e afërta filluan të vinin në fshat, duke kërkuar misterin e gurit të Ilirit. Ai e dinte se guri kishte fuqi të veçanta, por e ruante sekretin e tij me kujdes. Një ditë, një i ri nga qyteti, i quajtur Arber, u paraqit tek ai dhe i kërkoi ndihmë. Iliri, duke parë sinqeritetin në sytë e tij, vendosi t’i tregonte vendndodhjen e gurit. Ata të dy shkuan në liqen dhe Arberi, i shtyrë nga lakmia, tentoi të merrte gurin për veten e tij. Por, në momentin që e preku gurin, një dritë verbuese shpërtheu dhe ai u zhduk pa gjurmë. Iliri kuptoi se fuqia e gurit nuk duhej të përdorej për interesa vetjake dhe vendosi ta kthente përsëri në thellësitë e liqenit. Fshati, që kishte përjetuar begatinë për një kohë të shkurtër, u kthye në jetën e tij të zakonshme, por njerëzit mbetën mirënjohës për mësimin e marrë: që lumturia e vërtetë vjen nga gjërat e thjeshta dhe jo nga kërkimi i pushtetit apo pasurisë.", language="Albanian"),
    Language(text="Qədim bir şəhərdə, Qafqaz dağlarının ətəyində, bir gənc oğlan yaşayırdı. Onun adı Əli idi və o, öz ailəsi ilə birlikdə kiçik bir kənddə məskunlaşmışdı. Əlinin ən böyük arzusu dünya səyahətinə çıxmaq və uzaq diyarlarda macəralar yaşamaq idi. Amma kasıb bir ailədən gəldiyi üçün bu arzusunu reallaşdırmaq onun üçün çox çətin görünürdü. Hər gün səhər tezdən o, kəndin yaxınlığında yerləşən taxıl tarlalarına gedirdi və günəş batana qədər işləyirdi. Bir gün, Əli təsadüfən kəndin kənarındakı köhnə bir mağarada gizlənmiş qədim bir xəzinə xəritəsi tapdı. Bu xəritədə uzaq bir adada böyük bir xəzinə olduğu qeyd olunmuşdu. Əli xəritəni götürdü və uzun bir səyahətə çıxmağa qərar verdi. O, öz qəsəbəsindəki dostlarından kömək istədi və beş nəfərlik bir qrup yığdı. Onlar birlikdə səyahətə başladılar. Yolları çox çətin idi. Onlar qalın meşələrdən, təhlükəli dağ keçidlərindən keçdilər və sonunda böyük bir dənizin sahilinə çatdılar. Əlinin qrupu köhnə bir qayıq tapdı və onunla dənizdə üzdülər. Günlər və gecələr boyu onlar dənizdə üzdülər. Sular sakit olanda hər şey yaxşı idi, amma tez-tez güclü fırtınalar onlara mane olurdu. Bir dəfə onların qayıqları böyük bir dalğa ilə aşdı, amma xoşbəxtlikdən heç kim ciddi zədə almadı. Nəhayət, onlar xəritədə göstərilən adaya çatdılar. Ada çox sirli və təhlükəli görünürdü. Əli və onun dostları adada müxtəlif tələlərdən qaçmalı və müxtəlif bulmacaları həll etməli idilər. Günlərlə adada gəzdikdən sonra onlar nəhayət xəzinənin yerini tapdılar. Amma xəzinəni götürmək istəyəndə, qədim bir qoruyucu peyda oldu və onlara xəbərdarlıq etdi ki, bu xəzinəni yalnız səmimi niyyətlərlə götürmək olar. Əli ürəyindəki dürüstlük və dostlarına olan sevgisi ilə xəzinəni götürdü və kəndinə qayıtdı. Onlar kəndə qayıtdıqdan sonra, Əli tapdığı xəzinəni kəndin inkişafına sərf etdi. Onun bu yaxşı əməlləri nəticəsində kəndin hər bir sakini rifaha qovuşdu və Əlinin adı nəsillər boyu xatırlandı.", language="Azeri"),
    Language(text="U srcu Balkana, u malom selu skrivenom među brdima, živjela je starica po imenu Mara. Bila je poznata po svojoj mudrosti i velikom srcu, a ljudi iz svih okolnih sela dolazili su kod nje po savjet. Svakog jutra, Mara bi ustajala rano, pravila svoju jutarnju kafu i sjedila na staroj drvenoj klupi ispred svoje kuće. Gledala bi kako sunce izlazi iza planina i osluškivala cvrkut ptica. Život je bio miran i jednostavan, ali ispunjen toplinom. Jednog dana, u selo je stigao stranac. Bio je to mladić po imenu Ivan, koji je tražio utočište jer je bio putnik na dugom putovanju. Selo ga je srdačno primilo, ali Mara je primijetila da nešto nije u redu. Mladić je često bio zamišljen i provodio sate šetajući oko sela, gledajući u daljinu. Jednog dana, Mara ga je pozvala na čaj i upitala ga o njegovim brigama. Ivan je priznao da je izgubio put do svog doma i da je tražio način da se vrati, ali bezuspješno. Bio je rastrgan između želje da pronađe svoje korijene i straha da će zauvijek ostati izgubljen. Mara je pažljivo slušala i nakon što je završio svoju priču, rekla mu je: Ponekad, da bi pronašao ono što tražiš, moraš najprije pronaći mir u svom srcu. Te riječi su duboko pogodile Ivana. Počeo je provoditi više vremena s ljudima iz sela, pomagati im u poljskim poslovima i sudjelovati u zajedničkim proslavama. Kako su mjeseci prolazili, Ivan je shvatio da je našao novi dom među tim ljudima. Nije više osjećao tugu niti izgubljenost. Jednog jutra, dok je sunce izlazilo, Ivan je došao do Marine kuće i rekao: Našao sam svoj put, iako nije onaj koji sam tražio. Mara se nasmiješila i rekla mu da je sreća često skrivena tamo gdje je najmanje očekujemo. Ivan je ostao u selu, zasnovao porodicu i živio dug i sretan život. Selo ga je prihvatilo kao jednog od svojih, a njegova priča je ostala kao pouka da put do sreće nije uvijek pravocrtan, ali uvijek vrijedan truda.    ", language="Bosnian"),
    Language(text="En un petit poble de la costa catalana, vivia una dona anomenada Marta. Cada matí, es llevava amb el cant dels ocells i passejava pel mercat local, on comprava fruites fresques i verdures per al seu petit restaurant. Marta era coneguda per la seva cuina exquisida, especialment pel seu famós arròs negre amb sèpia. Els habitants i visitants feien cua per tastar els seus plats. Un dia, mentre passejava per la platja, va trobar una ampolla amb un missatge dins. La carta explicava una història d'amor perdut entre dos amants que havien promès retrobar-se en aquell mateix lloc molts anys enrere. Intrigada, Marta va decidir investigar la història, parlant amb els vilatans més grans per descobrir si la llegenda era real. Amb el pas del temps, es va adonar que la història era molt més complexa del que semblava i va acabar unint famílies que no es parlaven des de feia dècades. La seva recerca no només va resoldre un antic misteri, sinó que també va portar una nova vida al poble, convertint-lo en un lloc turístic famós per la seva rica història i els seus plats deliciosos.", language="Catalan"),
    Language(text="U jednom malom dalmatinskom selu, živio je čovjek po imenu Marko. Bio je ribar cijeli svoj život, odlazio bi rano ujutro na more, a vraćao se u sumrak s mrežama punim ribe. Njegova obitelj je generacijama živjela od mora, i svi su ga u selu poštovali zbog njegove skromnosti i marljivosti. Jednog dana, dok je pecao, naišao je na nevjerojatno otkriće - staru škrinju prekrivenu školjkama. Kada ju je otvorio, pronašao je zlatne novčiće i dragulje. Umjesto da zadrži blago za sebe, Marko je odlučio podijeliti svoje bogatstvo s cijelim selom. Zahvaljujući njemu, selo je obnovilo svoju crkvu, škole i bolnice. No, najvredniji dio priče bio je Markov primjer nesebičnosti, koji je ujedinio cijelu zajednicu. Od tog dana, svi su ga zvali Marko Velikodušni, a selo je postalo simbol zajedništva i solidarnosti.", language="Croatian"),
    Language(text="V malém městečku uprostřed Čech žila dívka jménem Anna. Každé ráno chodila do lesa sbírat houby a bylinky, které poté sušila a používala na přípravu léčivých čajů. Byla známá po celém kraji jako bylinkářka, která dokázala vyléčit téměř jakoukoli nemoc. Jednoho dne přišla do její chaloupky neznámá žena, která hledala pomoc pro svého nemocného syna. Anna připravila speciální směs z bylin, kterou dávala chlapci pít každý den. Po týdnu se zázračně uzdravil. Zpráva o Annině schopnosti se rychle rozšířila a lidé z daleka přicházeli, aby ji požádali o radu. Avšak, Anna nikdy nežádala peníze za své léčení, věřila, že její dar je tu pro všechny. Její skromnost a štědrost jí přinesly respekt a uznání nejen od místních obyvatel, ale i od cizinců, kteří za ní putovali dlouhé kilometry.", language="Czech"),
    Language(text="I en lille by i det sydlige Danmark boede en ældre mand ved navn Hans. Hver dag cyklede han til havnen, hvor han ejede en lille fiskerbåd. Hans far havde lært ham at fiske, og han havde gjort det hele sit liv. Fiskeriet var ikke kun en levevej for ham, men også en passion. En dag, mens han var ude på havet, stødte han på en lille sæl, der var blevet fanget i et fiskenet. Uden at tøve sprang Hans i vandet for at befri den. Efter at sælen var reddet, begyndte den at følge ham hver dag, når han sejlede ud. Byens børn elskede at komme ned til havnen for at se Hans og hans nye ven. Historien om Hans og sælen spredte sig hurtigt, og snart begyndte turister at strømme til byen for at se det usædvanlige venskab. Hans blev en lokal helt, men for ham var det blot endnu en dag på havet.", language="Danish"), 
    Language(text="In een klein dorpje in Nederland woonde een vrouw genaamd Sophie. Ze was bekend om haar prachtige bloemenwinkel, waar ze elke ochtend verse bloemen uit haar tuin bracht. Sophie had een talent voor het maken van boeketten, en mensen kwamen van heinde en verre om haar creaties te kopen. Op een dag kreeg ze een mysterieuze bestelling van een anonieme afzender, met de vraag om een speciaal boeket te maken voor een geliefde. Ze besloot haar creativiteit te laten spreken en maakte het mooiste boeket dat ze ooit had samengesteld, vol met rozen, tulpen en lelies. Toen ze het boeket afleverde, ontdekte ze dat het bestemd was voor een bruid die haar trouwdag wilde vieren. De bruid was zo ontroerd door het prachtige boeket dat ze Sophie uitnodigde voor de ceremonie. Vanaf die dag werd Sophie de favoriete bloemist` voor bruiloften en feesten in de regio.", language="Dutch"), 
    Language(text="Väikeses Eesti linnas, keset rohelisi metsi ja siniseid järvi, elas noor mees nimega Jaanus. Ta oli tuntud oma oskuste poolest puidutöös ning tema käsitöö oli kuulus üle kogu maakonna. Jaanus veetis oma päevad metsas, valides hoolikalt parimad puud, millest teha laudu, toole ja kaste. Ühel päeval leidis ta vana puutüki, mille sees oli peidus midagi erilist. Kui ta hakkas puitu töötlema, avastas ta puidu sees peidetud vanad nikerdused, mis jutustasid loo iidsetest aegadest. Pärast selle avastamist otsustas Jaanus luua terve mööblikollektsiooni, mis põhineb vanadel Eesti legendidel ja mustritel. Tema tööd äratasid tähelepanu ja peagi kutsuti teda esinema suurtele messidele nii Eestis kui ka välismaal. Jaanuse unistus oli alati olnud oma töökoja avamine, ja tänu tema leidlikkusele sai ta lõpuks oma unistu`se täide viia.", language="Estonian"),
    Language(text="Suomen Lapissa, kaukana pohjoisesta, asui nainen nimeltä Leena. Hän eli yksinkertaista elämää vanhassa mökissä keskellä laajaa metsää. Talvisin lumi peitti kaiken valkoiseen vaippaan, ja ainoat äänet olivat tuulen humina ja jään ritinä järven pinnalla. Leena oli erakkoluonteinen ja nautti rauhasta, mutta eräänä päivänä hänen elämänsä muuttui, kun metsästä löytyi eksynyt husky-koira. Leena otti koiran mukaansa, antoi sille ruokaa ja lämpöä. Vähitellen heistä tuli erottamattomat kumppanit. Koira auttoi Leenaa metsästyksessä ja seurasi häntä pitkillä hiihtoretkillä. Eräänä iltana, kun revontulet tanssivat taivaalla, Leena huomasi koiran käyttäytyvän oudosti. Se juoksi järvelle ja haukkui kovaan ääneen. Kun Leena seurasi koiraa, hän huomasi jäässä pienen halkeaman. Hän tiesi, että seuraava kylmä yö voisi rikkoa jään kokonaan. Kiitos koiran varoituksen, Leena pelastui vaarasta. Tämän jälkeen hän alkoi uskoa, että koira oli hänen suojelusenkelinsä, lähetetty turvaamaan hänen yksinäistä elämäänsä pohjoisen erämaassa.", language="Finnish"),
    Language(text="Dans un petit village provençal, vivait un homme nommé Pierre. Il possédait une petite ferme où il cultivait des herbes aromatiques comme le thym, le romarin et la lavande. Chaque matin, il se levait avant l’aube pour récolter les plantes lorsqu’elles étaient encore couvertes de rosée. Pierre était connu pour ses talents de guérisseur, préparant des tisanes et des onguents pour les villageois. Un jour, une épidémie frappa le village, et de nombreuses personnes tombèrent malades. Pierre travailla sans relâche, cherchant des remèdes naturels pour soulager ses voisins. Il passa des nuits à expérimenter avec différentes herbes, jusqu’à ce qu’il découvre une combinaison qui aidait à apaiser la fièvre. Sa renommée se répandit dans toute la région, attirant même des visiteurs des villages voisins. Cependant, Pierre restait humble, refusant de prendre crédit pour ce qu’il considérait comme un simple devoir. En fin de compte, grâce à ses efforts inlassables, le village survécut à la crise, et Pierre devint une légende vivante, un symbole de dévouement et de compassion.", language="French"),
    Language(text="In einem kleinen Dorf im Schwarzwald lebte ein alter Mann namens Heinrich. Jeden Morgen spazierte er durch den Wald, sammelte Pilze und Beeren, die er später auf dem Markt verkaufte. Heinrich war bekannt für seine Geschichten über den Wald und die Geheimnisse, die er verbarg. Eines Tages, während er tief im Wald war, entdeckte er eine versteckte Höhle, die er zuvor noch nie gesehen hatte. Neugierig ging er hinein und fand dort alte Wandmalereien, die die Geschichte eines längst vergessenen Stammes erzählten. Diese Entdeckung sorgte für Aufsehen in der Region, und bald strömten Historiker und Forscher herbei, um die Höhle zu untersuchen. Heinrich genoss die Aufmerksamkeit, aber er blieb bescheiden und erzählte jedem, dass der wahre Schatz nicht die Höhle war, sondern der Wald selbst, der immer wieder neue Wunder enthüllte. Mit der Zeit wurde das Dorf zu einem beliebten Ziel für Wanderer und Abenteurer, die hofften, selbst ein Stück der verborgenen Geschichte zu entdecken.", language="German"),
    Language(text="Az Alföld szívében, egy kis magyar faluban élt egy idős asszony, akit mindenki csak Rózsika néninek hívott. Egész életét a földművelésnek szentelte, és híres volt a környéken termesztett paprikájáról, amit a legfinomabb pörköltekhez használtak. Minden tavasszal Rózsika néni saját kezűleg ültette el a paprika magjait, gondosan ügyelve arra, hogy a növények elég napfényt és vizet kapjanak. Egy nap, amikor a termést szüretelte, egy különleges növényt talált, ami sokkal nagyobb és vörösebb volt, mint a többi. Ebből a paprikából készített egy új receptet, amit hamarosan az egész falu meg akart kóstolni. Híre gyorsan elterjedt, és hamarosan még a közeli városokból is érkeztek emberek, hogy megízleljék a híres pörköltet. Rózsika néni története inspirációt adott mindenkinek, hogy ne féljenek új dolgokat kipróbálni és mindig büszkék legyenek arra, amit a saját kezükkel teremtettek.", language="Hungarian"),
    Language(text="Í fallegum þorpum á Íslandi, þar sem fjöllin og jöklar teygja sig í himininn, bjó maður að nafni Jón. Hann hafði alist upp á bænum sínum, þar sem hann hafði alltaf haft ástríðu fyrir náttúrunni og hinu íslenska landslagi. Jón var þekktur fyrir að vera viðskiptamaður í að selja fjölbreytta íslenska vöru og vörur sem hann sjálfur framleiddi frá jörðinni og sjávargróðri. Hann var oft úti á fjöllum að safna fjallamellum og fjólublómum, sem hann nýtti til að búa til einstakar græjur og útskurði. Jón var staðfastur og nýtti þann tíma sem hann var á bænum til að njóta þessarar rósemi og einveru. Einhverjum vetri fann hann sig í miklum veikindum og þurfti að fara til læknis. Þar var honum úthlutað sérstökum ávísunum og hann byrjaði að nota náttúrulegar lækningar sem hann hafði áður lært frá fornu lagi. Meðan hann tók þessa meðferðir byrjaði hann að upplifa mikla útlit. En síðustu daga þegar honum líður best og landið fylgdi honum betur fyrr, sótti hann nýjan stuðning og féll í marga góðra tíma.", language="Icelandic"),
    Language(text="In una piccola città nel sud Italia, dove il sole baciava dolcemente le spiagge sabbiose e l’odore del mare si mescolava con quello delle piante aromatiche, viveva un uomo di nome Marco. Marco aveva un piccolo vigneto che tramandava di generazione in generazione e il suo vino era famoso in tutta la regione. Ogni giorno, al mattino presto, Marco si svegliava con il canto degli uccelli e andava nei suoi campi a prendersi cura delle viti. Era un lavoro duro, ma che amava con tutto il cuore. Ogni grappolo d’uva che raccoglieva era una piccola opera d’arte, e ogni bottiglia di vino che produceva era un pezzo della sua anima. Un giorno, durante la vendemmia, incontrò una giovane donna di nome Sofia, che era venuta da Roma per conoscere le tradizioni vinicole della regione. Marco la prese sotto la sua ala e le insegnò tutto ciò che sapeva sulla vinificazione. Con il tempo, i due si innamorarono e iniziarono a lavorare insieme nei vigneti. Grazie alla loro dedizione e al duro lavoro, il vino di Marco divenne ancora più famoso, attirando visitatori da ogni angolo del mondo. La loro storia d’amore e la passione per il vino divennero leggendarie e il vigneto di Marco divenne un simbolo di tradizione e amore eterno.", language="Italian"),
    Language(text="Latvijā, tālajā vidienē, bija neliels ciemats, kur dzīvoja vecāka gadagājuma vīrs vārdā Jānis. Viņš bija dzimis un audzis šajā ciematā un visu mūžu bija strādājis par zemeņu audzētāju. Viņš bija labi pazīstams savā apkārtnē ar savām garšīgajām, saldajām zemenēm, ko audzēja savā mazajā dārzā. Viņš katru pavasari rūpīgi stādīja zemenes un rūpējās par tām, lai tās būtu vislabākās, ko varētu piedāvāt. Kad zemenes bija gatavas ražai, viņš ar prieku tās veda uz vietējo tirgu, kur tās vienmēr tika pirktas ātri. Taču Jānis vienmēr bija pazemīgs un nekad nevēlējās lielīties ar savu veiksmīgo biznesu. Viņš uzskatīja, ka daba ir tā, kas viņam dod iespēju dzīvot un dot citiem. Viss mainījās, kad kādu ziemu ciematā iestājās liela snigšana un ledus. Zemeņu dārziem nebija iespējams iegūt pietiekamu ūdeni, un Jānis bija spiests meklēt risinājumu, lai saglabātu ražu. Ar draudzīgu palīdzību no kaimiņiem viņš izdomāja metodi, kas palīdzēja saglabāt zemenes pat visaukstākajās ziemās. Šī atklājuma dēļ Jānis kļuva slavens visā reģionā un viņa dārzi kļuva par īstu ciemata lepnumu.", language="Latvian"),
    Language(text="Lietuvos šiaurėje, netoli didžiojo miško, gyveno vyras vardu Tomas. Tomas buvo garsus dėl savo darbų kalvystėje, kurią pradėjo dirbti dar būdamas jaunas. Jo įrankiai ir skulptūros buvo labai vertinami visoje šalyje, o žmonės ateidavo iš tolimiausių kampelių, kad įsigytų jo kūrinių. Tomas mėgo dirbti su metalais, ypač su geležimi, nes tai buvo medžiaga, kurią jis galėjo formuoti į įvairias formas. Jo darbai nebuvo tik įrankiai, bet menai, kurie pasakojo istorijas ir išreiškė jo pačio gyvenimo filosofiją. Vieną dieną jis nusprendė sukurti didelį paminklą miestui, kuris atspindėtų Lietuvos istoriją ir jos didingumą. Jis praleido daug mėnesių dirbdamas prie šio paminklo, kruopščiai pjaustydamas ir lygindamas metalus. Galų gale paminklas buvo baigtas ir pastatytas miesto aikštėje. Tai tapo simboliu, ne tik vietiniams, bet ir atvykusiems turistams, kurie atvyko pasigrožėti jo kūriniu ir išgirsti pasakojimus apie jo gyvenimą ir kovas. Tomas, nors ir tapęs žinomu menininku, niekada nepasididžiavo ir laikėsi paprastumo, nes manė, kad menas turi būti prieinamas visiems.", language="Lithuanian"),
    Language(text="F’dawn l-aktar żminijiet, meta n-natura kienet għadha tidher fl-ostinazzjoni tagħha, kien hemm raġel jismu Ġużeppi li kien jgħix f’raħal żgħir fil-Lvant ta’ Malta. Ġużeppi kien magħruf għall-passjoni tiegħu għall-ħajja ta’ barra, u spiss kien jivvjaġġa lejn il-kosti ta’ Malta, kemm għall-ħobżu u l-ħut, kif ukoll għas-sbuħija tas-sajf. Kien jara l-ħajja f’Malta bħala eżempju ta’ sempliċità u qima għan-natura. L-art li kienet għadek tidher kemm fuq l-għoljiet kif ukoll f’dawk il-pajjiżi għaddejjin minn qattagni u għomorha għalqet tistqarrja. Iżda l-akbar xogħol li Ġużeppi għamel kien il-ġid tiegħu fuq dan il-beraħ tal-għarġut minħabba l-ħarsa mill-qiegħ. Għall-aħħar minn kemm hemm, miet għalkemm għadha ħafna misterju kollha minn u quddiem spinta.", language="Maltese"),
    Language(text="U Crna Gora je zemlja s bogatom istorijom, iako u njoj žive ljudi različitih kultura i veroispovesti, svi su povezani dublje nego što misle. Jedan od najlepših delova ove zemlje je svakako njena obala, koja je poznata po svojim prelepim plažama i kristalno čistom moru. Svakog leta, turisti sa svih krajeva sveta dolaze da uživaju u suncu, moru i prirodi. Međutim, iako je turizam postao važan deo ekonomske slike, narod Crne Gore je uvek bio poznat po tome što je sačuvao svoje tradicije i običaje. Ljudi su gostoljubivi, iako sa posebnim ponosom prema svojoj istoriji i tradiciji. Oni veruju da je najlepši način života u skladu sa prirodom, i svakodnevno se trude da očuvaju lepotu svoje zemlje. Iako su se u poslednjim decenijama stvari promenile, mnogi i dalje veruju u snagu zajednice i međusobnu pomoć, nešto što je od davnina bilo od suštinskog značaja za opstanak u planinskim predelima ove zemlje.", language="Montenegrin"),
    Language(text="Norge er et land med majestetiske fjell, lange fjorder og et landskap som har formet livet til folket i flere tusen år. I de tidlige tider var det et hardt liv for de som bodde her, men samtidig hadde de en nær tilknytning til naturen og levde i harmoni med elementene. Fra vikingtiden og framover har Norge vært et land som har utviklet seg gjennom handel, oppdagelser og innovasjon. Samtidig har folk alltid hatt en sterk følelse av identitet knyttet til den norske kulturen og historien. Hjemme i bygdene, langs kysten og inne i fjordene, finner man gamle tradisjoner som fortsatt er levende i dag. Maten, musikken og språket har blitt videreført gjennom generasjonene, og mange nordmenn er stolte av sine røtter. I dag er Norge kjent for sin høye livskvalitet, velferdssystem og sterke økonomi. Men til tross for de moderne fremskrittene, forblir respekten for naturen og tradisjonene like viktig som før. Fjellene og fjordene, de urørte skogene og de pittoreske landsbyene er fortsatt et symbol på Norges sjel og identitet.", language="Norwegian"),
    Language(text="Polska, kraj o bogatej historii, kulturze i tradycjach, znajduje się w samym sercu Europy. Przez wieki Polacy walczyli o swoją niepodległość i tożsamość narodową, przechodząc przez trudne okresy, ale również przeżywając chwile triumfu i sukcesów. Polska jest krajem o różnorodnym krajobrazie, od malowniczych gór na południu po urokliwe wybrzeże Bałtyku na północy. W jej miastach spotkamy zarówno średniowieczne zamki, jak i nowoczesne budynki, które tworzą wyjątkową atmosferę łączącą przeszłość z teraźniejszością. Polacy są dumni ze swojej historii, a wiele tradycji, takich jak obchodzenie Świąt Bożego Narodzenia czy Wielkanocy, pozostaje żywą częścią kultury. Kuchnia polska, z takimi potrawami jak pierogi, bigos czy żurek, jest bogata w smaki, a każdy region ma swoje unikalne przepisy. Polacy są również bardzo gościnni i chętni do dzielenia się swoją kulturą i historią z turystami, którzy odwiedzają kraj z całego świata. Mimo wielu trudności, Polska pozostaje symbolem siły, determinacji i nadziei na przyszłość.", language="Polish"),    
    Language(text="Portugal é um país com uma história rica, uma cultura vibrante e uma paisagem diversificada que vai desde as montanhas do interior até às belas praias do Atlântico. A sua história remonta a séculos atrás, quando os primeiros navegadores portugueses exploraram os mares desconhecidos e estabeleceram rotas comerciais com diversas partes do mundo. O país é também famoso pela sua gastronomia, com pratos como o bacalhau, as sardinhas assadas e, claro, os deliciosos pastéis de nata. A língua portuguesa, falada por milhões de pessoas em todo o mundo, tem um papel importante na comunicação entre diferentes culturas e países. A música portuguesa, com destaque para o fado, é igualmente um dos pilares da sua cultura. Ao longo dos anos, Portugal tem procurado equilibrar a preservação da sua tradição com a modernização e o progresso económico. Hoje, o país é reconhecido pela sua qualidade de vida, a sua hospitalidade e o seu ambiente amigável. Além disso, as cidades como Lisboa, Porto e Coimbra são conhecidos por sua história e beleza, atraindo turistas de todo o mundo.", language="Portuguese"),
    Language(text="România este o țară situată în sud-estul Europei, cu o istorie și cultură impresionante. Cu munți spectaculoși, coline și o coastă frumoasă la Marea Neagră, România oferă un peisaj natural diversificat. Capitala țării, București, este un important centru cultural și economic, în timp ce orașe istorice precum Brașov, Cluj-Napoca și Sibiu sunt pline de farmec și tradiție. România este cunoscută pentru mitologia sa bogată, iar legenda Contelui Dracula, inspirată de figura istorică a voievodului Vlad Țepeș, este una dintre cele mai cunoscute povești din lume. De asemenea, tradițiile românești sunt păstrate cu mândrie, inclusiv dansurile populare, muzica folclorică și sărbătorile religioase. Mâncarea românească, cu preparate tradiționale precum sarmale, mici și ciorbă de burtă, este apreciată de localnici și turiști deopotrivă. În ciuda unor perioade dificile din trecut, România este astăzi o țară în plină dezvoltare, iar locuitorii săi sunt mândri de patrimoniul lor și de realizările lor.", language="Romanian"),
    Language(text="Srbija je zemlja koja se nalazi u jugoistočnoj Europi, a njena istorija je duboko ukorenjena u tradiciji, kulturi i borbi za slobodu. Beograd, glavni grad, je jedinstveno mesto koje spaja istorijske spomenike i moderni urbanizam. Kroz vekove, Srbija je bila deo različitih carstava, ali je uvek održavala svoj identitet i nezavisnost. Srpski narod je poznat po svojoj hrabrosti i upornosti, a mnoge borbe i pobede su postale deo kolektivne svesti. Srpska kuhinja je bogata i raznolika, sa jelima poput ćevapa, sarme i ajvara, dok muzika, posebno narodna, ima snažan uticaj na srpsku kulturu. Srbi su veoma gostoljubivi i ponosni na svoju tradiciju i običaje, koji su se prenosili sa generacije na generaciju. Danas, Srbija se suočava s izazovima modernizacije, ali istovremeno čuva svoj bogat kulturni i istorijski nasleđeni identitet.", language="Serbian"),
    Language(text="Slovensko je država u srednji Evropi, ki ima bogato zgodovino, čudovito naravo in prijazne prebivalce. Dežela je znana po svojih visokih Alpah, številnih jezerih in gozdovih, pa tudi po svojih zgodovinskih mestih, kot sta Ljubljana, glavno mesto, in Maribor. Slovenija je bila dolgo časa del Jugoslavije, vendar je leta 1991 postala neodvisna država. Slovenska kultura je zelo raznolika, saj se odraža v številnih tradicijah, glasbi in kulinariki. Slovenci so ponosni na svojo dediščino, še posebej na svojo naravno dediščino, saj je Slovenija znana po tem, da je ena izmed najbolj ekološko ozaveščenih držav v Evropi. Slovenska kuhinja je preprosta, vendar okusna, z jedmi, kot so potica, kranjska klobasa in različni siri. Slovenci so tudi zelo gostoljubni in vedno pripravljeni deliti svojo kulturo s tujci. Čeprav je Slovenija majhna, je zelo ponosna na svojo neodvisnost in svojo vlogo v mednarodnih odnosih.", language="Slovak"),
    Language(text="Slovenija je država, ki se ponaša z neverjetno naravno lepoto in bogato zgodovino. Nahaja se v osrčju Evrope, med Alpami in Jadranskim morjem, in ponuja izjemne možnosti za ljubitelje narave in zgodovine. Ljubljana, glavno mesto Slovenije, je polno zgodovinskih spomenikov, kulturnih prireditev in prijetnih kavarn, ki obiskovalce vabijo, da uživajo v mirnem vzdušju. Slovenija je znana po svojih alpskih gorah, kot so Triglav in Kamniško-Savinjske Alpe, ki nudijo številne možnosti za pohodništvo, smučanje in druge zimske športe. Poleg tega pa država ponuja tudi osupljiva jezera, kot je Blejsko jezero, ter jame, kot je Postojnska jama, ki so med najbolj obiskanimi turističnimi destinacijami. Slovenija je ena izmed najbolj ekoloških držav na svetu, saj je velika večina njenega ozemlja pokrita z gozdovi. Slovenci so ponosni na svojo tradicijo in kulturno dediščino, ki se kaže v številnih festivalih, ljudski glasbi in kulinaričnih posebnostih, kot so potica, idrijski žlikrofi in kranjska klobasa.", language="Slovenian"),
    Language(text="España es un país con una historia y cultura fascinantes, que abarca desde los antiguos romanos hasta la vibrante modernidad de sus ciudades hoy en día. Madrid, la capital, es un crisol de arte, gastronomía y vida nocturna, mientras que Barcelona, en la costa mediterránea, destaca por su arquitectura única y su vibrante escena artística. España también es conocida por su variada geografía, que incluye playas, montañas y llanuras, lo que le permite ofrecer una gran variedad de actividades al aire libre, desde el senderismo en los Pirineos hasta los deportes acuáticos en la Costa Brava. Además, la gastronomía española es una de las más celebradas del mundo, con platos emblemáticos como la paella, el jamón ibérico, las tapas y la tortilla española. Las festividades, como la Feria de Abril en Sevilla o la famosa corrida de toros en Pamplona, reflejan el espíritu alegre y festivo de la cultura española. Con una población diversa y una rica tradición de cine, música y danza, España sigue siendo un destino turístico de primer orden y un centro cultural global.", language="Spanish"),
    Language(text="Sverige är ett land beläget i norra Europa, känd för sin storslagna natur, sin rika historia och sina moderna städer. Landet är hem till några av världens mest imponerande landskap, inklusive de majestätiska fjällen i norr, de vidsträckta skogarna och de tusentals sjöarna. Stockholm, landets huvudstad, är en vacker stad som sträcker sig över flera öar och bjuder på en fascinerande blandning av historia och modernitet. Sverige är också känt för sitt höga levnadsstandard, sina framstående sociala system och sitt engagemang för jämlikhet. Svensk kultur är starkt präglad av öppenhet och hållbarhet, och landet är en ledare inom miljövänlig teknologi och innovation. Svenska mattraditioner inkluderar rätter som köttbullar, gravad lax och sill, och fika – en älskad paus för kaffe och sötsaker. Svenskarna är också kända för sin älskvärda mentalitet och vänlighet mot turister. Dessutom är det svenska språket en viktig del av landets kultur, och Sverige är hem till många internationella företag och artister.", language="Swedish"),
    Language(text="La Suisse, située au cœur de l’Europe, est un pays célèbre pour sa diversité culturelle, sa neutralité politique et ses paysages spectaculaires. Le pays est divisé en quatre régions linguistiques, chacune ayant sa propre identité et traditions. Les montagnes des Alpes suisses attirent des milliers de touristes chaque année, qu'ils viennent pour le ski, l'alpinisme ou simplement pour admirer la beauté naturelle. Les villes suisses, telles que Zurich, Genève et Berne, combinent l'architecture médiévale avec des infrastructures modernes. La Suisse est également connue pour sa cuisine, avec des spécialités comme le fromage fondu (fondue), le chocolat et les horloges de haute qualité. Le pays a une longue tradition d’impartialité dans les affaires internationales, et son rôle en tant que centre diplomatique mondial est bien respecté. L’une des caractéristiques les plus fascinantes de la Suisse est son système politique fédéral, qui permet à chaque canton de prendre des décisions importantes tout en restant uni sous un gouvernement central. Cette organisation politique unique contribue à la stabilité et à la prospérité du pays. Enfin, les Suisses sont réputés pour leur ponctualité, leur efficacité et leur respect des traditions.", language="Swiss"),
    Language(text="Türkiye, tarihi, kültürel zenginliği ve doğal güzellikleriyle dikkat çeken bir ülkedir. Batıda Avrupa ve doğuda Asya arasında yer alan Türkiye, hem coğrafi hem de kültürel olarak iki kıta arasında bir köprü işlevi görür. İstanbul, dünyanın en önemli kültürel ve ticari merkezlerinden biri olarak, tarihi dokusuyla modern yaşamı birleştirir. Türkiye'nin zengin mutfağı, döner, kebap, baklava gibi lezzetlerle tanınır ve her bölgesi kendine özgü yemek kültürlerine sahiptir. Kapadokya'nın peri bacaları, Pamukkale'nin beyaz travertenleri ve Efes antik kenti gibi doğal ve tarihi zenginlikler, Türkiye'nin turistler için cazibe merkezi olmasını sağlar. Ayrıca, Türk halkı misafirperverliği ve dostane tavırlarıyla ünlüdür. Ülke, yıllardır çeşitli sosyal, kültürel ve ekonomik değişimlerden geçse de geleneksel değerlerini ve kültürel mirasını korumaktadır.", language="Turkish"),
    Language(text="България е страна с дълга история и богато културно наследство. Разположена на Балканския полуостров, България е известна със своите древни исторически паметници, красиви природни пейзажи и традиции. София, столицата, е голям културен и икономически център, който съчетава модерните технологии с историята, която се простира хиляди години назад. В България могат да се видят множество старинни манастири, замъци и тракийски гробници, които свидетелстват за богатото минало на страната. Българската кухня е известна със своето разнообразие и вкус, като ястия като баница, кебапчета и кисело мляко са сред най-популярните. Музиката и танците също играят важна роля в българската култура, като фолклорните изпълнения са неразривно свързани с българските празници и тържества.", language="Bulgarian"),
    Language(text="Україна — це країна, що розташована в Східній Європі, з багатою історією, традиціями та культурною спадщиною. Київ, столиця України, є одним із найстаріших міст Європи, відоме своєю архітектурною спадщиною та величезними культурними пам'ятками. Природа України вражає своєю різноманітністю: від Карпатських гір до широких степів, від глибоких лісів до морських узбережжів. Культура України базується на багатих традиціях народного мистецтва, піснях, танцях і ремеслах. В Україні народилася одна з найпопулярніших у світі пісень — «Щедрик», яка стала відомою у всьому світі як Carol of the Bells. Українська кухня славиться своєю різноманітністю, і такі страви, як борщ, вареники та сало, стали символами української гостинності. Україна також відома своїм виноробством і стародавніми традиціями, які збереглися до сьогодні.", language="Ukrainian"),
    Language(text="Россия — страна, расположенная в Восточной Европе и Северной Азии, обладающая огромным историческим, культурным и природным наследием. Москва, столица России, является крупнейшим культурным и финансовым центром страны. В России расположены множество исторических памятников, музеев и театров, отражающих многовековую историю народа. Природа России разнообразна: от суровых северных территорий и вечной мерзлоты до теплых черноморских курортов и тайги. Русская литература и искусство известны на весь мир своими великими мастерами, такими как Пушкин, Толстой и Чехов. Русская кухня славится своими блюдами, такими как борщ, пельмени и блины. Россия также известна своим фольклором и традиционными праздниками, такими как Масленица и Новый год.", language="Russian"),
    Language(text="Η Ελλάδα είναι μια χώρα στην ανατολική Μεσόγειο με μια ιστορία που χάνεται στους αιώνες. Είναι γνωστή για τα αρχαία μνημεία της, την πολιτιστική της κληρονομιά και τη συνεισφορά της στη δυτική σκέψη και τέχνη. Η Αθήνα, η πρωτεύουσα, φιλοξενεί μερικά από τα πιο διάσημα αρχαιολογικά μνημεία του κόσμου, όπως ο Παρθενώνας και η Ακρόπολη. Η Ελλάδα έχει μια εξαιρετικά ποικιλόμορφη γεωγραφία, με τα νησιά του Αιγαίου και του Ιονίου να προσφέρουν πανέμορφες παραλίες, ενώ η ενδοχώρα είναι γεμάτη βουνά και ποτάμια. Η ελληνική κουλτούρα είναι γνωστή για τις τέχνες, τη φιλοσοφία και τις παραδόσεις της, με τη μουσική, το θέατρο και τον χορό να παίζουν σημαντικό ρόλο στην κοινωνία. Η ελληνική κουζίνα είναι διάσημη για τα υγιεινά και νόστιμα πιάτα της, όπως ο γύρος, η φασολάδα και η μπουγάτσα. Η Ελλάδα, με την πανέμορφη φύση της και την πλούσια πολιτιστική της κληρονομιά, αποτελεί έναν από τους πιο δημοφιλείς τουριστικούς προορισμούς στον κόσμο.", language="Greek")
]

