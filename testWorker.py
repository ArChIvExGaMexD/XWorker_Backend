import serial.tools.list_ports, os, sys
ports = serial.tools.list_ports.comports()
comports = []
for port, desc, hwid in sorted(ports):
    comports.append(port)
comports.pop(0)
if os.path.exists("XWorker.backend.log"):
    os.remove("XWorker.backend.log")
    logger = open("XWorker.backend.log", "x")
else:
    logger = open("XWorker.backend.log", "x")
def Log(strlog):
    logger.write(strlog)
class Terminal:
    def Pay(amount):
        if type(amount) == float:
            sum = int(amount)
            print("Сумма:"+str(sum))
            print('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o1 /a'+str(sum)+' /c643')
            os.system('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o1 /a'+str(sum)+' /c643')
            Log('proccessed payment '+str(sum))
        elif type(amount):
            sum = int(float(amount))
            print("Сумма:"+str(sum))
            print('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o1 /a'+str(sum)+' /c643')
            os.system('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o1 /a'+str(sum)+' /c643')
            Log('proccessed payment '+str(sum))
    def Return(amount):
        if type(amount) == float:
            sum = int(amount)
            print("Сумма:"+str(sum))
            print('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o3 /a'+str(sum)+' /c643')
            os.system('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o3 /a'+str(sum)+' /c643')
            Log('proccessed payment return'+str(sum))
        elif type(amount):
            sum = int(float(amount))
            print("Сумма:"+str(sum))
            print('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o3 /a'+str(sum)+' /c643')
            os.system('C:/Arcus2/CommandLineTool/bin/CommandLineTool.exe /o3 /a'+str(sum)+' /c643')
            Log('proccessed payment return '+str(sum))

def main():
    args = ' '.join(sys.argv[1:])
    if "PayInt" in args:
        amountsum = args.replace("PayInt", "")
        Terminal.Pay(int(amountsum))
    elif "Return" in args:
        amountsum = args.replace("Return", "")
        Terminal.Return(int(amountsum))
    
def CheckCanPayUseTerminal():
    if comports.__len__ == 0:
        exit(110)
    else:
        main()
CheckCanPayUseTerminal()