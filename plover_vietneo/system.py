# vim: set fileencoding=utf-8 :

# #CTNRGLHUOA*IEZWNCMTFJRX
KEYS = (
    '#',
    'C-', 'T-', 'N-', 'R-', 'G-', 'L-', 'H-', 'U-',
    'O-', 'A-',
    '*',
    '-I', '-E',
    '-Z', '-W', '-N', '-C', '-M', '-T', '-F', '-J', '-R', '-X',
)

IMPLICIT_HYPHEN_KEYS = ('U-', 'O-', 'A-', '-I', '-E', '*', '-W')
#IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'C-': '1-',
    'N-': '2-',
    'G-': '3-',
    'H-': '4-',
    'O-': '5-',
    'A-': '0-',
    '-Z': '-6',
    '-N': '-7',
    '-M': '-8',
    '-F': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'C-'        : 'S1-',
        'T-'        : 'S2-',
        'N-'        : 'T-',
        'R-'        : 'K-',
        'G-'        : 'P-',
        'L-'        : 'W-',
        'H-'        : 'H-',
        'U-'        : 'R-',
        'O-'        : 'A-',
        'A-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-I'        : '-E',
        '-E'        : '-U',
        '-Z'        : '-F',
        '-W'        : '-R',
        '-N'        : '-P',
        '-C'        : '-B',
        '-M'        : '-L',
        '-T'        : '-G',
        '-F'        : '-T',
        '-J'        : '-S',
        '-R'        : '-D',
        '-X'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'C-'        : 'q',
        'T-'        : 'a',
        'N-'        : 'w',
        'R-'        : 's',
        'G-'        : 'e',
        'L-'        : 'd',
        'H-'        : 'r',
        'U-'        : 'f',
        'O-'        : 'c',
        'A-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-I'        : 'n',
        '-E'        : 'm',
        '-Z'        : 'u',
        '-W'        : 'j',
        '-N'        : 'i',
        '-C'        : 'k',
        '-M'        : 'o',
        '-T'        : 'l',
        '-F'        : 'p',
        '-J'        : ';',
        '-R'        : '[',
        '-X'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_vietneo:dictionaries'
DEFAULT_DICTIONARIES = ('vietneo_user.json', 'vietneo_commands.json', 'vietneo_main.json')
