import urllib.parse

template = """<div class="file-item">
            <a href="Mini%20test%20sylabus.pdf" class="file-item-name">
            <div class="file-item-select-bg bg-primary"></div>
            <div class="file-item-icon far fa-file-pdf text-secondary"></div>
                Mini test sylabus.pdf
            </a>
            <div class="file-item-actions btn-group">
                <button type="button" class="btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle" data-toggle="dropdown"><i class="ion ion-ios-more"></i></button>
                <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="Mini%20test%20sylabus.pdf" download>Download</a>
                </div>
            </div>
        </div>"""
content = ["Ancient and Medieval History.pdf","Ancient and Medieval History recorded.pdf","Additional Science.pdf","Biology.pdf","Disaster Management.pdf","Ecology and Environment.pdf" ,"Economics.pdf","Economics PG.pdf","Ethics.pdf","Ethics JG.pdf","Ethics Case Study.pdf","Ethics recorded.pdf","Ethics JG recorded.pdf","Ethics Case Study recorded.pdf","Geography.pdf","Map.pdf","Map recorded.pdf","History of Modern India.pdf","International Relation.pdf","Polity.pdf","Governance.pdf","Post Independence India.pdf","Post Independence India recorded.pdf","Science and Technology.pdf","Security.pdf","Social Change in Modern Society.pdf","World History.pdf"]

for c in content:
    print("""        <div class="file-item">
            <a href=\"""" + urllib.parse.quote(c) + """" class="file-item-name">
            <div class="file-item-select-bg bg-primary"></div>
            <div class="file-item-icon far fa-file-pdf text-secondary"></div>
                """ + c + """
            </a>
            <div class="file-item-actions btn-group">
                <button type="button" class="btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle" data-toggle="dropdown"><i class="ion ion-ios-more"></i></button>
                <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href=\"""" + urllib.parse.quote(c) + """" download>Download</a>
                </div>
            </div>
        </div>""")