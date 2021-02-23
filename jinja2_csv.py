import jinja2
import csv

with open('switch_vars.csv') as f:
    read_csv = csv.DictReader(f)
    #s = read_csv[0]
    #print(s)
    for switch_vars in read_csv:
        vlan_ids = switch_vars['vlan_ids']
        vlan_ids = vlan_ids.split()
        switch_vars['vlan_ids'] = vlan_ids

        vlan_names = switch_vars['vlan_names']
        vlan_names = vlan_names.split()
        switch_vars['vlan_names'] = vlan_names

#Read jinja2 template file
switch_template_file = 'switch_tmpl_csv.j2'
with open(switch_template_file) as f:
   switch_templ = f.read()

#Render template file and print
templ = jinja2.Template(switch_templ)
ren_templ = templ.render(switch_vars)
print(ren_templ)