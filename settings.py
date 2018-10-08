import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

# don't share this with anybody.
SECRET_KEY = 'mgz=n2r#zx412)_-r57o%7158(zdxopg1fc9_i1lk@54lvcqrz'


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree',]

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1,
    'participation_fee': 0,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'network_identity',
        'display_name': "network_identity",
        'num_demo_participants': 7,
        'app_sequence': ['network_identity'],
    },
    {
        'name': 'instructions',
        'display_name': "instructions",
        'num_demo_participants': 1,
        'app_sequence': ['instructions'],
    },
    # {
    #     'name': 'inst_spillovers',
    #     'display_name': "inst_spillovers",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['inst_spillovers'],
    # },
    {
        'name': 'group_spillover',
        'display_name': "group_spillover",
        'num_demo_participants': 4,
        'app_sequence': ['group_spillover'],
    },
    {
        'name': 'group_spillover_no',
        'display_name': "group_spillover_no",
        'num_demo_participants': 4,
        'app_sequence': ['inst_spillovers','group_spillover'],
        'treatment': 1,
    },
    {
        'name': 'group_spillover_low',
        'display_name': "group_spillover_low",
        'num_demo_participants': 4,
        'app_sequence': ['inst_spillovers', 'group_spillover'],
        'treatment': 2,
    },
    {
        'name': 'group_spillover_high',
        'display_name': "group_spillover_high",
        'num_demo_participants': 4,
        'app_sequence': ['inst_spillovers', 'group_spillover'],
        'treatment': 3,
    },
    # {
    #     'name': 'network_identity2',
    #     'display_name': "network_identity2",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['network_identity2'],
    # },
    # {
    #     'name': 'network_study',
    #     'display_name': "network_study",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['network_study'],
    # },
    # {
    #     'name': 'networx_individual',
    #     'display_name': "Network - for single player",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['networx_individual'],
    # },
    # {
    #     'name': 'networx',
    #     'display_name': "Network - for three players",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['networx'],
    # },
    # {
    #     'name': 'networx2',
    #     'display_name': "Network - for 3 players",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['networx2'],
    # },
    # {
    #     'name': 'networx_custom',
    #     'display_name': "Network - for three players, scalable, using custom models",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['networx_custom'],
    # },
    # {
    #     'name': 'net_formation',
    #     'display_name': "net_formation",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['net_formation'],
    # },
    {
        'name': 'diversity',
        'display_name': "Diversity",
        'num_demo_participants': 4,
        'app_sequence': ['diversity'],
    },
    # {
    #     'name': 'min_effort',
    #     'display_name': "Min. Effort",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['min_effort'],
    # },
    {
        'name' : 'canvas',
        'display_name' : "canvas",
        'num_demo_participants' : 4,
        'app_sequence' : ['canvas'],
    },
    # {
    #     'name': 'id_switch',
    #     'display_name': "ID Switch",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['id_switch'],
    # },
    # {
    #     'name' : 'matrixgman',
    #     'display_name' : "Matrixgman",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['matrixgman', 'final'],
    # },
    # {
    #     'name': 'word_task',
    #     'display_name': "Word Task",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['word_task', 'final'],
    # },
    # {
    #     'name': 'sum_task',
    #     'display_name': "Sum Task",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['sum_task', 'final'],
    # },
    # {
    #     'name' : 'test_qualtrix',
    #     'display_name' : "Test Qualtrix",
    #     'num_demo_participants' : 12,
    #     'app_sequence' : ['qualtrix', 'matrixgman', 'qualtrix2'],
    # },
    # {
    #     'name' : 'payment_info',
    #     'display_name' : "Payment info",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['payment_info'],
    # },
    # {
    #     'name' : 'attached_en',
    #     'display_name' : "Attachment Survey English",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['attached_en',],
    # },
    # {
    #     'name' : 'attached',
    #     'display_name' : "Attachment",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['attached',],
    # },
    # {
    #     'name' : 'qualtrix',
    #     'display_name' : "Qualtrix",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['qualtrix'],
    # },
    # {
    #     'name' : 'qualtrix2',
    #     'display_name' : "Qualtrix2",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['qualtrix', 'qualtrix2'],
    # },
   # {
   #      'name' : 'matrix',
   #      'display_name' : "Matrix",
   #      'num_demo_participants' : 2,
   #      'app_sequence' : ['matrix'],
   #  },
    # {
    #     'name': 'public_goods',
    #     'display_name': "Public Goods",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['public_goods', 'payment_info'],
    # },
    # {
    #     'name': 'trust',
    #     'display_name': "Trust Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['trust', 'payment_info'],
    # },
    # {
    #     'name': 'guess_two_thirds',
    #     'display_name': "Guess 2/3 of the Average",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['guess_two_thirds', 'payment_info'],
    # },
    # {
    #     'name': 'survey',
    #     'display_name': "Survey",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'display_name': "Quiz",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },
    # {
    #     'name': 'prisoner',
    #     'display_name': "Prisoner's Dilemma",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['prisoner', 'payment_info'],
    # },
    # {
    #      'name': 'ultimatum',
    #      'display_name': "Ultimatum (randomized: strategy vs. direct response)",
    #      'num_demo_participants': 2,
    #      'app_sequence': ['ultimatum', 'payment_info'],
    # },
    # {
    #     'name': 'ultimatum_strategy',
    #     'display_name': "Ultimatum (strategy method treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': True,
    # },
    # {
    #     'name': 'ultimatum_non_strategy',
    #     'display_name': "Ultimatum (direct response treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': False,
    # },
    # {
    #     'name': 'vickrey_auction',
    #     'display_name': "Vickrey Auction",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['vickrey_auction', 'payment_info'],
    # },
    # {
    #     'name': 'volunteer_dilemma',
    #     'display_name': "Volunteer's Dilemma",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['volunteer_dilemma', 'payment_info'],
    # },
    # {
    #     'name': 'cournot',
    #     'display_name': "Cournot Competition",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'cournot', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'principal_agent',
    #     'display_name': "Principal Agent",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['principal_agent', 'payment_info'],
    # },
    # {
    #     'name': 'dictator',
    #     'display_name': "Dictator Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dictator', 'payment_info'],
    # },
    # {
    #     'name': 'matching_pennies',
    #     'display_name': "Matching Pennies",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'matching_pennies',
    #     ],
    # },
    # {
    #     'name': 'traveler_dilemma',
    #     'display_name': "Traveler's Dilemma",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['traveler_dilemma', 'payment_info'],
    # },
    # {
    #     'name': 'bargaining',
    #     'display_name': "Bargaining Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['bargaining', 'payment_info'],
    # },
    # {
    #     'name': 'common_value_auction',
    #     'display_name': "Common Value Auction",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['common_value_auction', 'payment_info'],
    # },
    # {
    #     'name': 'stackelberg',
    #     'display_name': "Stackelberg Competition",
    #     'real_world_currency_per_point': 0.01,
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'stackelberg', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'bertrand',
    #     'display_name': "Bertrand Competition",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'bertrand', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'real_effort',
    #     'display_name': "Real-effort transcription task",
    #     'num_demo_participants': 1,
    #     'app_sequence': [
    #         'real_effort',
    #     ],
    # },
    # {
    #     'name': 'lemon_market',
    #     'display_name': "Lemon Market Game",
    #     'num_demo_participants': 3,
    #     'app_sequence': [
    #         'lemon_market', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'battle_of_the_sexes',
    #     'display_name': "Battle of the Sexes",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'battle_of_the_sexes', 'payment_info'
    #     ],
    # },
    {
        'name': 'p1_frst3',
        'display_name': "p1_frst3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_no3'],
        'treatment': 1,
    },
    {
        'name': 'p1_no3',
        'display_name': "p1_no3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_no3'],
        'treatment': 2,
    },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
