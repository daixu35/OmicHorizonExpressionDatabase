import re

from django.shortcuts import render
from django.db import connection

colors = ["#60caeb", "#09d837", "#b362ac", "#b1a41d", "#5a2fc4", "#a6df8c", "#452ad1", "#42d4c8", "#91022d", "#1dbe2c",
          "#9fd70e", "#5c98bb", "#e6fb86", "#311b10", "#b4d650", "#e0e8ec", "#9cbba9", "#fdeda8", "#4bd116", "#8fe4e0",
          "#6d522c", "#583d9f", "#6e6f05", "#da130e", "#adf6d8", "#69951c", "#55894c", "#68a724", "#27fab7", "#575212",
          "#16f9b2", "#cf6917", "#313942", "#74bbb2", "#c9acf5", "#e079a2", "#98ae86", "#8c566b", "#9d7a7d", "#abcf84",
          "#d1d4d8", "#c6a2f3", "#c50292", "#5da287", "#b2ac88", "#1d058e", "#4d6b03", "#02da22", "#2821ca", "#29df21",
          "#567ea8", "#412a6e", "#454537", "#c0b070", "#98fb7f", "#5d63db", "#0e5d82", "#9900fe", "#325641", "#981647",
          "#7a9f91", "#b05f56", "#a21f5d", "#45e52e", "#b429a4", "#380e77", "#b16749", "#211c7c", "#c5745e", "#53bf40",
          "#991b30", "#6f9ee6", "#4eddab", "#e16579", "#c9de7d", "#07652b", "#e8a56a", "#355f38", "#569655", "#2af880",
          "#c31b2d", "#024ad2", "#dce160", "#cabf81", "#d1c621", "#152e71", "#8a61ec", "#5c95da", "#d1b52b", "#762fa5",
          "#51a043", "#9f30e5", "#860642", "#a54ec9", "#cbd9ce", "#a1735e", "#4c8ff9", "#f76063", "#2e1377", "#e99170",
          "#eda5df", "#06b9f7", "#e2580f", "#895b4c", "#d748e1", "#f9f87b", "#7d53c5", "#c2a149", "#576ea1", "#50c168",
          "#c387b9", "#5a96a9", "#6dbfbf", "#4c7068", "#5daa10", "#58a03b", "#58a03b", "#58a03b", "#9b6e0c", "#c9d8d2",
          "#067d0b", "#bc50d2", "#12b30c", "#67b2a7", "#c0853d", "#a44733", "#3076b2", "#adb634", "#11b6e4", "#52280f",
          "#60caeb", "#09d837", "#b362ac", "#b1a41d", "#5a2fc4", "#a6df8c", "#452ad1", "#42d4c8", "#91022d", "#1dbe2c",
          "#9fd70e", "#5c98bb", "#e6fb86", "#311b10", "#b4d650", "#e0e8ec", "#9cbba9", "#fdeda8", "#4bd116", "#8fe4e0",
          "#6d522c", "#583d9f", "#6e6f05", "#da130e", "#adf6d8", "#69951c", "#55894c", "#68a724", "#27fab7", "#575212",
          "#16f9b2", "#cf6917", "#313942", "#74bbb2", "#c9acf5", "#e079a2", "#98ae86", "#8c566b", "#9d7a7d", "#abcf84",
          "#d1d4d8", "#c6a2f3", "#c50292", "#5da287", "#b2ac88", "#1d058e", "#4d6b03", "#02da22", "#2821ca", "#29df21",
          "#567ea8", "#412a6e", "#454537", "#c0b070", "#98fb7f", "#5d63db", "#0e5d82", "#9900fe", "#325641", "#981647",
          "#7a9f91", "#b05f56", "#a21f5d", "#45e52e", "#b429a4", "#380e77", "#b16749", "#211c7c", "#c5745e", "#53bf40",
          "#991b30", "#6f9ee6", "#4eddab", "#e16579", "#c9de7d", "#07652b", "#e8a56a", "#355f38", "#569655", "#2af880",
          "#c31b2d", "#024ad2", "#dce160", "#cabf81", "#d1c621", "#152e71", "#8a61ec", "#5c95da", "#d1b52b", "#762fa5",
          "#51a043", "#9f30e5", "#860642", "#a54ec9", "#cbd9ce", "#a1735e", "#4c8ff9", "#f76063", "#2e1377", "#e99170",
          "#eda5df", "#06b9f7", "#e2580f", "#895b4c", "#d748e1", "#f9f87b", "#7d53c5", "#c2a149", "#576ea1", "#50c168",
          "#c387b9", "#5a96a9", "#6dbfbf", "#4c7068", "#5daa10", "#58a03b", "#58a03b", "#58a03b", "#9b6e0c", "#c9d8d2",
          "#067d0b", "#bc50d2", "#12b30c", "#67b2a7", "#c0853d", "#a44733", "#3076b2", "#adb634", "#11b6e4", "#52280f",
          "#60caeb", "#09d837", "#b362ac", "#b1a41d", "#5a2fc4", "#a6df8c", "#452ad1", "#42d4c8", "#91022d", "#1dbe2c",
          "#9fd70e", "#5c98bb", "#e6fb86", "#311b10", "#b4d650", "#e0e8ec", "#9cbba9", "#fdeda8", "#4bd116", "#8fe4e0",
          "#6d522c", "#583d9f", "#6e6f05", "#da130e", "#adf6d8", "#69951c", "#55894c", "#68a724", "#27fab7", "#575212",
          "#16f9b2", "#cf6917", "#313942", "#74bbb2", "#c9acf5", "#e079a2", "#98ae86", "#8c566b", "#9d7a7d", "#abcf84",
          "#d1d4d8", "#c6a2f3", "#c50292", "#5da287", "#b2ac88", "#1d058e", "#4d6b03", "#02da22", "#2821ca", "#29df21",
          "#567ea8", "#412a6e", "#454537", "#c0b070", "#98fb7f", "#5d63db", "#0e5d82", "#9900fe", "#325641", "#981647",
          "#7a9f91", "#b05f56", "#a21f5d", "#45e52e", "#b429a4", "#380e77", "#b16749", "#211c7c", "#c5745e", "#53bf40",
          "#991b30", "#6f9ee6", "#4eddab", "#e16579", "#c9de7d", "#07652b", "#e8a56a", "#355f38", "#569655", "#2af880",
          "#c31b2d", "#024ad2", "#dce160", "#cabf81", "#d1c621", "#152e71", "#8a61ec", "#5c95da", "#d1b52b", "#762fa5",
          "#51a043", "#9f30e5", "#860642", "#a54ec9", "#cbd9ce", "#a1735e", "#4c8ff9", "#f76063", "#2e1377", "#e99170",
          "#eda5df", "#06b9f7", "#e2580f", "#895b4c", "#d748e1", "#f9f87b", "#7d53c5", "#c2a149", "#576ea1", "#50c168",
          "#c387b9", "#5a96a9", "#6dbfbf", "#4c7068", "#5daa10", "#58a03b", "#58a03b", "#58a03b", "#9b6e0c", "#c9d8d2",
          "#067d0b", "#bc50d2", "#12b30c", "#67b2a7", "#c0853d", "#a44733", "#3076b2", "#adb634", "#11b6e4", "#52280f"]


def seach_home(request):
    return render(request, "immusubset.html")


def update(request):
    return render(request, "update.html")


def contact(request):
    return render(request, "contact.html")


def contactSuccess(request):
    params = request.POST
    db_cursor = connection.cursor()
    feedbackName = "'" + params["suggestName"] + "'"
    feedbackMail = "'" + params["suggestE-mail"] + "'"
    feedback = "'" + params["suggestion"] + "'"
    sql = "insert into feedback values (%s, %s, %s)" % (feedbackName, feedbackMail, feedback)
    db_cursor.execute(sql)

    return render(request, "contactSuccess.html")


def FAQ(request):
    return render(request, "FAQ.html")


def result(request):
    # initial value
    params = request.POST
    query_field_ = ""
    query_subfield_ = ""
    query_field = ""

    # get value from HTML
    query_value = "'" + params["gene_name"] + "'"
    query_type_ = params["first"]
    if query_type_ != "All":
        if query_type_ == "CellLine":
            query_field_ = request.POST.getlist(query_type_, [])
        else:
            query_field_ = params[query_type_]
            query_field = "'" + query_field_ + "'"
            if query_field_ != "All":
                query_subfield_ = request.POST.getlist(query_field_, [])

    # search
    if query_type_ == "PrimaryCell":
        query_type_ = "Primary Cell"
    if query_type_ == "CellLine":
        query_type_ = "Cell line"
    query_type = "'" + query_type_ + "'"
    db_cursor = connection.cursor()
    sql = "select * from geneinfo where geneid=%s or genesymbol=%s or NCBI_geneid = %s or genesynonym=%s" \
          % (query_value, query_value, query_value, query_value)
    db_cursor.execute(sql)
    rows = db_cursor.fetchone()

    if not rows:
        sql = "select geneid from genesynonymtable where first = %s or second=%s or third=%s or fourth=%s or " \
              "fifth=%s or sixth=%s or seventh=%s or eighth=%s or ninth=%s or tenth=%s or eleventh=%s or twelfth=%s or " \
              "thirteenth=%s or fourteenth=%s or fifteenth=%s" % \
              (query_value, query_value, query_value, query_value, query_value, query_value, query_value, query_value,
               query_value, query_value, query_value, query_value, query_value, query_value, query_value)
        db_cursor.execute(sql)
        thegeneid = db_cursor.fetchone()
        if thegeneid:
            sql = "select * from geneinfo where geneid=%s" % ("'" + thegeneid[0] + "'")
            db_cursor.execute(sql)
            rows = db_cursor.fetchone()
    if rows:
        query_value = "'" + rows[0] + "'"

    context = {}
    if not rows:  # no result HTML
        context = {"search_name": params["gene_name"]}
        return render(request, "no result.html", context=context)
    else:  # the result HTML
        context["search_name"] = params["gene_name"]
        context["gene_symbol"] = rows[1]
        context["gene_description"] = rows[3]
        context["gene_synonym"] = rows[2]
        context["Ensemble_gene_id"] = rows[0]
        context["NCBI_gene_id"] = rows[4]
        context["NCBI_gene_biotype"] = rows[5]
        context["chromosome"] = rows[6]
        context["map_location"] = rows[7]
        context["chromosome_localization"] = rows[8]
        context["strand"] = rows[9]

        if query_type_ == "Cell line":
            sql = "select type,field,subfield,value from expressioninfo where type=%s and geneid=%s" \
                  % (query_type, query_value)
            i = 0
            reCellLine = r"[a-z0-9A-Z-]+"
            for field in query_field_:
                field = re.search(reCellLine, field).group()
                i += 1
                if i == 1:
                    sql += " and ("
                    field = "'" + field + "'"
                    sql = sql + "field=" + field
                else:
                    sql += " or "
                    field = "'" + field + "'"
                    sql = sql + "field=" + field
            sql += ")"
        else:
            if query_type_ == 'All':
                sql = "select type,field,subfield,value from expressioninfo where geneid=%s" % (query_value,)
            elif query_field_ == 'All':
                sql = "select type,field,subfield,value from expressioninfo where type=%s and geneid=%s" % \
                      (query_type, query_value)
            else:
                sql = "select type,field,subfield,value from expressioninfo where type=%s and field=%s and geneid=%s" \
                      % (query_type, query_field, query_value)
                i = 0
                for subfield in query_subfield_:
                    i += 1
                    if i == 1:
                        sql += " and ("
                        subfield = "'" + subfield + "'"
                        sql = sql + "subfield=" + subfield
                    else:
                        sql += " or "
                        subfield = "'" + subfield + "'"
                        sql = sql + "subfield=" + subfield
                sql += ")"

        db_cursor.execute(sql)
        plot = db_cursor.fetchall()
        plotLegends = []
        tableLegends = []
        plotColors = []
        legendColors = {}
        values = []
        abnormalValue = []

        i = -1
        tempDict = {}
        plot = sorted(plot, reverse=True)
        for temp in plot:
            i += 1
            legendDict = {}
            legendDict["legendIndex"] = i
            legendDict["legendType"] = temp[0]
            legendDict["legendsubType"] = temp[1]
            legendDict["legendfinalType"] = temp[2]
            tempStrList = temp[3]
            legendDict["legendValue"] = tempStrList
            tempList = tempStrList.split(",")
            valueList = []
            for tempValue in tempList:
                tempValue = float(tempValue)
                valueList.append(tempValue)
            valueBoxParam = getBoxValue(valueList)
            abnormalBoxParam = getBoxAbnormalValue(i, valueList)
            theMedian = medianValue(valueList)
            legendDict["medianValue"] = theMedian
            for boxParam in abnormalBoxParam:
                abnormalValue.append(boxParam)
            values.append(valueBoxParam)

            if temp[0] == "Cell line":
                if query_type_ == "All":
                    legendName = str(temp[0] + ", " + temp[1])
                    plotLegends.append(legendName)
                else:
                    legendName = temp[1]
                    plotLegends.append(legendName)
            else:
                if query_type_ == "All":
                    legendName = str(temp[0] + ", " + temp[1] + ", " + temp[2])
                    plotLegends.append(legendName)
                elif query_field_ == "All":
                    legendName = str(temp[1] + ", " + temp[2])
                    plotLegends.append(legendName)
                else:
                    legendName = str(temp[2])
                    plotLegends.append(legendName)

            typeField = str(temp[0] + ", " + temp[1])
            if not tempDict.get(typeField):
                tempDict[typeField] = colors[i]
            legendColors[legendName] = tempDict[typeField]
            plotColors.append(tempDict[typeField])
            tableLegends.append(legendDict)

        stepSize = 1
        stepSizeRegular = int(i / 50)
        if stepSizeRegular > 1:
            stepSize = stepSizeRegular + 1

        context["stepSize"] = stepSize
        context["tableLegends"] = tableLegends
        context["plotLegends"] = plotLegends
        context["plotColors"] = plotColors
        context["legendColors"] = legendColors
        context["values"] = values
        context["abnormalValue"] = abnormalValue
        return render(request, "result.html", context=context)


def maxValue(tempList):
    theMax = max(tempList)
    theQ3 = Q3Value(tempList)
    theQ1 = Q1Value(tempList)
    IQR = theQ3 - theQ1
    upper = theQ3 + 1.5 * IQR
    if upper <= theMax:
        return upper
    return theMax


def minValue(tempList):
    theMin = min(tempList)
    theQ3 = Q3Value(tempList)
    theQ1 = Q1Value(tempList)
    IQR = theQ3 - theQ1
    lower = theQ1 - 1.5 * IQR
    if lower >= theMin:
        return lower
    return theMin


def medianValue(tempList):
    tempList.sort()
    n = len(tempList)
    n = int((n + 1) / 2)
    return tempList[n - 1]


def Q3Value(tempList):
    n = len(tempList)
    n = int((3 * (n + 1)) / 4)
    return tempList[n - 1]


def Q1Value(tempList):
    n = len(tempList)
    n = int((n + 1) / 4)
    return tempList[n - 1]


def getBoxValue(tempList):
    boxValue = []
    tempList.sort()
    theMax = maxValue(tempList)
    theMin = minValue(tempList)
    theMedian = medianValue(tempList)
    theQ3 = Q3Value(tempList)
    theQ1 = Q1Value(tempList)
    boxValue.append(theMin)
    boxValue.append(theQ1)
    boxValue.append(theMedian)
    boxValue.append(theQ3)
    boxValue.append(theMax)
    return boxValue


def getBoxAbnormalValue(index, tempList):
    abnormalBoxValue = []
    tempList.sort()
    theMin = minValue(tempList)
    theMax = maxValue(tempList)
    for tempValue in tempList:
        if tempValue <= theMin or tempValue >= theMax:
            abnormalBoxValue.append([index, tempValue])
    return abnormalBoxValue
