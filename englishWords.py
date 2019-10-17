# englishWords.py

import re

from pinyin_utils import getVersion

reNonAscii = re.compile(r'[^\x00-\x7F]')
reOr = re.compile(r'^(\S+)\s+or\s+(\S+)')
reReject = re.compile(r'''
		^(
		[A-Za-z] \.   # an initial
		|
		[A-Z]{2,}     # two or more capital letters
		|
		.+ \'         # word ends with apostrophe
		|
		\' .+         # word starts with apostrophe
		)$''',
		re.X)

hAbbrev = None
hFix = None
setSkip = None
__VERSION__ = getVersion()

# ---------------------------------------------------------------------------

def isAbbrev(word):

	return hAbbrev.get(word)

# ---------------------------------------------------------------------------

def fixWord(word, debug=False):
	# --- Return None to skip this word

	orgWord = word    # for debugging

	# --- Reject if it has any non-ASCII characters
	if reNonAscii.match(word):
		if debug:
			print(f"   fixWord('{word}'): REJECT non-ASCII")
		return None

	# --- Extract first word in "A or B"
	#     this is particular to Wiktionary
	result = reOr.match(word)
	if result:
		newWord = result.group(1)
		if debug:
			print(f"   fixWord('{word}') => '{newWord}'")
		word = newWord

	# --- Check for explicit fixes
	if word in hFix:
		fixed = hFix[word]
		if debug:
			print(f"   fixWord('{word}'): FIX to {fixed} (in hFix)")
		return fixed

	if reReject.match(word):
		if debug:
			print(f"   fixWord('{word}'): REJECT")
		return None

	# --- Check for explicit skips
	if word.lower() in setSkip:
		if debug:
			print(f"   fixWord('{word}'): SKIP (in setSkip)")
		return None
	return word

# ---------------------------------------------------------------------------

hAbbrev = {
	"I'm": "I am",
	"I've": "I have",
	"it's": "it is",
	"you're": "you are",
	"that's": "that is",
	"can't": "can not",
	"he's": "he is",
	"she's": "she is",
	"didn't": "did not",
	"we're": "we are",
	"don't": "do not",
	"I'll": "I will",
	"we'll": "we will",
	"what's": "what is",
	"there's": "there is",
	"let's": "let us",
	"doesn't": "does not",
	"you've": "you have",
	"they're": "they are",
	"I'd": "I would",
	"isn't": "is not",
	"aren't": "are not",
	"won't": "will not",
	"ain't": "is not",
	"wouldn't": "would not",
	"wasn't": "was not",
	"gonna": "going to",
	"wanna": "want to",
	"you'll": "you will",
	"haven't": "have not",
	"couldn't": "could not",
	"we've": "we have",
	"gotta": "got to",
	"we've": "we have",
	"you'd": "you would",
	"who's": "who has",
	"shouldn't": "should not",
	"where's": "where is",
	"he'll": "he will",
	"it'll": "it will",
	"weren't": "were not",
	"how's": "how is",
	"here's": "here is",
	"she'll": "she will",
	"they'll": "they will",
	"hasn't": "has not",
	"we'd": "we would",
	"he'd": "he would",
	"they've": "they have",
	"would've": "would have",
	"hadn't": "had not",
	"everything's": "everything is",
	"she'd": "she would",
	"how'd": "how would",
	"could've": "could have",
	"c'mon": "come on",
	"should've": "should have",
	"outta": "out of",
	"what'd": "what did",
	"that'll": "that will",
	"something's": "something is",
	"they'd": "they would",
	"it'd": "it would",
	"where'd": "where did",
	"must've": "must have",
	"nothing's": "nothing is",
	"why'd": "why did",
	"what're": "what are",
	'gimme': 'give me',
	"that'd": 'that would',
	"there'll": 'there will',
	"who'd": 'who would',
	'dunno': "don't know",
	"when's": "when is",
	}

hFix = {
	'Rose': 'rose',
	'Angel': 'angel',
	'Eve': 'eve',
	'Ivy': 'ivy',
	'days': 'day',
	'minutes': 'minute',
	'eyes': 'eye',
	'hours': 'hour',
	'parents': 'parent',
	'months': 'month',
	'tv': 'TV',
	'bucks': 'buck',
	'papers': 'paper',
	"guy's": 'guy',
	"dad's": 'dad',
	"man's": 'man',
	"mom's": 'mom',
	'Tad': 'tad',
	'stories': 'story',
	'stars': 'star',
	'cars': 'car',
	'facts': 'fact',
	'pills': 'pill',
	'dogs': 'dog',
	"name's": 'name',
	'students': 'student',
	'witches': 'witch',
	"brother's": 'brother',
	'messages': 'message',
	'somethin': 'something',
	'nothin': 'nothing',
	'letters': 'letter',
	'decisions': 'decision',
	"daughter's": 'daughter',
	"son's": 'son',
	'animals': 'animal',
	"sister's": 'sister',
	"year's": 'year',
	'balls': 'ball',
	'talkin': 'talking',
	"woman's": 'woman',
	'yourselves': 'yourself',
	'walls': 'wall',
	'parties': 'party',
	'leads': 'lead',
	'gettin': 'getting',
	"hell's": 'hell',
	'bodies': 'body',
	"girl's": 'girl',
	'dates': 'date',
	'reminds': 'remind',
	'twins': 'twin',
	'options': 'option',
	'members': 'member',
	'minds': 'mind',
	'lawyers': 'lawyer',
	'burns': 'burn',
	'tricks': 'trick',
	'cookies': 'cookie',
	'families': 'family',
	"family's": 'family',
	'comin': 'coming',
	'tears': 'tear',
	'knees': 'knee',
	"wife's": 'wife',
	'lookin': 'looking',
	"husband's": 'husband',
	'gifts': 'gift',
	"kid's": 'kid',
	'classes': 'class',
	'millions': 'million',
	'vampires': 'vampire',
	'hits': 'hit',
	'birds': 'bird',
	"life's": 'life',
	'holidays': 'holiday',
	'wishes': 'wish',
	'candles': 'candle',
	'Americans': 'American',
	"world's": 'world',
	'relationships': 'relationship',
	"daddy's": 'daddy',
	'trees': 'tree',
	'rocks': 'rock',
	'banks': 'bank',
	"other's": 'other',
	"today's": 'today',
	'sons': 'son',
	'fella': 'fellow',
	'enemies': 'enemy',
	'thousands': 'thousand',
	'clients': 'client',
	'witnesses': 'witness',
	'instincts': 'instinct',
	'actions': 'action',
	'agents': 'agent',
	'answered': 'answer',
	'answers': 'answer',
	'appears': 'appear',
	'arguing': 'argue',
	'arms': 'arm',
	'arranged': 'arrange',
	'asked': 'ask',
	'asking': 'ask',
	'assumed': 'assume',
	'assuming': 'assume',
	'attacked': 'attack',
	'babies': 'baby',
	'bags': 'bag',
	'bars': 'bar',
	'beating': 'beat',
	'beats': 'beat',
	'belongs': 'belong',
	'betrayed': 'betray',
	'bills': 'bill',
	'blowing': 'blow',
	'bones': 'bone',
	'books': 'book',
	'boots': 'boot',
	'bothering': 'bother',
	'boys': 'boy',
	'brains': 'brain',
	'breaks': 'break',
	'brothers': 'brother',
	'buying': 'buy',
	'called': 'call',
	'calling': 'call',
	'calls': 'call',
	'cards': 'card',
	'cases': 'case',
	'chances': 'chance',
	'changes': 'change',
	'charges': 'charge',
	'chasing': 'chase',
	'china': 'China',
	'choices': 'choice',
	'cops': 'cop',
	'demons': 'demon',
	'details': 'detail',
	'doctors': 'doctor',
	'dollars': 'dollar',
	'doors': 'door',
	'dreaming': 'dream',
	'drinking': 'drink',
	'drinks': 'drink',
	'drugs': 'drug',
	'ears': 'ear',
	'eggs': 'egg',
	'events': 'event',
	'excuses': 'excuse',
	'faces': 'face',
	'falls': 'fall',
	'falling': 'fall',
	'feelings': 'feeling',
	'fighting': 'fight',
	'figured': 'figure',
	'files': 'file',
	'finding': 'find',
	'finds': 'find',
	'fingers': 'finger',
	'flowers': 'flower',
	'following': 'follow',
	'forgetting': 'forget',
	'friends': 'friend',
	'fucked': 'fuck',
	'fucking': 'fuck',
	'games': 'game',
	'girls': 'girl',
	'guards': 'guard',
	'guests': 'guest',
	'guns': 'gun',
	'guys': 'guy',
	'hands': 'hand',
	'hearts': 'heart',
	'hoped': 'hope',
	'horses': 'horse',
	'hundreds': 'hundred',
	'interests': 'interest',
	'interrupting': 'interrupt',
	'invited': 'invite',
	'issues': 'issue',
	'joining': 'join',
	'avoiding': 'avoid',
	'schools': 'school',
	'catching': 'catch',
	'sneaking': 'sneak',
	'imagined': 'imagine',
	'symptoms': 'symptom',
	'cameras': 'camera',
	'concerns': 'concern',
	'remembering': 'remember',
	'crimes': 'crime',
	'doubts': 'doubt',
	'pages': 'page',
	'gloves': 'glove',
	'occurred': 'occur',
	'boxes': 'box',
	'chips': 'chip',
	'aliens': 'alien',
	'daughters': 'daughter',
	'joined': 'join',
	'vows': 'vow',
	}

# ---------------------------------------------------------------------------

# --- Especially, skip people's names
#     Even if they're words, the frequency is misleading
#     Case is not relevant

strSkip = """
	john sam jack jimmy oh
	sonny tony billy nick victor
	o'neill maciver grace uh huh
	um hmm ah ha ya mm leo
	theresa carly ethan paul david
	jen ooh jake al michael max lewis
	louis crane natalie frank lucy y'know
	sheridan ben julian joey antonio
	jason george ross brooke niles todd
	alison rick frazier york danny nbsp
	craig ray bo luis frasier miguel
	cristian greenlee phoebe luke emily timmy
	chris kay jerry richard jesus james ryan
	lindsey lindsay mmm beth nora jax jessica
	dawson alexis shawn barbara adam mike kevin
	buffy chloe rafe shh erica brenda jim blair
	laura elizabeth sabrina phillip philip eric
	olivia cassie aaron kendall tom josh simon ho
	one's hal aw edmund brady troy mary courtney
	mark alan joe tim roz bob mother's sharon
	jennifer diane bridget brad livvie er charlie
	karen eh skye molly kyle father's alex th
	liz ian henry phyllis mac maria isaac abigail
	god's anna simone amber pacey liza daphney whitney
	chad la katie mitch rory heh larry prue bianca
	paige ohh eddy eddie yo rebecca viki chandler
	nikolas starr gee monica steve ugh jill taylor
	charles neal neil christ doin harry elaine
	rachel salem colleen goddamn keri vanessa ahem
	tess scot scott nah michelle ned bonnie umm
	austin peter amy whoo brian nobody's margo hank
	reva stenbeck gwen marah mia re ed alkazar kramer
	kate martin asa harvey dave andy jess colin
	amanda fraser caleb someone's seth rosanna nicole
	allison forrester isabella lexie sami lily edward
	diego cole kenny bobby bobbie ahh sally stephanie
	parker de toby blake frankie kelly brittany jamal
	roy dean gia everybody's nicholas somebody's holden
	corinthos zander sarah sara brandon san santa
	jackson helena victoria hm baby's ricky raul
	stephen steven harley jack's daniel roger stan julia
	da blah aah newman maureen everyone's oakdale
	pete lucas trey jan abby don sean lee
	dick donna malcolm vegas bud baldwin gus susan
	santos people's annie sydney lorelai jackie maggie
	sonny's johnny johnnie tabitha lisa morgan ashley
	cartman ted kristina casey hoo nancy xander giles
	non russell mateo spaulding carmen diana
	abe v laurence hayward dan kane alexandra hilda
	travers matthew jeez buchanan dixie rex tory seattle
	zach zack aidan lizzie washington christine kim lt
	bryant montgomery walter tommy matt glenn con phil
	helen nikki caroline maris rae abbott carter smith
	jane william wh uhh proteus mimi audrey q marty
	greta barry wesley else's thomas logan robert snyder
	harold fred sec quinn llanview theresa's randy zelda
	palmer manning jamie janie colby bart claire nate
	carly's harvard mel quartermaine mackenzie margaret
	carl homer del laurie co jenny massimo walker
	mickey gabrielle julie joshua valerie lucinda holly
	dimera roxy chuck thorne hughes spencer alice peggy
	pre kristen zach mum roxanne andie tricia lorelei
	sakes hon wayne cordelia robbie alcazar al's ali
	arnold bauer bennett betty catalina cooper daphne darla
	davidson davis doug elliot ellison emma ephram gina greg
	hayley howard bruce bermuda florida hollywood isabel
	jenkins johnson jones julian's katherine keith lauren
	linda nathan niki nina oz ralph rappaport reese
	roman romeo samantha sandburg sookie stanley stuart
	valentine's vega vince will's williams accepted
	acted amp belle boo d'you dahlia daria deacon
	duke fellas geez glen goa'uld gt hah hmmm ma'am
	St. Timmy's Marlena Benny Norman Lloyd Andrew Sheridan's
	Cassadine Libby Wilson Ethan's Stefan Springfield Sid
	Louise Jean Winnie Patrick Coleman Bundy woo Leo's
	Ellen president's teal'c tonight's boy's ba
	Eden Ellen shhh shh oooh ooh ohhh ohh whew Leo's yay Bundy
	warren Val yah Sheila ups Stefano doctor's rach sherry
	thou barb anti el carol cris
	"""

setSkip = set()
for word in strSkip.split():
	setSkip.add(word.lower())
