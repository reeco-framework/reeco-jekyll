---
component-id: licences
name: Licences Knowlegde Graph
description: Resources for the Polifonia Licences KG, containing licence information of the resources from third-parties that the project reused.
type: Software
release-date: 28/04/2023
release-number: v0.3
work-package: 
- WP2
licence: Public domain, https://unlicense.org
doi: 10.5281/zenodo.7875034
links:
credits:
- https://github.com/enridaga
- https://github.com/jasemk
- Marco Gurrieri
---
# Polifonia Licences KG

This project includes resources for the Polifonia Licences KG, containing licence information of the resources from third-parties that the project reused.

In what follows, fx refers to the following command line `java -jar sparql-anything-<version>-.jar`.
	
## Download licence descriptions from Dalicc
We reuse a catalogue of machine readable licences from the [Dalicc project](https://www.dalicc.net/).

```
fx -q queries/harvest-dalicc.sparql -f TTL -o knowledgegraph/dalicc.ttl
```

## Knowledge Graph Construction

### Generate `datasets-licences.ttl`
From the spreadhseet in `data/` to the RDF file.

```
fx -q queries/kg.sparql -f TTL -o knowledgegraph/datasets-licences.ttl
```

### Views

```
fx -q queries/terms-view.sparql -l knowledgegraph/
```

### Stats

```
fx -q queries/datasets-by-licence.sparql -l knowledgegraph/

fx -q queries/terms-stats.sparql -l knowledgegraph/
```




