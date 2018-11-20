from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv


author = 'Manu Munoz'

doc = """
Real effort task. A player is shown a word and he has to make new words (min length 5) using the letters of the word shown.
"""

class Constants(BaseConstants):
    name_in_url = 'task_words'
    players_per_group = None

    with open('task_words/list.csv') as f:
        questions = list(csv.DictReader(f)) # PERHAPS INCLUDE THE ANSWERS AS A LIST HERE.

    word1 = ['aeonic','canoe','cocain','cocaine','conic','ocean']
    word2 = ['baking','baning','kiang']
    word3 = ['aedes','ashed','dates','deash','death','deaths','deets','eased','hades','hadst','haets','haste',
            'hasted','hated','hates','heads','heated','heats','heeds','sadhe','sated','seated','sedate','setae',
            'shade','sheet','stade','stead','steed','tease','teased','these','tsade' ]
    word4 = ['arles','asker','askew','eaks','earls','eskar','kales','laker','lakers','lakes','lares','larks',
             'laser','lears','rakes','rales','reals','resaw','saker','sawer','seral','sewar','slake','slaker',
            'swale','sware','swear','waker','wakers','wakes','waler','walers','wales','walker','walks','wares',
            'warks','warsle','weals','wears','wekas','wreak','wreaks']
    word5 = ['alert','alter','areic','ariel','artel','atelic','caret','carle','carte','cartel','cater','ceria',
            'citer','citral','claret','clear','cleat','crate','eclair','eclat','erica','ileac','irate','lacer',
            'lacier','later','liter','litre','ratel','react','recital','recta','rectal','recti','relic','relict',
            'relit','retail','retia','retial','rictal','tailer','taler','telia','telic','terai','tical','tiler',
            'trace','trail','triac','trial','trice']
    word6 = ['cousins','scions','chinos','sushi','sinus','shuns','scion','incus','hocus','cuish','coins','chins',
            'cushion','sonics','cousin','uncos','sonic','sinhs','shins','nisus','icons','cusso','conus','cions','chino']
    word7 = ['coempt','comer','comet','compt','compute','comte','coper','copter','coupe','court','couter','crept','croup','croupe',
            'cruet','crump','crumpet','curet','cuter','eruct','erupt','metro','moper','mucor','mucro','muter','outer','outre',
            'pouter','precut','proem','recoup','recto','rectum','recut','repot','roupet','route','tempo','toper','tromp','trompe',
            'trope','troupe','truce','trump','tumor','uptore']
    word8 = ['compel','clomp','celom']
    word9 = ['retinal','ratline','lantern','trinal','tineal','tanner','retina','retain','rental','ratlin','narine','linter','linear',
            'larine','intern','inaner','antler','trine','train','tinea','terai','telia','riant','renin','relit','nitre','litre',
             'liner','liane','leant','laten','inter','inlet','inane','elint','artel','antre','anent','aline','alert','trenail',
            'reliant','latrine','entrain','tinner','tenail','tailer','retial','retail','renail','ratine','nailer','linnet','learnt',
            'lanner','innate','entail','aliner','trial','trail','tiler','tenia','taler','retia','renal','ratel','niter','liter',
            'linen','learn','later','irate','inner','inert','entia','elain','ariel','anile','alter','alien']
    word10 = ['smooth','soths','sooth','shoot','moths','mosso','hosts','homos','sooths','shoots','soots','shots','shoos',
              'mosts','moots','hoots']
    word11 = ['teiids','teiid','steed','edits','diets','deets','tidies','tides','stied','sited','dites','deist']
    word12 = ['ferula','earful','ureal','lucre','flare','feral','farle','facer','clear','alure','fulcra','fecula',
              'carful','ulcer','lacer','feuar','fecal','farce','cruel','carle']
    word13 = ['tireder','retire','reedit','trier','treed','rider','erred','drier','deter','retried','tiered','retied',
              'dieter','tried','tired','retie','eider','direr']
    word14 = ['savior','carious','soucar','scoria','savior','curios','visor','vicar','vairs','scaur','orcas','curia',
              'coirs','auris','arvos','various','curiosa','vicars','souari','savour','ovisac','arioso','virus','varus',
              'scour','savor','curio','coria','aviso','auric','arcus']
    word15 = ['lucidity','fluidic','tidily','cliffy','lytic','lucid','icily','fluty','fitly','dicty','clift','difficult',
            'fluidity','dulcify','fitful','citify','ludic','licit','fluyt','fluid','fifty','culti','cliff']
    word16 = ['vireo','obeah','haver','bravi','bohea','aiver','abhor','havior','rehab','hover','bravo','brave','bevor','above']
    word17 = ['hippo','hippos','hippy','hooly','hoops','hoppy','hypos','lippy','loops','loopy','loppy','olios','plops',
              'ploys','polio','polios','polis','polish','polos','polyp','polypi','polyps','polys','poohs','pools','poops',
              'popish','popishly','popsy','poshly','shily','shool','slippy','sloop','sloppy','sophy','soppy','spoil','spool','sylph']
    word18 = ['raider','arider','rimer','rider','rearm','ramie','media','irade','drear','direr','derma','darer','armed',
              'airer','aimer','aider','admirer','marred','admire','rimed','redia','rared','mired','madre','drier','dream',
              'dimer','deair','armer','amide','aired','aimed']
    word19 = ['taker','mater','armet','tamer','ramet','maker']
    word20 = ['writes','wisent','twines','twiers','triens','sinter','nitres','inters','inerts','writs','wrist','wrest',
              'wites','wires','weirs','twine','trine','trews','tines','terns','strew','stein','sinew','senti','risen',
              'rewin','rents','nitre','niter','nerts','inter','inert','twiners','wriest','winter','twiner','trines',
              'strewn','rewins','niters','insert','estrin','write','wries','wrens','wiser','wines','twins','twier','tries',
              'tires','tiers','swine','stern','siren','serin','rites','rinse','resin','reins','nites','newts','neist','inset']
    word21 = ['reseals','leasers','sealer','reseal','refels','rassle','leases','lasers','fleers','feases','falser','easels',
              'seres','selfs','seels','seals','sales','safer','reels','reals','rales','lease','leafs','laser','laree','frass',
              'fleer','flare','feres','feels','fears','farle','false','erase','easel','arses','alefs','sealers','resales',
              'earless','sarees','resale','reales','lesser','leaser','larees','flares','farles','erases','serfs','seral',
              'seers','sears','saree','safes','refel','reefs','rases','leers','lears','lases','lares','frees','flees','fleas',
              'fesse','feral','fease','farls','fares','erses','eases','earls','arles']
    word22 = ['ennuis','suns','sinhs','shuns','shine','nisus','issue','shines','sushi','sinus','sines','shins','shies','nines','ennui']
    word23 = ['wenny','renin','winner','winey','rewin','inner']
    word24 = ['suints','satins','units','tunas','suits','stuns','snits','sinus','satin','saint','nisus','issuant',
              'stains','saints','unais','tains','suint','stain','situs','satis','sasin','sains','aunts']
    words = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10,
             word11, word12, word13, word14, word15, word16, word17, word18, word19, word20,
             word21, word22, word23, word24]
    # A better way would maybe be to have alle the answers as lists in a dictionary instead of as seperate lists, then we could just reference the item in the dictionary instead of having
    # to make a list of lists.... A matter of taste.

    num_rounds = 100

    min_answer_length = 5


class Subsession(BaseSubsession):
    word_points = models.FloatField()

    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions

        for i in self.get_players():
            for word in Constants.questions:
                i.participant.vars[word['question']] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    word_num = models.PositiveIntegerField(initial=0)
    word_id = models.IntegerField()
    word = models.StringField()
    submitted_answer = models.StringField(blank=True)
    # El blank=True es por ahora valido para testing, luego lo quito
    word_points = models.FloatField()
    word_show = models.PositiveIntegerField(initial=0)
    word_increment = models.IntegerField(initial=0)
    total_payoff = models.CurrencyField(initial=0)

    is_correct = models.BooleanField()
    payoff_score = models.IntegerField()

    def current_question(self):
        if self.round_number>1:
            self.word_show = self.in_round(self.round_number-1).word_show
        return self.session.vars['questions'][self.word_show]

    def word_check(self):
        if self.submitted_answer in Constants.words[self.word_show] and self.submitted_answer not in self.participant.vars[Constants.questions[self.word_show]['question']]:

            self.participant.vars[Constants.questions[self.word_show]['question']].append(self.submitted_answer)

            self.is_correct = True
            self.payoff_score = (len(self.submitted_answer) - 4)
        else:
            self.is_correct = False
            self.payoff_score = -1 * (len(self.submitted_answer) - 4)

        print(self.is_correct)
        self.payoff += c(self.payoff_score)
        self.total_payoff = c(sum([p.payoff for p in self.in_all_rounds()]))

    # Checks if the given answer is empty or shorter than the min_lenght, in which case returns false
    def validate_answer(self, answer):
        if len(answer) < Constants.min_answer_length or answer == 'None':
            return False
        return True

    def set_payoffs(self):
        self.payoff = self.payoff_score