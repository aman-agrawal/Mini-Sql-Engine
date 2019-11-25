import sys,pandas,numpy,csv,re

def condfoo(conditions,df,table_name):
    conditions= "".join(conditions)
    
    #1a
    if conditions[1]=='=':
        comp=conditions.split("=")
        df=df[df[str(table_name+"."+conditions[0])]==int(comp[1])]
    #1b
    elif conditions[1]=='>' and conditions[2]!='=':
        comp=conditions.split(">")
        df=df[df[str(table_name+"."+conditions[0])]>int(comp[1])]
        
    #1c
    elif conditions[1]=='<' and conditions[2]!='=':
        comp=conditions.split("<")
        df=df[df[str(table_name+"."+conditions[0])]<int(comp[1])]
        
    #1d
    elif conditions[1]=='>' and conditions[2]=='=':
        comp=conditions.split(">=")
        df=df[df[str(table_name+"."+conditions[0])]>=int(comp[1])]
        
    #1e
    elif conditions[1]=='<' and conditions[2]=='=':
        comp=conditions.split("<=")
        df=df[df[str(table_name+"."+conditions[0])]<=int(comp[1])]
        
    return df

def condfooand(conditions,cond_1,cond_2,table_name,df):
      if len(cond_1[0])==1 and len(cond_2[0])==1:
          df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1])]
          df=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])]
            
      elif len(cond_2[0])==1 and cond_1[0][1]=='>' and conditions[0][2]!='=':
          compa=''.join(cond_1)
          comp=compa.split(">")
          df=df[df[str(table_name+"."+cond_1[0][0])]>int(comp[1])]
          df=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])] 
          
      elif len(cond_2[0])==1 and cond_1[0][1]=='<' and conditions[0][2]!='=' :
          compa=''.join(cond_1)
          comp=compa.split("<")
          df=df[df[str(table_name+"."+cond_1[0][0])]<int(comp[1])]
          df=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])] 
          
      elif len(cond_2[0])==1 and cond_1[0][1]=='>' and conditions[0][2]=='=':
          df=df[df[str(table_name+"."+cond_1[0][0])]>=int(cond_1[1])]
          df=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])] 
          
      elif len(cond_2[0])==1 and cond_1[0][1]=='<' and conditions[0][2]=='=':
          df=df[df[str(table_name+"."+cond_1[0][0])]<=int(cond_1[1])]
          df=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])] 
    #             -------------------------------------- 
      elif cond_2[0][1]=='>' and conditions[2][2]!='=' and len(cond_1[0])==1:
          compa=''.join(cond_2)
          comp=compa.split(">")
          df=df[df[str(table_name+"."+cond_2[0][0])]>int(comp[1])]
          df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1])] 
          
      elif cond_2[0][1]=='<' and conditions[2][2]!='=' and len(cond_1[0])==1:
          compa=''.join(cond_2)
          comp=compa.split("<")
          df=df[df[str(table_name+"."+cond_2[0][0])]<int(comp[1])]
          df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1])] 
          
      elif cond_2[0][1]=='>' and conditions[2][2]=='=' and len(cond_1[0])==1:
          df=df[df[str(table_name+"."+cond_2[0][0])]>=int(cond_2[1])]
          df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1])] 
          
      elif cond_2[0][1]=='<' and conditions[2][2]=='='  and len(cond_1[0])==1:
          df=df[df[str(table_name+"."+cond_2[0][0])]<=int(cond_2[1])]
          df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1])] 
    
      return df

def table_attr(table_name,metadata):

    with open(metadata, "r+") as fp1:
        data = fp1.readlines()
        string=""
        string = ''.join(data)
        string=string.split("\r\n")
    result = []
    i = string.index(table_name) + 1
   
    while string[i] != '<end_table>':
        result.append(table_name+"."+string[i])
        i+=1

#    print "result", required_list_of_attributes ['table1.A', 'table1.B', 'table1.C']
    return result


def aggregate(attr):
    all_functions = {'func_flag': 0, 'func':{'max':[], 'min':[], 'avg':[], 'sum':[], 'distinct':[]}}

    for i in attr:
        if re.match(r'max\((.+)\)', i, re.I) is not None:
            all_functions['func_flag'] = 1
            all_functions['func']['max'].append((re.match(r'max\((.+)\)', i, re.I)).group(1))
#                print all_functions['func']['max']

        if re.match(r'min\((.+)\)', i, re.I) is not None:
            all_functions['func_flag'] = 1
            all_functions['func']['min'].append((re.match(r'min\((.+)\)', i, re.I)).group(1))

        if re.match(r'avg\((.+)\)', i, re.I) is not None:
            all_functions['func_flag'] = 1
            all_functions['func']['avg'].append((re.match(r'avg\((.+)\)', i, re.I)).group(1))

        if re.match(r'sum\((.+)\)', i, re.I) is not None:
            all_functions['func_flag'] = 1
            all_functions['func']['sum'].append((re.match(r'sum\((.+)\)', i, re.I)).group(1))

        if re.match(r'distinct\((.+)\)', i, re.I) is not None:
            all_functions['func_flag'] = 1
            all_functions['func']['distinct'].append((re.match(r'distinct\((.+)\)', i, re.I)).group(1)) 

#    print all_functions {'func': {'distinct': [], 'max': ['A'], 'sum': [], 'avg': [], 'min': ['B']}, 'func_flag': 1}
    return all_functions

query=[]
query = (sys.argv[1]).split(" ")
#-----------------------error checking--------------------------------
i=len(query)-1
j=len(query[i])-1
if query[i][j]!=';' or len(query) < 4 or query[0]!="select" or 'from' not in query or ('where' in query and len(query) < 6):
    print "syntax error1"
    sys.exit()

query[i] = query[i].replace(";", "")
#print "query",query

i=0
j=0
#-------------------------------------flags
star=0
distinct=0
singlecol=0
morecol=0
singletable=0
moretable=0
where=0
and_flag = 0
or_flag = 0
#----------------------------------------
tables = []
subtables = []

select_index = query.index('select')
from_index = query.index('from')

if "distinct" in query:
    distinct=1
    distinct_index = query.index('distinct')


if '*' in query:star=1

if "where" in query:
    where=1
    where_index = query.index('where')
    subtables = query[from_index+1 : where_index]
    for i in subtables:
        tables.extend(i.split(","))
        
    conditions = []
    conditions = query[where_index+1 : ]
    
    if 'where' in query and (conditions==[] or len(conditions) > 3):
         print "invalid conditions"
         sys.exit()

    cond_1 = []
    cond_2 = []
    
    if 'AND' in conditions or 'and' in conditions:
        and_flag=1
        cond_1 = query[where_index+1 : query.index('AND')]
        cond_2 = query[query.index('AND')+1 : ]
        cond_1 = "".join(cond_1)
        cond_2 = "".join(cond_2)

        cond_1 = cond_1.split("=")
        cond_2 = cond_2.split("=")
    
    elif 'OR' in conditions or 'or' in conditions:
        or_flag=1
        cond_1 = query[where_index+1 : query.index('OR')]
        cond_2 = query[query.index('OR')+1 : ]
        cond_1 = "".join(cond_1)
        cond_2 = "".join(cond_2)

        cond_1 = cond_1.split("=")
        cond_2 = cond_2.split("=")
    #cond_1, cond_2 are condition lists after and before and/or
    
    if (and_flag==1 or or_flag==1) and ((len(cond_1) + len(cond_2) > 4) or (len(cond_1) == 0 or len(cond_2) == 0)):
        print "invalid conditions"
        sys.exit()
        
else:
    subtables = query[from_index+1 : ]
    for i in subtables:
        tables.extend(i.split(","))

#tables.sort()
if len(tables)==1:
    singletable=1
elif len(tables)>1:
    moretable=1
#print tables
        
cols = []
if distinct==1:temp=select_index+2
else:temp=select_index+1
while temp != from_index:
    cols.extend(query[temp].split(","))        
    temp += 1

#print cols   ['max(A)', 'min(B)', 'C']
if len(cols)==1:singlecol=1
else:morecol=1

attr = cols[:]
all_funcs = aggregate(attr)


#-------*************************************************---------------------


#for queries with max, min, sum, avg, distinct

if all_funcs['func_flag'] == 1 and where == 0:
    
    table_name = query[len(query) - 1]
    df = pandas.read_csv(table_name + '.csv', names = table_attr(table_name,"metadata.txt"))

    exist_funcs = {}
    for key in all_funcs['func']:
        if all_funcs['func'][key] != []:
            exist_funcs[key] = all_funcs['func'][key]

    #print exist_funcs
    answer = []
    header = []
    l = []
    distinct_answer = []
    distinct_checked = []

    #################################################
    #for queries: select max(A), min(B), sum(C), avg(D) from table;
    for key in exist_funcs:
        for i in exist_funcs[key]:
            column_name =  table_name + '.' + i
            k = (list(df[table_name + '.' +i]))
            header.append(key + '(' + table_name+"."+i + ')')
            if key == 'max':
                answer.append(str(max(k)))

            if key == 'min':
                answer.append(str(min(k)))

            if key == 'avg':
                answer.append(str(numpy.mean(k)))

            if key == 'sum':
                answer.append(str(sum(k)))

    if len(all_funcs['func']['distinct']) == 0:
        print ",".join(header)
        print ",".join(answer)
        sys.exit()

# *************************************************************************************


if moretable==0 and where==0:   
    table_name = query[len(query) - 1]
    df = pandas.read_csv(table_name + '.csv', names = table_attr(table_name,"metadata.txt"))
    names = table_attr(table_name,"metadata.txt")
  
    #select * from tablename
    if star==1:
        header=[]
        ans=[]
        for i in range(len(names)):
          header.append(names[i])
        print ",".join(header)
        
        with open(table_name+".csv", "r+") as fp1:
            data = fp1.readlines()
#            print "data",data
            string = ''.join(data)
            string=string.split("\r\n")
#            print "stringo",string
           
        for i in range(len(string)):
           print string[i]
        sys.exit()
    
    #select A,B from tablename       
    elif star==0 and distinct==0:
        columns=[]
        header=[]
        ans=[]
        for i in range(len(cols)):
          header.append(table_name+"."+cols[i])
        print ",".join(header)
        
        for i in cols:
            if table_name+"."+i not in table_attr(table_name,"metadata.txt"):
                print "invalid columns selected"
                sys.exit()
                break
            else:
                columns.append(list(df[table_name+"."+i]))
                
        rows_count=len(columns[0])
        i=0    
        while i<rows_count:
            j = 0
            string=""
            while j<len(cols):
                string=string+str(columns[j][i])+','
                j=j+1
            print string.rstrip(',')
            i=i+1
            
    #select distinct A,B from tablename       
    elif star==0 and distinct==1:
        columns=[]
        for i in cols:   
            if table_name+"."+i not in table_attr(table_name,"metadata.txt"):
                print "invalid columns selected"
                sys.exit()
                break
            else:
                columns.append(list(df[table_name+"."+i]))
                
        header=[]
        duplicate_ans=[]
        ans=[]
        for i in range(len(cols)):
          header.append(table_name+"."+cols[i])
        print ",".join(header)
        
        rows_count=len(columns[0])
        i = 0
        while i<rows_count:
            foo=[]
            j = 0
            while j<len(cols):
                foo.append(columns[j][i])
                j+=1
            duplicate_ans.append(foo)
            i+=1
            
        for i in duplicate_ans:
            if i not in ans:
                ans.append(i)

        for i in range(len(ans)):
            string=""
            for j in range(len(ans[i])):
                 string=string+str(ans[i][j])+','
            print string.rstrip(',')

    
       
elif moretable==0 and where==1:
    table_name = query[from_index+1]
    df = pandas.read_csv(table_name + '.csv', names = table_attr(table_name,"metadata.txt"))
    names = table_attr(table_name,"metadata.txt")        

    # 1a. select A,B from tablename  where col=x 
    # 1b. select A,B from tablename  where col>x 
    # 1c. select A,B from tablename  where col<x 
    # 1d. select A,B from tablename  where col>=x 
    # 1e. select A,B from tablename  where col=<x 
    
    # 2. select A,B from tablename  where col=x  AND col=y
    # 3. select A,B from tablename  where col=x  OR col=y
    if star==0 and distinct==0:
        columns=[]
        header=[]
        ans=[]
        for i in range(len(cols)):
          header.append(table_name+"."+cols[i])
        print ",".join(header)
        
        # 1
        if and_flag==0 and or_flag==0:
            df=condfoo(conditions,df,table_name)
        # 2 
        elif and_flag==1 and or_flag==0:
           df=condfooand(conditions,cond_1,cond_2,table_name,df) 
           
        # 3 
        elif and_flag==0 and or_flag==1:
            df=df[df[str(table_name+"."+cond_1[0])]==int(cond_1[1]) | df[str(table_name+"."+cond_2[0])]==int(cond_2[1])]
#            df2=df[df[str(table_name+"."+cond_2[0])]==int(cond_2[1])]
        
        for i in cols:
            if table_name+"."+i not in table_attr(table_name,"metadata.txt"):
                print "invalid columns selected"
                sys.exit()
            else:
                if and_flag==0 and or_flag==1:
                    columns.append(list(df[table_name+"."+i]))
#                    columns.append(list(df2[str(table_name+"."+i)]))
                else:
                    columns.append(list(df[table_name+"."+i]))
                
        rows_count=len(columns[0])
        i = 0
        while i<rows_count:
            string=""
            j = 0
            while j<len(cols):
                string=string+str(columns[j][i])+','
                j=j+1

            print string.rstrip(',')
            i=i+1
        sys.exit()
            
#    select * from table1 where col=x
    elif star==1 and distinct==0:

        if and_flag==0 and or_flag==0:
            df=condfoo(conditions,df,table_name)
            
        elif and_flag==1 and or_flag==0:
            df=condfooand(conditions,cond_1,cond_2,table_name,df)
            
        header=[]
        ans=[]
        for i in range(len(names)):
          header.append(names[i])
        print ",".join(header)
        
        cola=[]
        attrbutes=table_attr(table_name,"metadata.txt")
        for i in attrbutes:
            cola.append(list(df[i]))
            
        rows_count=len(cola[0])
        i = 0
       
        while i<rows_count:
            string=""
            j = 0
            while j<len(attrbutes):
                string=string+str(cola[j][i])+','
                j=j+1

            print string.rstrip(',')
            i=i+1
        cola=[]
        sys.exit()

elif moretable==1:
    countatr_in_table1=len(table_attr(tables[0],"metadata.txt"))
    countatr_in_table2=len(table_attr(tables[1],"metadata.txt"))
    if where==1:
        congo=0
        onetwo=0
        twoone=0
        tonetwo=0
        ttwoone=0
        condindx=[]
        
        cong=''.join(conditions)
        cong=cong.split("=")
        if "." in cong[0] and "." in cong[1]:
            congo=1
        
        if congo==1:
            if "table1" in cong[0]:
                onetwo=1
            else:
                twoone=1
                
            if tables[0]=="table1":
                tonetwo=1
            else:
                ttwoone=1
                
            if onetwo==1 and tonetwo==1:
                if cong[0] in table_attr("table1","metadata.txt"):
                   condindx.append( table_attr("table1","metadata.txt").index(cong[0]))
                   condindx.append(countatr_in_table1+ table_attr("table2","metadata.txt").index(cong[1]))
                else:
                    print "error"
                    sys.exit()
                    
            
            elif onetwo==1 and tonetwo==0:
                if cong[0] in table_attr("table1","metadata.txt"):
                   condindx.append(countatr_in_table1+ table_attr("table1","metadata.txt").index(cong[0]))
                   condindx.append( table_attr("table2","metadata.txt").index(cong[1]))
                else:
                    print "error"
                    sys.exit()
                    
                    
            elif onetwo==0 and tonetwo==0:
                if cong[0] in table_attr("table2","metadata.txt"):
                   condindx.append( table_attr("table2","metadata.txt").index(cong[0]))
                   condindx.append( countatr_in_table1+table_attr("table1","metadata.txt").index(cong[1]))
                else:
                    print "error"
                    sys.exit()
                    
            elif onetwo==0 and tonetwo==1:
                if cong[0] in table_attr("table2","metadata.txt"):
                   condindx.append( countatr_in_table1+table_attr("table2","metadata.txt").index(cong[0]))
                   condindx.append( table_attr("table1","metadata.txt").index(cong[1]))
                else:
                    print "error"
                    sys.exit()
    
    tabledata1={"atr":[],"data":[]}
    tabledata2={"atr":[],"data":[]}
    mergedrow=[]
    
    countatr_in_table1=len(table_attr(tables[0],"metadata.txt"))
    with open(tables[0]+".csv", "r+") as fp1:
        data = fp1.readlines()
        for j in data:
            j=j.rstrip()
            j=j.split(",")
            tabledata1["data"].append(j)
    tabledata1["atr"].append(table_attr(tables[0],"metadata.txt"))
    
    with open(tables[1]+".csv", "r+") as fp2:
        data = fp2.readlines()
        for j in data:
            j=j.rstrip()
            j=j.split(",")
            tabledata2["data"].append(j)
    tabledata2["atr"].append(table_attr(tables[1],"metadata.txt"))

        
# take projection of tables
    
    for row1 in tabledata1["data"]:
        for row2 in tabledata2["data"]:
            mergedrow.append(row1+row2)
        
    mergedrowatr=[]
    for row1 in tabledata1["atr"]:
        for row2 in tabledata2["atr"]:
            mergedrowatr.append(row1+row2)
       
#    select * from table1,table2
    if star==1 and where==0:       
        for i in mergedrowatr:
            i=','.join(i)
            print i
        
        if distinct==0:
            for i in mergedrow:
                i=','.join(i)
                print i
            sys.exit()
            
        elif distinct==1:
            fab=[]
            for i in mergedrow:
                i=','.join(i)
                if i not in fab:
                    print i
                    fab.append(i)
            sys.exit()
    
#    select table.col1,table.col2 from table1,table2
    
    elif star==0 and where==0:
        countatr_in_table1=len(table_attr(tables[0],"metadata.txt"))
        indx=[]
        for i in attr:
            tbname=i.split(".")
            if i in table_attr(tbname[0],"metadata.txt"):
                if tbname[0]==tables[0]:
                    indx.append( table_attr(tbname[0],"metadata.txt").index(i))
                else:
                    indx.append(countatr_in_table1 + table_attr(tbname[0],"metadata.txt").index(i))
            else:
                print "error"
                sys.exit()
 
        ans=""
        for i in attr:
            ans=ans+i+","
        print ans.rstrip(",")
        
        if distinct==0:
            for i in range(len(mergedrow)):
                ans=""
                for j in indx:
                    ans= ans+mergedrow[i][j]+","
                print ans.rstrip(",")
            
        elif distinct==1:
            fab=[]
            for i in range(len(mergedrow)):
                ans=""
                for j in indx:
                    ans= ans+mergedrow[i][j]+","
                ans=ans.rstrip(",")
                if ans not in fab:
                    print ans
                    fab.append(ans)
            sys.exit()
            
    #    select * from table1,table2 where col=x        
    elif star==1 and where==1 and and_flag==0 and or_flag==0 and congo==0:
        cbname=conditions[0].split(".")
        colname=cbname[1].split("=")
        
        if cbname[0]==tables[0]:
            cbindex=table_attr(tables[0],"metadata.txt").index(cbname[0]+"."+colname[0])
       
        elif cbname[0]!=tables[0]:
            cbindex=countatr_in_table1 + table_attr(cbname[0],"metadata.txt").index(cbname[0]+"."+colname[0])
            
        for i in mergedrowatr:
            i=','.join(i)
            print i
        
        if distinct==0:
            for i in mergedrow:
                if i[cbindex]==colname[1]:
                    i=','.join(i)
                    print i
            sys.exit()
            
        elif distinct==1:
            fab=[]
            for i in mergedrow:
                if i[cbindex]==colname[1]:
                    i=','.join(i)
                    if i not in fab:
                        print i
                        fab.append(i)
            sys.exit()
    
    
    #    select table.col1,table.col2 from table1,table2 where col=x
    elif star==0 and where==1 and and_flag==0 and or_flag==0 and congo==0:
        countatr_in_table1=len(table_attr(tables[0],"metadata.txt"))
        indx=[]
        cbname=conditions[0].split(".")
        colname=cbname[1].split("=")
        
        if cbname[0]==tables[0]:
            cbindex=table_attr(tables[0],"metadata.txt").index(cbname[0]+"."+colname[0])
       
        elif cbname[0]!=tables[0]:
            cbindex=countatr_in_table1 + table_attr(cbname[0],"metadata.txt").index(cbname[0]+"."+colname[0])
            
#        print cbindex
            
        for i in attr:
            tbname=i.split(".")
            if i in table_attr(tbname[0],"metadata.txt"):
                if tbname[0]==tables[0]:
                    indx.append( table_attr(tbname[0],"metadata.txt").index(i))
                else:
                    indx.append(countatr_in_table1 + table_attr(tbname[0],"metadata.txt").index(i))
            else:
                print "error"
                sys.exit()
 
        ans=""
        for i in attr:
            ans=ans+i+","
        print ans.rstrip(",")
        
        if distinct==0:
            for i in range(len(mergedrow)):
                ans=""
                if mergedrow[i][cbindex]==colname[1]:
                    for j in indx:
                        ans= ans+mergedrow[i][j]+","
                    print ans.rstrip(",")
            
        elif distinct==1:
            fab=[]
            for i in range(len(mergedrow)):
                ans=""
                if mergedrow[i][cbindex]==colname[1]:
                    for j in indx:
                        ans= ans+mergedrow[i][j]+","
                    ans=ans.rstrip(",")
                    if ans not in fab:
                        print ans
                        fab.append(ans)
            sys.exit()
            
#    select * from table1,table2 where table1.B=table2.B
    elif star==1 and where==1 and and_flag==0 and or_flag==0 and congo==1:
        
        to1=table_attr(tables[0],"metadata.txt")
        to2=table_attr(tables[1],"metadata.txt")
        to1=','.join(to1)
        to2=','.join(to2)
        to1=to1+","+to2
        to1=to1.split(",")
        to1[condindx[1]]=""
        while '' in to1:
            to1.remove('')
        to1=','.join(to1)
        print to1

        if distinct==0:
            for i in mergedrow:
                if i[condindx[0]]==i[condindx[1]]:
                    i[condindx[1]]=""
                    while '' in i:
                        i.remove('')
                    i=','.join(i)
                    print i
            sys.exit()
            
        elif distinct==1:
            fab=[]
            for i in mergedrow:
                if i[condindx[0]]==i[condindx[1]]:
                    i[condindx[1]]=""
                    while '' in i:
                        i.remove('')
                    i=','.join(i)
                    if i not in fab:
                        print i
                        fab.append(i)
            sys.exit()
            
    #    select col,col from table1,table2 where table1.B=table2.B
    elif star==0 and where==1 and and_flag==0 and or_flag==0 and congo==1:
        atrindx=[]
        if (len(attr)>1 and '.' in attr[0] and '.' in attr[1]) or (len(attr)==1 and '.' in attr[0]):
            lo=[]
            for i in attr:
               j=i.split(".")
               if i in table_attr(j[0],"metadata.txt"):
                      lo.append(i)
                      atrindx.append(table_attr(j[0],"metadata.txt").index(i))
#        
            if tonetwo==1 and len(attr)>1:
                atrindx[1]+=countatr_in_table1
            elif ttwoone==1:
                atrindx[0]+=countatr_in_table1
        
        
        else:
            lo=[]
            for i in attr:
               if tables[0]+"."+i in table_attr(tables[0],"metadata.txt"):
                      lo.append(tables[0]+"."+i)
                      atrindx.append(table_attr(tables[0],"metadata.txt").index(tables[0]+"."+i))
               elif tables[1]+"."+i in table_attr(tables[1],"metadata.txt"):
                      lo.append(tables[1]+"."+i)
                      atrindx.append(table_attr(tables[1],"metadata.txt").index(tables[1]+"."+i))
               else:
                   print "syntax error"
            
            if tonetwo==1:
                atrindx[1]+=countatr_in_table1
            elif ttwoone==1:
                atrindx[0]+=countatr_in_table1
            
        
        s=""
        for i in lo:
            s+=i+","
        print s.rstrip(",")

        if distinct==0:
            for i in mergedrow:
                if i[condindx[0]]==i[condindx[1]]:
                    i[condindx[1]]=""
                    
                    suum=countatr_in_table1+countatr_in_table2
                    sumindx=0
                    while(suum!=0):
                        if len(attr)>1 and sumindx!=atrindx[0] and sumindx!=atrindx[1]:
                            i[sumindx]=""
                        if len(attr)==1 and sumindx!=atrindx[0]:
                            i[sumindx]=""    
                        sumindx+=1
                        suum-=1
                        
                    while '' in i:
                        i.remove('')
                    i=','.join(i)
                    print i
            sys.exit()
            
        elif distinct==1:
            fab=[]
            for i in mergedrow:
                if i[condindx[0]]==i[condindx[1]]:
                    i[condindx[1]]=""
                    
                    suum=countatr_in_table1+countatr_in_table2
                    sumindx=0
                    while(suum!=0):
                        if len(attr)>1 and sumindx!=atrindx[0] and sumindx!=atrindx[1]:
                            i[sumindx]=""
                        if len(attr)==1 and sumindx!=atrindx[0]:
                            i[sumindx]=""    
                        sumindx+=1
                        suum-=1
                        
                    while '' in i:
                        i.remove('')
                    i=','.join(i)
                    if i not in fab:
                        print i
                        fab.append(i)
            sys.exit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        