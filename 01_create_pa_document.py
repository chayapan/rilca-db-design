'''
Created on Dec 12, 2018

@author: chayapan
'''

from pa_items import PAItem, PAGroup, PACategory, PAPart, PAClass, PAForm

if __name__ == '__main__':
    items = PAItem.loadFromWorkbook()
    print items
    
    
    for k, v in items.iteritems():
        p = v.findParent(items)
        # print v.id, p, v.parent
    
    # Roots
    roots = [p for i, p in items.iteritems() if p.parent == 'NULL' ]

    for r in roots:
        print r.desc_en
        print r.findChildren(items)
        # for c in r.findChildren(items):
        #     print c.desc_en
        #     for i in c.findChildren(items):
        #         print i.desc_en
    
    selectable_items = []
    for i, pa in items.iteritems():
        if pa.level == '3:itemClass':
            selectable_items.append(pa)
    print "Selectable:", len(selectable_items), selectable_items
    
    item_hierarchy = {}
    
    item_groups = []
    for i, pa in items.iteritems():
        if pa.level == '1:itemGroup':
            item_groups.append(pa)
    print "Groups:", len(item_groups), item_groups
    
    
    categories = PACategory.fromDictionary(items)
    groups = PAGroup.fromDictionary(items)
    classes = PAClass.fromDictionary(items)
    sections = PAPart.fromDictionary(items)
    
    print "Categories", len(categories)
    print "Group", len(groups)
    print "Sections", len(sections)
    print "Classes (Selectable)", len(classes)
    
    
    form = PAForm(items)
    form.print_items()