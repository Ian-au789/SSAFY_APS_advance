common_proverbs = {
    "abirdinthehandisworthtwointhebush",
    "apictureisworthathousandwords",
    "actionsspeaklouderthanwords",
    "allgoodthingsmustcometoanend",
    "allthatglittersisnotgold",
    "anappleadaykeepsthedoctoraway",
    "beautyisintheeyeofthebeholder",
    "beggarscantbechoosers",
    "betterlatethannever",
    "bettersafethansorry",
    "cleanlinessisnexttogodliness",
    "dontbitethehandthatfeedsyou",
    "dontcountyourschickensbeforetheyhatch",
    "dontcryoverspiltmilk",
    "dontjudgeabookbyitscover",
    "dontputallyoureggsinonebasket",
    "easycomeeasygo",
    "everycloudhasasilverlining",
    "fortunefavorsthebold",
    "godhelpsthosewhohelpthemselves",
    "goodthingscometothosewhowait",
    "hastemakeswaste",
    "honestyisthebestpolicy",
    "ifatfirstyoudontsucceedtrytryagain",
    "ifitaintbrokedontfixit",
    "ignoranceisbliss",
    "ittakesonetoknowone",
    "keepyourfriendscloseandyourenemiescloser",
    "laughteristhebestmedicine",
    "letsleepingdogslie",
    "lookbeforeyouleap",
    "loveisblind",
    "moneydoesntgrowontrees",
    "nopainnogain",
    "practicemakesperfect",
    "preventionisbetterthancure",
    "romewasntbuiltinaday",
    "silenceisgolden",
    "slowandsteadywinsherace",
    "strikewhiletheironishot",
    "theearlybirdcatchestheworm",
    "thegrassisalwaysgreenerontheotherside",
    "thepenismightierthanthesword",
    "thesqueakywheelgetsthegrease",
    "theresnoplacelikehome",
    "theresnosuchthingasafreelunch",
    "timeandtidewaitfornoman",
    "timehealsallwounds",
    "toomanycooksspoilthebroth",
    "twoheadsarebetterthanone",
    "varietyisthespiceoflife",
    "whatgoesaroundcomesaround",
    "wheninromedoastheromansdo",
    "whenthegoinggetstoughthetoughgetgoing",
    "wheretheresawilltheresaway",
    "youcantjudgeabookbyitscover",
    "youcanthaveyourcakeandeatittoo",
    "youcantmakeanomeletwithoutbreakingeggs",
    "youcanleadahorsetowaterbutyoucantmakeitdrink",
    "absencemakestheheartgrowfonder",
    "awatchedpotneverboils",
    "curiositykilledthecat",
    "dontputoffuntiltomorrowwhatyoucando",
    "everydoghasitsday",
    "afriendinneedisafriendindeed",
    "familiaritybreedscontempt",
    "greatmindsthinkalike",
    "honoramongthieves",
    "jackofalltradesmasterofnone",
    "letthecatoutofthebag",
    "manyhandsmakelightwork",
    "miserylovescompany",
    "nothingventurednothinggained",
    "oldhabitsdiehard",
    "oncebittentwiceshy",
    "outofsightoutofmind",
    "patienceisavirtue",
    "peoplewholiveinglasshousesshouldntthrowstones",
    "practicewhatyoupreach",
    "stillwatersrundeep",
    "thebestthingsinlifearefree",
    "thecustomerisalwaysright",
    "themorethemerrier",
    "theresnosmokewithoutfire",
    "thistooshallpass",
    "toerrishumantoforgivedivine",
    "toeachehisown",
    "whatsdoneisdone",
    "youcancatchmoreflieswithhoneythanwithvinegar",
    "youcantalwaysgetwhatyouwant",
    "youreapwhatyousow",
    "youwinsomeyoulosesome",
    "bloodisthickerthanwater",
    "dontthrowthebabyoutwiththebathwater",
    "theappledoesntfallfarfromthetree",
    "theroadtohellispavedwithgoodintentions",
    "hewholaughslastlaughsbest",
    "achainisonlyasstrongasitsweakestlink",
    "dontburnyourbridgesbehindyou",
    "ifyouplaywithfireyoullgetburned",
    "abarkingdogneverbites",
    "abigfishinasmallpond",
    "agoodmedicinetastesbitter",
    "itneverrainsbutitpours",
    "abadworkmanblameshistools",
    "wallshaveears",
    "adrowningmanwillcatchatastro",
    "youscratchmybackandillscratchyours",
    "betweenarockandahardplace",
    "foolsrushinwhereangelsfeartotread",
    "dontkillthegoosethatlaysthegoldeneggs",
    "dontputthecartbeforethehorse",
    "emptyvesselsmakethemostsound",
    "nonewsisgoodnews",
    "iftheresnowindrow",
    "asoundmindinasoundbody",
    "sleepisbetterthanmedicine",
    "nosmokewithoutfire",
    "ittakestwototango",
    "ifyoucantbeatthemjointhem",
    "youarewhatyoueat",
    "moneyisnteverything",
    "loversarefools",
    "willispower",
    "afriendisknowninnecessity",
    "letbygonesbebygones",
    "thegrassisalwaysgreenerontheothersideofthefence",
    "dontcrossthebridgeuntilyoucometoit",
    "nomanisanisland",
    "birdsofafeatherflocktogether",
    "theproofofthepuddingisintheeating",
    "aleopardcannotchangehisspots",
    "afterastormcomesacalm",
    "aheavypursemakesalightheart",
    "makehaywhilethesunshines",
    "amanisknownbythecompanyhekeeps",
    "evenawormwillturn"
}


def get_ord_diff_features(word):
    """주어진 문자열에서 주요 ordinal 차이를 추출"""
    length = len(word)
    if length < 3:
        return None
    mid = length // 2
    return [((ord(word[0]) - ord(word[mid])) % 26, (ord(word[mid]) - ord(word[-1])) % 26)]


def decode_caesar_using_shape(cipher, proverb_set):
    # 1. 글자 수가 같은 속담만 필터링
    candidates = [p for p in proverb_set if len(p) == len(cipher)]

    # 2. ord 차이 특징 추출
    cipher_feat = get_ord_diff_features(cipher)
    if not cipher_feat:
        return 0  # 너무 짧아서 비교 불가

    # 3. 특징이 동일한 속담 후보 필터링
    decoded = []
    for p in candidates:
        if get_ord_diff_features(p) == cipher_feat:
            decoded.append(p)

    # 4. 결과 결정
    if len(decoded) == 1:
        return decoded[0]
    return len(decoded)  # 후보가 없거나 2개 이상인 경우


def caesar_decrypt(cipher: str, shift: int) -> str:
    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # 알파벳 외 문자는 그대로
    return result


test_case = [
    "achainisonlyasstrongasitsweakestlink",
    "dontburnyourbridgesbehindyou",
    "ifyouplaywithfireyoullgetburned",
    "abarkingdogneverbites",
    "abigfishinasmallpond",
    "agoodmedicinetastesbitter",
    "itneverrainsbutitpours",
    "abadworkmanblameshistools",
    "wallshaveears",
    "adrowningmanwillcatchatastro",
    "youscratchmybackandillscratchyours",
    "betweenarockandahardplace",
    "foolsrushinwhereangelsfeartotread",
    "dontkillthegoosethatlaysthegoldeneggs",
    "dontputthecartbeforethehorse",
    "emptyvesselsmakethemostsound",
    "nonewsisgoodnews",
    "iftheresnowindrow",
    "asoundmindinasoundbody",
    "sleepisbetterthanmedicine",
    "nosmokewithoutfire",
    "ittakestwototango",
    "ifyoucantbeatthemjointhem",
    "youarewhatyoueat",
    "moneyisnteverything",
    "loversarefools",
    "willispower",
    "afriendisknowninnecessity",
    "letbygonesbebygones",
    "thegrassisalwaysgreenerontheothersideofthefence",
    "dontcrossthebridgeuntilyoucometoit",
    "nosmokewithoutfire",
    "ittakestwototango",
    "ifyoucantbeatthemjointhem",
    "youarewhatyoueat",
    "moneyisnteverything",
    "loversarefools",
    "willispower",
    "afriendisknowninnecessity",
    "letbygonesbebygones",
    "thegrassisalwaysgreenerontheothersideofthefence",
    "dontcrossthebridgeuntilyoucometoit",
    "nomanisanisland",
    "birdsofafeatherflocktogether",
    "theproofofthepuddingisintheeating",
    "aleopardcannotchangehisspots",
    "afterastormcomesacalm",
    "aheavypursemakesalightheart",
    "makehaywhilethesunshines",
    "amanisknownbythecompanyhekeeps",
    "evenawormwillturn"
]

ciphers = []
for t in test_case:
    ciphers.append(caesar_decrypt(t, 13))

for cipher in ciphers:
    result = decode_caesar_using_shape(cipher, common_proverbs)
    print(f"복호 결과: {result}" if type(result) == str else f"해독 실패 또는 다중 후보 : {result}")
