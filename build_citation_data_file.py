import pysparql_anything as pysa
import os
import yaml

config = yaml.load(open('_config.yml','r'), Loader=yaml.Loader)
namespace = config['rdf']['namespace']
engine = pysa.SparqlAnything()
directory = './content/'
includes = './_includes/cite/'
for root, dirs, files in os.walk(directory):
    for filename in files:
        if not filename.endswith('.md'):
            continue
        location = os.path.join(root, filename)
        if "/.github/" in location:
            continue
        #print(location)
        pre, ext = os.path.splitext(location)
        output_includes = pre.replace("./content/", includes)
        output_includes_apa = output_includes + ".cite.apa"
        output_includes_bib = output_includes + ".cite.bib"
        #pth = os.path.dirname(os.path.abspath(output))
        pth_includes = os.path.dirname(os.path.abspath(output_includes))
        #if not os.path.exists(pth):
        #    os.makedirs(pth)
        if not os.path.exists(pth_includes):
            os.makedirs(pth_includes)
        d = engine.select(q='./component-citation.sparql', v={'componentFile': location}) #
        if len(d['results']['bindings']) == 0 or 'component' not in d['results']['bindings'][0]:
            continue
        if 'apa' in d['results']['bindings'][0]:
            apa = d['results']['bindings'][0]['apa']['value']
            f1 = open(output_includes_apa, 'w')
            f1.write(apa)

        if 'bibtex' in d['results']['bindings'][0]:
            bibtex = d['results']['bindings'][0]['bibtex']['value']
            f1 = open(output_includes_bib, 'w')
            f1.write(bibtex)

