import jinja2

switch_vars = {
    'host_name': 'leaf1',
    'domain_name':'ntc.com',
    'apache': False,
    'vlans1': {
        '10': 'web',
        '20': 'app',
        '30': 'db'
        },
    'vlans2': {
        '10': 'web',
        '20': 'app',
        '30': 'db',
        '40': 'apache server'
        },
}

#Read jinja2 template file
switch_template_file = 'switch_tmpl_conditional.j2'
with open(switch_template_file) as f:
   switch_templ = f.read()

#Render template file and print
templ = jinja2.Template(switch_templ)
ren_templ = templ.render(switch_vars)
print(ren_templ)