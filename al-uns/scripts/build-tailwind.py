# -*- coding: utf-8 -*-
"""Genera un CSS statico con le sole utility Tailwind usate dal sito al-uns."""
import re, glob, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'al-uns'
OUT  = sys.argv[2] if len(sys.argv) > 2 else 'al-uns/assets/tailwind.css'

SP = {'0':'0px','0.5':'0.125rem','1':'0.25rem','1.5':'0.375rem','2':'0.5rem','2.5':'0.625rem',
 '3':'0.75rem','3.5':'0.875rem','4':'1rem','5':'1.25rem','6':'1.5rem','7':'1.75rem','8':'2rem',
 '9':'2.25rem','10':'2.5rem','11':'2.75rem','12':'3rem','14':'3.5rem','16':'4rem','20':'5rem',
 '24':'6rem','28':'7rem','32':'8rem','36':'9rem','40':'10rem','44':'11rem','48':'12rem',
 '64':'16rem','72':'18rem','80':'20rem','px':'1px','auto':'auto','full':'100%'}
FS = {'xs':('0.75rem','1rem'),'sm':('0.875rem','1.25rem'),'base':('1rem','1.5rem'),
 'lg':('1.125rem','1.75rem'),'xl':('1.25rem','1.75rem'),'2xl':('1.5rem','2rem'),
 '3xl':('1.875rem','2.25rem'),'4xl':('2.25rem','2.5rem'),'5xl':('3rem','1'),
 '6xl':('3.75rem','1'),'7xl':('4.5rem','1')}
GRAY = {'50':'#f9fafb','100':'#f3f4f6','200':'#e5e7eb','300':'#d1d5db','400':'#9ca3af','500':'#6b7280'}
MAXW = {'sm':'24rem','md':'28rem','xl':'36rem','2xl':'42rem','3xl':'48rem','4xl':'56rem','5xl':'64rem','6xl':'72rem'}
ROUND = {'':'0.25rem','lg':'0.5rem','xl':'0.75rem','2xl':'1rem','3xl':'1.5rem','full':'9999px'}
LEAD = {'snug':'1.375','relaxed':'1.625','loose':'2'}
TRACK = {'wide':'0.025em','wider':'0.05em'}
FRAC = {'1/2':'50%','1/3':'33.333333%','2/3':'66.666667%','2/5':'40%','3/5':'60%'}
BP = {'sm':'640px','md':'768px','lg':'1024px','xl':'1280px'}

# classi definite negli <style> di pagina: non sono Tailwind, non vanno generate
CUSTOM = {'ar','ar-name','ar-verse','arabic','bg-cream','card-img','card-refs','gl-entry','gl-section',
 'heading','img-cover','kicker','panel','section-label','text-primary','text-secondary','translit',
 'tr-verse','verse-ar','verse-block','verse-tr','group','text-secondary/80'}

TRANS = 'transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s'
SIMPLE = {
 'block':'display:block','inline-block':'display:inline-block','inline-flex':'display:inline-flex',
 'flex':'display:flex','grid':'display:grid','hidden':'display:none','relative':'position:relative',
 'absolute':'position:absolute','fixed':'position:fixed','flex-col':'flex-direction:column',
 'flex-row':'flex-direction:row','flex-row-reverse':'flex-direction:row-reverse','flex-wrap':'flex-wrap:wrap',
 'flex-1':'flex:1 1 0%','items-center':'align-items:center','items-start':'align-items:flex-start',
 'items-baseline':'align-items:baseline','items-stretch':'align-items:stretch',
 'justify-between':'justify-content:space-between','justify-center':'justify-content:center',
 'justify-start':'justify-content:flex-start','self-center':'align-self:center','shrink-0':'flex-shrink:0',
 'text-center':'text-align:center','text-left':'text-align:left','text-right':'text-align:right',
 'italic':'font-style:italic','not-italic':'font-style:normal','uppercase':'text-transform:uppercase',
 'font-medium':'font-weight:500','font-semibold':'font-weight:600','underline':'text-decoration-line:underline',
 'overflow-hidden':'overflow:hidden','overflow-x-auto':'overflow-x:auto','whitespace-nowrap':'white-space:nowrap',
 'object-cover':'object-fit:cover','object-contain':'object-fit:contain','object-center':'object-position:center',
 'object-top':'object-position:top','cursor-pointer':'cursor:pointer','list-disc':'list-style-type:disc',
 'list-none':'list-style-type:none','border-collapse':'border-collapse:collapse','border-dashed':'border-style:dashed',
 'invisible':'visibility:hidden','visible':'visibility:visible','align-middle':'vertical-align:middle',
 'align-top':'vertical-align:top','resize-y':'resize:vertical','min-w-0':'min-width:0px','h-auto':'height:auto',
 'w-auto':'width:auto','h-full':'height:100%','w-full':'width:100%','mx-auto':'margin-left:auto;margin-right:auto',
 'inset-0':'top:0px;right:0px;bottom:0px;left:0px','left-0':'left:0px','right-0':'right:0px','top-0':'top:0px',
 'top-full':'top:100%','z-50':'z-index:50','min-h-screen':'min-height:100vh','aspect-square':'aspect-ratio:1/1',
 'backdrop-blur-sm':'backdrop-filter:blur(4px)',
 'drop-shadow-lg':'filter:drop-shadow(0 10px 8px rgb(0 0 0/.04)) drop-shadow(0 4px 3px rgb(0 0 0/.1))',
 'shadow-sm':'box-shadow:0 1px 2px 0 rgb(0 0 0/.05)',
 'shadow-lg':'box-shadow:0 10px 15px -3px rgb(0 0 0/.1),0 4px 6px -4px rgb(0 0 0/.1)',
 'transition':'transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter;'+TRANS,
 'transition-all':'transition-property:all;'+TRANS,
 'transition-colors':'transition-property:color,background-color,border-color,text-decoration-color,fill,stroke;'+TRANS,
 'transition-opacity':'transition-property:opacity;'+TRANS,
 'transition-transform':'transition-property:transform;'+TRANS,
 'border':'border-width:1px','border-b':'border-bottom-width:1px','border-b-2':'border-bottom-width:2px',
 'border-t':'border-top-width:1px','border-l-2':'border-left-width:2px','border-l-4':'border-left-width:4px',
 'border-r-2':'border-right-width:2px','order-1':'order:1','order-2':'order:2',
 'scroll-mt-28':'scroll-margin-top:7rem','rotate-180':'transform:rotate(180deg)','h-px':'height:1px',
 'outline-none':'outline:2px solid transparent;outline-offset:2px','border-0':'border-width:0px',
 'bg-gradient-to-t':'background-image:linear-gradient(to top,var(--tw-gradient-stops))',
 'sr-only':'position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;'
           'clip:rect(0,0,0,0);white-space:nowrap;border-width:0',
}

def hexa(c, o=None):
    if o is None: return c
    c = c.lstrip('#')
    r, g, b = int(c[0:2],16), int(c[2:4],16), int(c[4:6],16)
    return 'rgb(%d %d %d / %s)' % (r, g, b, o)

def color(tok):
    m = re.match(r'^\[(#[0-9a-fA-F]{6})\](?:/(\d+))?$', tok)
    if m: return hexa(m.group(1), int(m.group(2))/100 if m.group(2) else None)
    if tok == 'white': return '#fff'
    if tok == 'black': return '#000'
    m = re.match(r'^(white|black)/(\d+)$', tok)
    if m: return 'rgb(%s / %s)' % ('255 255 255' if m.group(1)=='white' else '0 0 0', int(m.group(2))/100)
    m = re.match(r'^gray-(\d+)$', tok)
    if m and m.group(1) in GRAY: return GRAY[m.group(1)]
    return None

def size(tok):
    if tok in SP: return SP[tok]
    if tok in FRAC: return FRAC[tok]
    m = re.match(r'^\[([^\]]+)\]$', tok)
    if m: return m.group(1)
    if tok == 'screen': return '100vh'
    if tok == 'full': return '100%'
    return None

def decl(c):
    if c in SIMPLE: return SIMPLE[c]
    m = re.match(r'^opacity-(\d+)$', c)
    if m: return 'opacity:%s' % (int(m.group(1))/100)
    m = re.match(r'^(-?)(m|p)([tblrxy]?)-(.+)$', c)
    if m:
        neg, kind, side, val = m.groups()
        v = size(val)
        if v is None: return None
        if neg: v = '-' + v
        prop = 'margin' if kind == 'm' else 'padding'
        sides = {'':[''],'t':['-top'],'b':['-bottom'],'l':['-left'],'r':['-right'],
                 'x':['-left','-right'],'y':['-top','-bottom']}[side]
        return ';'.join('%s%s:%s' % (prop, s, v) for s in sides)
    m = re.match(r'^(w|h)-(.+)$', c)
    if m:
        v = size(m.group(2))
        if v: return ('width' if m.group(1)=='w' else 'height') + ':' + v
    m = re.match(r'^max-w-(.+)$', c)
    if m:
        t = m.group(1)
        if t in MAXW: return 'max-width:' + MAXW[t]
        v = size(t)
        if v: return 'max-width:' + v
    m = re.match(r'^(max-h|min-h|min-w)-(.+)$', c)
    if m:
        v = size(m.group(2))
        if v: return {'max-h':'max-height','min-h':'min-height','min-w':'min-width'}[m.group(1)] + ':' + v
    m = re.match(r'^gap(?:-(x|y))?-(.+)$', c)
    if m:
        v = size(m.group(2))
        if v: return {None:'gap','x':'column-gap','y':'row-gap'}[m.group(1)] + ':' + v
    m = re.match(r'^text-(.+)$', c)
    if m:
        t = m.group(1)
        if t in FS: return 'font-size:%s;line-height:%s' % FS[t]
        mm = re.match(r'^\[(\d+px)\]$', t)
        if mm: return 'font-size:%s;line-height:1' % mm.group(1)
        col = color(t)
        if col: return 'color:' + col
    for pre, prop in (('bg','background-color'), ('border','border-color')):
        m = re.match(r'^%s-(.+)$' % pre, c)
        if m:
            col = color(m.group(1))
            if col: return '%s:%s' % (prop, col)
    m = re.match(r'^placeholder-(.+)$', c)
    if m:
        col = color(m.group(1))
        if col: return ('PLACEHOLDER', 'color:' + col)
    m = re.match(r'^divide-(.+)$', c)
    if m:
        if m.group(1) == 'y': return ('DIVIDE', 'border-top-width:1px;border-bottom-width:0px')
        col = color(m.group(1))
        if col: return ('DIVIDE', 'border-color:' + col)
    m = re.match(r'^accent-\[(#[0-9a-fA-F]{6})\]$', c)
    if m: return 'accent-color:' + m.group(1)
    m = re.match(r'^(from|via|to)-(.+)$', c)
    if m:
        k, col = m.group(1), color(m.group(2))
        if col:
            if k == 'from': return '--tw-gradient-from:%s;--tw-gradient-stops:var(--tw-gradient-from),var(--tw-gradient-to,rgb(0 0 0/0))' % col
            if k == 'via':  return '--tw-gradient-stops:var(--tw-gradient-from),%s,var(--tw-gradient-to,rgb(0 0 0/0))' % col
            return '--tw-gradient-to:' + col
    m = re.match(r'^rounded(?:-(.+))?$', c)
    if m:
        t = m.group(1) or ''
        if t in ROUND: return 'border-radius:' + ROUND[t]
    m = re.match(r'^leading-(.+)$', c)
    if m:
        t = m.group(1)
        if t in LEAD: return 'line-height:' + LEAD[t]
        mm = re.match(r'^\[([\d.]+)\]$', t)
        if mm: return 'line-height:' + mm.group(1)
    m = re.match(r'^tracking-(.+)$', c)
    if m:
        t = m.group(1)
        if t in TRACK: return 'letter-spacing:' + TRACK[t]
        mm = re.match(r'^\[([^\]]+)\]$', t)
        if mm: return 'letter-spacing:' + mm.group(1)
    m = re.match(r'^aspect-\[(\d+)/(\d+)\]$', c)
    if m: return 'aspect-ratio:%s/%s' % m.groups()
    if c == 'aspect-auto': return 'aspect-ratio:auto'
    m = re.match(r'^grid-cols-(\d+)$', c)
    if m: return 'grid-template-columns:repeat(%s,minmax(0,1fr))' % m.group(1)
    m = re.match(r'^col-span-(\d+)$', c)
    if m: return 'grid-column:span %s/span %s' % (m.group(1), m.group(1))
    m = re.match(r'^space-(x|y)-(.+)$', c)
    if m:
        v = size(m.group(2))
        if v: return ('SPACE', m.group(1), v)
    return None

def esc(c):
    return re.sub(r'([:\[\]#/\.%\(\)])', r'\\\1', c)

def rules_for(c, sel_prefix='', sel_suffix=''):
    """restituisce le regole css per la classe c, con eventuale prefisso/suffisso di selettore"""
    d = decl(c)
    if d is None: return None
    base = sel_prefix + '.' + esc(FULL[c]) + sel_suffix
    if isinstance(d, tuple):
        if d[0] == 'PLACEHOLDER': return ['%s::placeholder{%s}' % (base, d[1])]
        if d[0] == 'DIVIDE':      return ['%s>:not([hidden])~:not([hidden]){%s}' % (base, d[1])]
        if d[0] == 'SPACE':
            prop = 'margin-left' if d[1] == 'x' else 'margin-top'
            return ['%s>:not([hidden])~:not([hidden]){%s:%s}' % (base, prop, d[2])]
    return ['%s{%s}' % (base, d)]

PREFLIGHT = """*,::before,::after{box-sizing:border-box;border-width:0;border-style:solid;border-color:#e5e7eb}
::before,::after{--tw-content:''}
html{line-height:1.5;-webkit-text-size-adjust:100%;tab-size:4;font-family:ui-sans-serif,system-ui,sans-serif}
body{margin:0;line-height:inherit}
hr{height:0;color:inherit;border-top-width:1px}
abbr:where([title]){text-decoration:underline dotted}
h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit;margin:0}
a{color:inherit;text-decoration:inherit}
b,strong{font-weight:bolder}
code,kbd,samp,pre{font-family:ui-monospace,monospace;font-size:1em}
small{font-size:80%}
sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}
sub{bottom:-.25em}sup{top:-.5em}
table{text-indent:0;border-color:inherit;border-collapse:collapse}
button,input,optgroup,select,textarea{font-family:inherit;font-size:100%;font-weight:inherit;line-height:inherit;color:inherit;margin:0;padding:0}
button,select{text-transform:none}
button,[type='button'],[type='reset'],[type='submit']{-webkit-appearance:button;background-color:transparent;background-image:none}
:-moz-focusring{outline:auto}
progress{vertical-align:baseline}
summary{display:list-item}
blockquote,dl,dd,h1,h2,h3,h4,h5,h6,hr,figure,p,pre{margin:0}
fieldset{margin:0;padding:0}
legend{padding:0}
ol,ul,menu{list-style:none;margin:0;padding:0}
textarea{resize:vertical}
input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}
button,[role="button"]{cursor:pointer}
:disabled{cursor:default}
img,svg,video,canvas,audio,iframe,embed,object{display:block;vertical-align:middle}
img,video{max-width:100%;height:auto}
[hidden]{display:none}"""

# ---- raccolta classi ----
FULL = {}
found = set()
for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True):
    for attr in re.findall(r'class="([^"]*)"', open(f, encoding='utf-8').read()):
        found.update(attr.split())

out, unknown = [], []
base_rules, resp_rules, state_rules = [], {k: [] for k in BP}, []

STATE_SEL = {'hover':':hover','focus':':focus','last':':last-child','first':':first-child'}

for c in sorted(found):
    if c in CUSTOM: continue
    m = re.match(r'^(sm|md|lg|xl|hover|focus|group-hover|last|first|group-open):(.+)$', c)
    if m:
        variant, bare = m.groups()
        FULL[bare] = c
        if variant in BP:
            r = rules_for(bare)
            if r: resp_rules[variant].extend(r); continue
        elif variant == 'group-hover':
            r = rules_for(bare, sel_prefix='.group:hover ')
            if r: state_rules.extend(r); continue
        elif variant == 'group-open':
            r = rules_for(bare, sel_prefix='.group[open] ')
            if r: state_rules.extend(r); continue
        else:
            r = rules_for(bare, sel_suffix=STATE_SEL[variant])
            if r: state_rules.extend(r); continue
        unknown.append(c); continue
    FULL[c] = c
    r = rules_for(c)
    if r: base_rules.extend(r)
    else: unknown.append(c)

css = ['/* Tailwind statico — generato dalle sole classi usate dal sito. Rigenerare dopo ogni modifica al markup. */',
       PREFLIGHT, '']
css += base_rules
for bpname in ('sm', 'md', 'lg', 'xl'):
    if resp_rules[bpname]:
        css.append('@media (min-width:%s){%s}' % (BP[bpname], ''.join(resp_rules[bpname])))
css += state_rules

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write('\n'.join(css) + '\n')

print('classi trovate      :', len(found))
print('regole generate     :', len(base_rules) + sum(len(v) for v in resp_rules.values()) + len(state_rules))
print('dimensione          :', os.path.getsize(OUT) // 1024, 'KB')
print('NON RICONOSCIUTE    :', len(unknown))
for u in unknown: print('   ', u)
