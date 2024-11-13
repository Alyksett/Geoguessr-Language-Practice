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
    Language(text="Dielli po perëndonte mbi horizont, duke pikturuar qiellin me nuanca të gjalla portokalli dhe rozë. Një fllad i lehtë mbartte aromën e luleve të freskëta, ndërsa tingujt e valëve që përplaseshin në breg mbushnin ajrin. Ishte një mbrëmje e përkryer, një që të bënte të vlerësoje gëzimet e thjeshta të jetës.", language="Albanian"),
    Language(text="Günəş üfüqdə batırdı, göyü parlaq narıncı və çəhrayı rənglərlə boyayırdı. Yumşaq bir külək təravətli çiçəklərin qoxusunu gətirir, sahilə çırpılan dalğaların səsi havanı doldururdu. Bu, həyatın sadə zövqlərini qiymətləndirməyə vadar edən mükəmməl bir axşam idi.", language="Azeri"),
    Language(text="Sunce je zalazilo na horizontu, bojajući nebo živopisnim nijansama narančaste i ružičaste boje. Blagi povjetarac nosio je miris svježeg cvijeća, a zvuk valova koji su udarali o obalu ispunjavao je zrak. Bila je to savršena večer koja te tjera da cijeniš jednostavne radosti života.", language="Bosnian"),
    Language(text="El sol es va pondre a l'horitzó, pintant el cel amb tons vius de taronja i rosa. Una brisa suau portava l'aroma de flors fresques, i el so de les onades trencant a la costa omplia l'aire. Era un vespre perfecte que et feia apreciar les alegries senzilles de la vida.", language="Catalan"),
    Language(text="Sunce je zalazilo iznad horizonta, bojajući nebo živim nijansama narančaste i ružičaste boje. Lagani povjetarac nosio je miris svježeg cvijeća, a zvuk valova koji su udarali o obalu ispunjavao je zrak. Bila je to savršena večer, jedna koja te tjera da cijeniš jednostavne užitke u životu.", language="Croatian"),
    Language(text="Slunce zapadalo nad obzorem a malovalo oblohu živými odstíny oranžové a růžové. Jemný vánek přinášel vůni čerstvých květin a zvuk vln narážejících na pobřeží naplňoval vzduch. Byl to dokonalý večer, který vás nutil ocenit jednoduché radosti života.", language="Czech"),
    Language(text="Solen var ved at gå ned over horisonten og malede himlen med levende nuancer af orange og pink. En let brise bar duften af friske blomster, og lyden af bølger, der slog mod kysten, fyldte luften. Det var en perfekt aften, en der fik dig til at værdsætte livets enkle glæder.", language="Danish"),
    Language(text="De zon ging onder aan de horizon en schilderde de lucht met levendige tinten oranje en roze. Een zachte bries droeg de geur van verse bloemen, en het geluid van golven die op de kust sloegen, vulde de lucht. Het was een perfecte avond die je deed waarderen wat het leven simpel maakt.", language="Dutch"),
    Language(text="Päike loojus silmapiiri taga, värvides taeva oranžide ja roosade toonidega. Õrn tuuleiil kandis endaga värskete õite lõhna ning rannikul purunevate lainete heli täitis õhku. See oli ideaalne õhtu, mis pani sind hindama elu lihtsaid rõõme.", language="Estonian"),
    Language(text="Aurinko oli laskemassa horisonttiin, maalaten taivaan elävillä oranssin ja vaaleanpunaisen sävyillä. Kevyt tuuli toi mukanaan tuoreiden kukkien tuoksun, ja aaltojen ääni, jotka löivät rantaan, täytti ilman. Se oli täydellinen ilta, joka sai sinut arvostamaan elämän yksinkertaisia iloja.", language="Finnish"),
    Language(text="Le soleil se couchait à l'horizon, peignant le ciel de nuances vibrantes d'orange et de rose. Une brise légère apportait le parfum des fleurs fraîches, et le son des vagues s'écrasant sur le rivage remplissait l'air. C'était une soirée parfaite, qui te faisait apprécier les joies simples de la vie.", language="French"),
    Language(text="Die Sonne ging am Horizont unter und malte den Himmel in lebhaften Orangetönen und Rosa. Eine sanfte Brise trug den Duft frischer Blüten, und das Rauschen der Wellen, die an die Küste schlugen, erfüllte die Luft. Es war ein perfekter Abend, der einen die einfachen Freuden des Lebens schätzen ließ.", language="German"),
    Language(text="Seqineq kangerlussuarmiilerpoq, qilammi qalipaatinik aappaluttunik amernik qalipillugu. Anorersuaq pualuinnaq tikkilissuaq naasut nutaat saqqaatipajaarai, imarlu qooqqussimasoq qorlutisaarpoq. Perlaatillugu unnuk kusanartoq inuunermi nuannersutut ilallugu.", language="Greenlandic"),
    Language(text="A nap lenyugodott a látóhatár fölött, narancssárga és rózsaszín árnyalatokkal festve az eget. Egy enyhe szellő hozta a friss virágok illatát, és a partot érő hullámok zaja betöltötte a levegőt. Ez egy tökéletes este volt, amely arra késztetett, hogy értékeld az élet egyszerű örömeit.", language="Hungarian"),
    Language(text="Sólin var að setjast við sjóndeildarhringinn og litaði himininn með lifandi tónum af appelsínugulum og bleikum. Mjúkur andvari bar ilm af ferskum blómum og bylgjuhljóðin sem skullu á ströndinni fylltu loftið. Þetta var fullkomið kvöld sem fékk þig til að meta einföld gleði lífsins.", language="Icelandic"),
    Language(text="Il sole stava tramontando all'orizzonte, dipingendo il cielo con vivaci tonalità di arancione e rosa. Una leggera brezza portava con sé il profumo dei fiori freschi, e il suono delle onde che si infrangevano sulla riva riempiva l'aria. Era una serata perfetta, che ti faceva apprezzare le semplici gioie della vita.", language="Italian"),
    Language(text="Saule rietējās aiz apvāršņa, iekrāsojot debesis ar košām oranžām un rozā nokrāsām. Viegla vēja brāzma nesa līdzi svaigu ziedu smaržu, un viļņu skaņa, kas ietriecās krastā, piepildīja gaisu. Tā bija ideāla vakara, kas lika novērtēt dzīves vienkāršos priekus.", language="Latvian"),
    Language(text="Saulė leidosi už horizonto, nudažydama dangų ryškiomis oranžinėmis ir rausvomis spalvomis. Švelnus vėjelis atnešė šviežių gėlių kvapą, o bangų garsas, daužančių krantą, užpildė orą. Tai buvo tobula vakaras, kuriame galėjai įvertinti paprastus gyvenimo džiaugsmus.", language="Lithuanian"),
    Language(text="Ix-xemx kienet qed tnin fuq l-orizzont, iżżebgħa s-sema b'kuluri ħajja oranġjo u roża. Riħ ħafif ġab miegħu l-fwieħa ta’ fjuri friski, u l-ħoss tal-mewġ li qed jolqot ix-xatt imla l-arja. Kienet lejla perfetta, waħda li tagħmlek tapprezza l-ferħ sempliċi tal-ħajja.", language="Maltese"),
    Language(text="Ix-xemx kienet qed tinżel fuq l-orizzont, iżżebgħa s-sema b'kuluri ħajjin ta' oranġjo u roża. Riħ ħafif ġab miegħu l-fwieħa ta' fjuri friski, u l-ħoss tal-mewġ li jolqot ix-xatt imla l-arja. Kienet lejla perfetta, waħda li tagħmlek tapprezza l-ferħ sempliċi tal-ħajja.", language="Maltese"),
    Language(text="Sunce je zalazilo nad horizontom, osvetljavajući nebo živopisnim nijansama narandžaste i ružičaste boje. Blagi povetarac nosio je miris svežeg cveća, a zvuk talasa koji su udarali o obalu ispunjavao je vazduh. Bila je to savršena večer koja te tera da ceniš jednostavne radosti života.", language="Montenegrin"),
    Language(text="Solen gikk ned over horisonten og malte himmelen med levende nyanser av oransje og rosa. En lett bris bar med seg duften av friske blomster, og lyden av bølger som slo mot kysten fylte luften. Det var en perfekt kveld som fikk deg til å sette pris på livets enkle gleder.", language="Norwegian"),
    Language(text="Słońce zachodziło nad horyzontem, malując niebo żywymi odcieniami pomarańczy i różu. Lekki powiew niósł zapach świeżych kwiatów, a dźwięk fal rozbijających się o brzeg wypełniał powietrze. To był idealny wieczór, który sprawiał, że doceniasz proste radości życia.", language="Polish"),
    Language(text="O sol estava se pondo no horizonte, pintando o céu com tons vibrantes de laranja e rosa. Uma brisa suave trazia o aroma de flores frescas, e o som das ondas quebrando na costa enchia o ar. Era uma noite perfeita, que fazia você apreciar as simples alegrias da vida.", language="Portuguese"),
    Language(text="Soarele apunea la orizont, colorând cerul în nuanțe vibrante de portocaliu și roz. O briză ușoară purta mirosul de flori proaspete, iar sunetul valurilor care se izbeau de țărm umplea aerul. Era o seară perfectă, care te făcea să apreciezi bucuriile simple ale vieții.", language="Romanian"),
    Language(text="Sunce je zalazilo nad horizontom, osvetljavajući nebo živopisnim nijansama narandžaste i ružičaste boje. Blagi povetarac nosio je miris svežeg cveća, a zvuk talasa koji su udarali o obalu ispunjavao je vazduh. Bila je to savršena večer koja te tera da ceniš jednostavne radosti života.", language="Serbian"),
    Language(text="Slnko zapadalo za obzor, maľujúc oblohu živými odtieňmi oranžovej a ružovej farby. Jemný vánok niesol vôňu čerstvých kvetov a zvuk vĺn narážajúcich na pobrežie plnil vzduch. Bol to dokonalý večer, ktorý ťa nútil oceniť jednoduché radosti života.", language="Slovak"),
    Language(text="Sonce je zahajalo za obzor in barvalo nebo z živahnimi odtenki oranžne in rožnate barve. Lahek vetrič je prinašal vonj svežega cvetja, in zvok valov, ki so butali ob obalo, je polnil zrak. Bil je popoln večer, ki te je spodbudil k cenjenju preprostih užitkov življenja.", language="Slovenian"),
    Language(text="El sol se estaba poniendo en el horizonte, pintando el cielo con tonos vibrantes de naranja y rosa. Una brisa suave traía consigo el aroma de flores frescas, y el sonido de las olas rompiendo en la orilla llenaba el aire. Era una tarde perfecta que te hacía apreciar las alegrías simples de la vida.", language="Spanish"),
    Language(text="Solen höll på att gå ner vid horisonten och målade himlen i livfulla nyanser av orange och rosa. En mild bris förde med sig doften av färska blommor, och ljudet av vågor som slog mot stranden fyllde luften. Det var en perfekt kväll som fick dig att uppskatta livets enkla glädjeämnen.", language="Swedish"),
    Language(text="D'Sunne isch am Horizont abegange und het de Himmel mit liechtige Farbetöne vo Orangsch und Rosarot gmalt. Es läichts Lüftli het de Duft vo frische Blueme brucht, und d'Wälle, wo an d'Ufer gschlage sind, händ d'Luft erfüllt. Es isch e perfekte Aabig gsi, wo di dranne erinnert het, d'egfachi Freid am Läbe z'werte.", language="Swiss"),
    Language(text="Güneş ufukta batarken, gökyüzünü canlı turuncu ve pembe tonlarıyla boyadı. Hafif bir esinti taze çiçeklerin kokusunu getirdi ve sahile çarpan dalgaların sesi havayı doldurdu. Bu, hayatın basit zevklerini takdir etmenizi sağlayan mükemmel bir akşamdı.", language="Turkish"),
    Language(text="Слънцето залязваше на хоризонта, оцветявайки небето с живи нюанси на оранжево и розово. Лек бриз носеше аромата на свежи цветя, а звукът на вълните, разбиващи се в брега, изпълваше въздуха. Това беше перфектна вечер, която те караше да оцениш простите радости на живота.", language="Bulgarian"),
    Language(text="Сонце сідало за обрій, розмальовуючи небо яскравими відтінками помаранчевого та рожевого. Легкий вітерець приносив аромат свіжих квітів, а звук хвиль, що розбивалися об берег, наповнював повітря. Це був ідеальний вечір, що змушував цінувати прості радощі життя.", language="Ukrainian"),
    Language(text="Солнце садилось за горизонт, окрашивая небо в яркие оттенки оранжевого и розового. Лёгкий ветерок приносил аромат свежих цветов, а звук волн, разбивающихся о берег, наполнял воздух. Это был идеальный вечер, который заставлял ценить простые радости жизни.", language="Russian"),
    Language(text="Ο ήλιος έδυε στον ορίζοντα, χρωματίζοντας τον ουρανό με ζωηρές αποχρώσεις του πορτοκαλί και του ροζ. Ένα ελαφρύ αεράκι έφερνε τη μυρωδιά από φρέσκα λουλούδια, και ο ήχος των κυμάτων που έσκαγαν στην ακτή γέμιζε τον αέρα. Ήταν μια τέλεια βραδιά που σε έκανε να εκτιμήσεις τις απλές χαρές της ζωής.", language="Greek"),
]
