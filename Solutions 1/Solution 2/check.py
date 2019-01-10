dict = {}

def host(line):
    words = line.split()
    for i in range(len(words)):
        if words[i] in ('Consumer','Producer'):
            return words[i+1]

def checking(line):
    hostVal = host(line)
    firstPor,secondPor = line.split('[ERROR]')
    str = '[ERROR]'+secondPor
    if hostVal not in dict:
        #if key not in dict
        dict[hostVal] = [[1,str]]
    else:
        #if key and value already in dict
        for i in dict[hostVal]:
            if str in i:
                i[0] += 1
                break
        else:
            #if key in dict but not value
            dict[hostVal].append([1,str])

def display(total,infoCount):
    #for html
    import os
    this_folder = os.path.dirname(os.path.abspath(__file__))
    htmlFile = os.path.join(this_folder,'log.html')
    fw = open(htmlFile,'w')
    fw.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">')
    fw.write('<div class="container">')
    fw.write('<table class="table">')

    totalError = 0
    for key in dict:
        temp = 0
        dict[key].sort(reverse=True)
        print("Host ",key)
        print("============================")

        #for html
        fw.write('<thead class="thead-dark">')
        fw.write('<tr><th colspan="2">')
        htm = "<h3>Host "+key+"</h3>"
        fw.write(htm)
        fw.write("</th></tr>")
        fw.write("</thead>")
        fw.write("<tr><td><h4> Number of errors</h4></td>")
        fw.write("<td><h4> Error/WARNING</h4></td></tr>")
        ##

        for value in dict[key]:
            print(value[0], ' - ',value[1])
            temp += value[0]

            #for html
            htm = "<tr><td>"+str(value[0])+"</td>"
            fw.write(htm)
            htm = "<td>"+str(value[1])+"</td></tr>"
            fw.write(htm)
            ##

        # print(temp,"ERROR/WARNING")
        # print(infoCount[key]+temp,"total send")
        print(round((temp/(infoCount[key]+temp))*100),"% Error/Warning\n")

        #for htmlFile
        fw.write('<tr><td colspan="2">')
        htm = "<h4 style='color:#DC143C'>"+str(round((temp/(infoCount[key]+temp))*100))+"% Error/Warning</h4>"
        fw.write(htm)
        fw.write("</br></td></tr>")
        ##

        totalError += temp
    print("Total: ",round((totalError/total)*100),"% Error/Warning")

    #for html
    fw.write('<tr><td colspan="2">')
    htm = "<h4 style='color:#4682B4'>Total: "+str(round((temp/(infoCount[key]+temp))*100))+"% Error/Warning</h4>"
    fw.write(htm)
    fw.write("</td></tr>")
    fw.write("</table>")
    fw.write("</div>")
    fw.close()
    ##
