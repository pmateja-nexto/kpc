#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      noisy
#
# Created:     31-07-2012
# Copyright:   (c) noisy 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from jinja2 import Environment, PackageLoader
from jinja2 import FileSystemLoader
from jinja2.runtime import Context


project_path='../Templates/eKundelek_mag1/'
opf_file='ekundelek_utf8_without_BOM.opf'

def main():

    env = Environment()
    loader = FileSystemLoader(project_path)

    template = loader.load(env, opf_file)
    #print template.render(name='noisy')

    #ctx = Context(loadContext());

    #d = {'unique_identifier':'test', 'dc_title':'title_test', 'dc_lang':'lang_test'}
    d = loadContext()

    ctx = Context(env, blocks=d, name=opf_file, parent=env.globals)

    strim = template.stream(**d)  #unique_identifier='test', dc_title='title_test', dc_lang='lang_test') #jak dzia?a ** ?
    strim.dump(project_path+'ekundelek_gen.opf')

    print 'Gotowe!'
    pass

def loadContext():

    dict = {}
    with open(project_path+"context.txt") as f:
        for line in f:
            (key, val) = line.split('=')
            dict[key.strip()] = val.strip()

    dict['item_list'] = [{'id':'id_test', 'mimetype':'application/xhtml+xml', 'href':'file.html'},
                        {'id':'id_test', 'mimetype':'application/xhtml+xml', 'href':'file.html'}]
    return dict

if __name__ == '__main__':
    main()
