from win32com.client import constants as c

xsi= Application
log = xsi.LogMessage


def searchAndReplace():
    """UI for search and replace object strings"""
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
    #if there are objects selected, replace them with new string
    if obj in xsi.Selection:
        obj.Name = obj.Name.replace( search, replace)
