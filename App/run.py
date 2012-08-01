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
ncx_file='ekundelek_utf8_without_BOM.ncx'

def main():

    env = Environment()
    loader = FileSystemLoader(project_path)

    template_opf = loader.load(env, opf_file)
    template_ncx = loader.load(env, ncx_file)
    #print template_opf.render(name='noisy')

    #ctx = Context(loadContext());

    #d = {'unique_identifier':'test', 'dc_title':'title_test', 'dc_lang':'lang_test'}
    d = loadContext()

    ctx = Context(env, blocks=d, name=opf_file, parent=env.globals)

    template_opf.stream(**d).dump(project_path+'ekundelek_gen.opf')                            #unique_identifier='test', dc_title='title_test', dc_lang='lang_test') #jak dzia?a ** ?
    template_ncx.stream(**d).dump(project_path+'ekundelek_gen.ncx')
    #strim.dump(project_path+'ekundelek_gen.opf')

    print 'Gotowe!'
    pass

def loadContext():

    dict = {}
    with open(project_path+"context.txt") as f:
        for line in f:
            (key, val) = line.split('=')
            dict[key.strip()] = val.strip()

    dict['item_list'] = [{'id':'id_test', 'mimetype':'application/xhtml+xml', 'href':'file.html'},
                        {'id':'id_test', 'mimetype':'application/xhtml+xml', 'href':'file.html', 'no_linear':1}]

    dict['periodical'] = {'label':'eKundelek.pl', 'content_file':'content.html'}

    dict['section_list'] = [ {'id':'sid1', 'play_order':'1', 'label':'Artyku?y (od najnowszych)', 'description':'Artyku?y (od najnowszych)_desc', 'author':'Krzysztof Szumny', 'content_href_link':'art1'},
                             {'id':'sid2', 'play_order':'2', 'label':'Inne', 'description':'Inne_desc', 'author':'Magdalena Szumna', 'content_href_link':'art2'}]

    return dict

if __name__ == '__main__':
    main()
