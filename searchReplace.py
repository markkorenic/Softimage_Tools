from win32com.client import constants as c

xsi=Application
log = LogMessage


def searchAndReplace():
#add ui
    prop = xsi.ActiveSceneRoot.AddProperty('CustomProperty',False, "SearchAndReplace" )
    #create search and replace textfields
    search_par = prop.AddParameter3("Search", c.siString)
    replace_par = prop.AddParameter3("Replace", c.siString)

    canceled = xsi.InspectObj(prop, "", "SearchAndReplace", c.siModal, False)
    search  = search_par.Value
    replace = replace_par.Value
    xsi.DeleteObj(prop)
    if cancelled:
        return

    if obj in xsi.Selection:
        obj.Name = obj.Name.replace( search, replace)
